import taichi as ti
import numpy as np

res = 600
RESOLUTION = res
dx = 1.0
half_inv_dx = 0.5 / dx
dt = 0.03
p_jacobi_iters = 30
f_strength = 10000.0
dye_decay = 0.99

force_radius = res / 5.0
inv_dye_denom = 16.0 / (res / 15.0)**2
p_alpha = -dx * dx


# ti.init(arch=ti.opengl)
ti.init(arch=ti.cuda)

_velocities = ti.Vector(2, dt=ti.f32, shape=(res, res))
_new_velocities = ti.Vector(2, dt=ti.f32, shape=(res, res))
velocity_divs = ti.var(dt=ti.f32, shape=(res, res))
_pressures = ti.var(dt=ti.f32, shape=(res, res))
_new_pressures = ti.var(dt=ti.f32, shape=(res, res))
color_buffer = ti.Vector(3, dt=ti.f32, shape=(res, res))
_dye_buffer = ti.Vector(3, dt=ti.f32, shape=(res, res))
_new_dye_buffer = ti.Vector(3, dt=ti.f32, shape=(res, res))


class TexPair:
    def __init__(self, cur, nxt):
        self.cur = cur
        self.nxt = nxt

    def swap(self):
        self.cur, self.nxt = self.nxt, self.cur


velocities_pair = TexPair(_velocities, _new_velocities)
pressures_pair = TexPair(_pressures, _new_pressures)
dyes_pair = TexPair(_dye_buffer, _new_dye_buffer)


@ti.func
def clip_index(array2d, ind0, ind1):
    N0,N1 = array2d.shape
    ret = array2d[max(0, min(ind0, N0-1)), max(0, min(ind1, N1-1))]
    return ret


@ti.func
def bilinear_interp(vf, s, t):
    iu, iv = int(s), int(t)
    fu, fv = s - iu, t - iv
    a = clip_index(vf, iu, iv)
    b = clip_index(vf, iu+1, iv)
    c = clip_index(vf, iu, iv+1)
    d = clip_index(vf, iu+1, iv+1)
    tmp0 = a + fu*(b-a)
    tmp1 = c + fu*(d-c)
    ret = tmp0 + fv*(tmp1-tmp0)
    return ret


@ti.kernel
def advect(vf:ti.template(), qf:ti.template(), new_qf:ti.template()):
    for i, j in vf:
        tmp0 = i - dt*vf[i,j][0]
        tmp1 = j - dt*vf[i,j][1]
        new_qf[i, j] = bilinear_interp(qf, tmp0, tmp1)


@ti.kernel
def apply_impulse(vf:ti.template(), dyef:ti.template(), mouse_data:ti.ext_arr()):
    for i, j in vf:
        mouse_direction = ti.Vector([mouse_data[0],mouse_data[1]])
        dx = i + 0.5 - mouse_data[2]
        dy = j + 0.5 - mouse_data[3]
        d2 = dx * dx + dy * dy
        vf[i, j] += (f_strength * dt * ti.exp(-d2/force_radius)) * mouse_direction
        dc = dyef[i, j]
        if mouse_direction.norm() > 0.5:
            dc += ti.exp(-d2 * inv_dye_denom) * ti.Vector([mouse_data[4],mouse_data[5],mouse_data[6]])
        dyef[i, j] = dc * dye_decay


@ti.kernel
def divergence(vf: ti.template()):
    for i, j in vf:
        vl = clip_index(vf, i-1, j)[0]
        vr = clip_index(vf, i+1, j)[0]
        vb = clip_index(vf, i, j-1)[1]
        vt = clip_index(vf, i, j+1)[1]
        vc = clip_index(vf, i, j)
        if i == 0:
            vl = -vc[0]
        if i == res - 1:
            vr = -vc[0]
        if j == 0:
            vb = -vc[1]
        if j == res - 1:
            vt = -vc[1]
        velocity_divs[i, j] = (vr - vl + vt - vb) * half_inv_dx



@ti.kernel
def pressure_jacobi(pf: ti.template(), new_pf: ti.template()):
    for i, j in pf:
        pl = clip_index(pf, i-1, j)
        pr = clip_index(pf, i+1, j)
        pb = clip_index(pf, i, j-1)
        pt = clip_index(pf, i, j+1)
        div = velocity_divs[i, j]
        new_pf[i, j] = (pl + pr + pb + pt + p_alpha * div) * 0.25


@ti.kernel
def subtract_gradient(vf: ti.template(), pf: ti.template()):
    for i, j in vf:
        pl = clip_index(pf, i-1, j)
        pr = clip_index(pf, i+1, j)
        pb = clip_index(pf, i, j-1)
        pt = clip_index(pf, i, j+1)
        v = clip_index(vf, i, j)
        v = v - half_inv_dx * ti.Vector([pr - pl, pt - pb])
        vf[i, j] = v


@ti.kernel
def fill_color_v3(vf: ti.template()):
    for i, j in vf:
        v = vf[i, j]
        color_buffer[i, j] = ti.Vector([abs(v[0]), abs(v[1]), abs(v[2])])



def generate_mouse_data(gui, previous_mouse, previous_color):
    # [0:2]: normalized delta direction
    # [2:4]: current mouse xy
    # [4:7]: color
    gui.get_event(ti.GUI.PRESS) #DO nothing, just to capture key press
    if gui.is_pressed(ti.GUI.LMB):
        tmp0 = gui.get_cursor_pos() #(tuple,float,2) (x,y) in [0,1] from lower left corner
        mxy = np.array(tmp0, dtype=np.float32) * RESOLUTION
        if previous_mouse is None:
            # prevent too dark color
            ret = mxy, np.random.uniform(0.3, 0.7, size=3), np.zeros(7, dtype=np.float32)
        else:
            mdir = mxy - previous_mouse
            mdir = mdir / (np.linalg.norm(mdir) + 1e-5)
            ret = mxy, previous_color, np.array([*mdir, *mxy, *previous_color], dtype=np.float32)
    else:
        ret = None, None, np.zeros(7, dtype=np.float32)
    return ret

def interactive_stable_fluid():
    gui = ti.GUI('Stable-Fluid', (res, res))
    previous_mouse = None
    previous_color = None
    while gui.running:
        previous_mouse, previous_color, mouse_data = generate_mouse_data(gui, previous_mouse, previous_color)

        advect(velocities_pair.cur, velocities_pair.cur, velocities_pair.nxt)
        advect(velocities_pair.cur, dyes_pair.cur, dyes_pair.nxt)
        velocities_pair.swap() #TODO
        dyes_pair.swap()

        apply_impulse(velocities_pair.cur, dyes_pair.cur, mouse_data)

        divergence(velocities_pair.cur)
        for _ in range(p_jacobi_iters):
            pressure_jacobi(pressures_pair.cur, pressures_pair.nxt)
            pressures_pair.swap()

        subtract_gradient(velocities_pair.cur, pressures_pair.cur)
        fill_color_v3(dyes_pair.cur)

        gui.set_image(color_buffer.to_numpy())
        gui.show()


def np_circle(x0, y0, radius, angular_velocity, delta_time, num_per_round=30, max_round=100):
    ind0 = 0
    factor = 2*np.pi*angular_velocity*delta_time
    while ind0<max_round:
        ind1 = min(max_round, ind0+num_per_round)
        theta = factor*np.arange(ind0, ind1)
        cos_theta = np.cos(theta)
        sin_theta = np.sin(theta)
        x = x0 + radius*cos_theta
        y = y0 + radius*sin_theta
        ind0 = ind1
        yield from np.stack([x,y,-sin_theta,cos_theta], axis=1)

np_particle0 = np_circle(0.5, 0.5, 0.2, angular_velocity=0.3, delta_time=dt, max_round=1000)

def generate_fake_data():
    color_particle0 = np.random.uniform(0.3, 0.7, size=3)
    for x,y,delta_x,delta_y in np_particle0:
        yield np.array([delta_x, delta_y, x*RESOLUTION, y*RESOLUTION, *color_particle0], dtype=np.float32)


def fake_stable_fluid():
    gui = ti.GUI('Stable-Fluid', (res, res))
    for mouse_data in generate_fake_data():
        if not gui.running:
            break
        advect(velocities_pair.cur, velocities_pair.cur, velocities_pair.nxt)
        advect(velocities_pair.cur, dyes_pair.cur, dyes_pair.nxt)
        velocities_pair.swap() #TODO
        dyes_pair.swap()

        apply_impulse(velocities_pair.cur, dyes_pair.cur, mouse_data)

        divergence(velocities_pair.cur)
        for _ in range(p_jacobi_iters):
            pressure_jacobi(pressures_pair.cur, pressures_pair.nxt)
            pressures_pair.swap()

        subtract_gradient(velocities_pair.cur, pressures_pair.cur)
        fill_color_v3(dyes_pair.cur)

        gui.set_image(color_buffer.to_numpy())
        gui.show()


if __name__=='__main__':
    # interactive_stable_fluid()
    fake_stable_fluid()
