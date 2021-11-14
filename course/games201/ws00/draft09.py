# https://forum.taichi.graphics/t/homework-0-molecular-dynamics/717
import numpy as np
import taichi as ti

ti.init(arch=ti.gpu)

DIM = 3
WINDOW_SIZE = 1024
rgb2hex = lambda x: x[0].astype(np.int64) * 65536 + x[1].astype(np.int64) * 256 + x[2].astype(np.int64)

@ti.data_oriented
class MolecularDynamics:
    # cutoff radius, interaction is not calculated if two particles are farther than cutoff
    rcut = 2.5
    ecut = 4. * (1. / rcut ** 12 - 1. / rcut ** 6)
    # thermostat "damping" coefficients
    Q1 = 5
    Q2 = 5

    def __init__(self, density, temperature, boxlength, dt):
        self.rho = density
        self.boxlength = boxlength
        self.dt = dt
        self.n_particles = int(density * boxlength ** DIM)

        self.position = ti.Vector.field(DIM, dtype=ti.f32, shape=self.n_particles)
        self.velocity = ti.Vector.field(DIM, dtype=ti.f32, shape=self.n_particles)
        self.force = ti.Vector.field(DIM, dtype=ti.f32, shape=self.n_particles)

        self.ek = ti.field(ti.f32, shape=()) #kinetic energy
        self.ep = ti.field(ti.f32, shape=()) #potential energy
        self.temp = ti.field(ti.f32, shape=()) #temperature
        self.xi = ti.field(ti.f32, shape=2)
        self.vxi = ti.field(ti.f32, shape=2)
        self.xi.fill(0)
        self.vxi.fill(0)
        self.temp.fill(temperature)

        # place particles on a regular grid, randomize their velocities according to the temperature
        n_pow = int(np.ceil(self.n_particles ** (1/DIM)))
        tmp0 = [(self.boxlength/n_pow) * (0.5 + np.arange(n_pow)) for _ in range(DIM)]
        self.position.from_numpy(np.stack(np.meshgrid(*tmp0)).reshape(DIM, -1)[:, :self.n_particles].T)
        vs = np.random.random((self.n_particles, DIM))
        vs -= vs.mean(axis=0)
        vs *= np.sqrt(DIM * self.temp[None] * self.n_particles / np.sum(vs ** 2))
        self.velocity.from_numpy(vs)

    '''
    Calculates distance with periodic boundary conditions and wraps a particle into the simulation box.
    '''
    @ti.func
    def calc_distance(self, x1, x2):
        dist = ti.Vector([0.0] * DIM)
        for i in ti.static(range(DIM)):
            dist[i] = x1[i] - x2[i]
            if dist[i] <= -0.5 * self.boxlength:
                dist[i] += self.boxlength
            elif dist[i] > 0.5 * self.boxlength:
                dist[i] -= self.boxlength
        return dist

    @ti.func
    def wrap(self, x):
        for i in ti.static(range(DIM)):
            if x[i] <= 0:
                x[i] += self.boxlength
            elif x[i] > self.boxlength:
                x[i] -= self.boxlength
        return x

    @ti.kernel
    def integrate_thermostat_half_step(self):
        self.vxi[1] += 0.25*self.dt*(self.Q1*self.vxi[0]**2 - self.temp[None])
        G1 = (2*self.ek[None] - 3*self.n_particles*self.temp[None])/self.Q1
        self.vxi[0] = self.vxi[0]*ti.exp(-0.25*self.dt*self.vxi[1]) + 0.25*self.dt*G1*ti.exp(-0.125*self.dt*self.vxi[1])

        self.xi[0] += 0.5*self.dt*self.vxi[0]
        self.xi[1] += 0.5*self.dt*self.vxi[1]
        s = ti.exp(-0.5*self.dt*self.vxi[0])
        self.ek[None] *= s * s

        G1 = (2*self.ek[None] - 3*self.n_particles*self.temp[None])/self.Q1
        self.vxi[0] = self.vxi[0]*ti.exp(-0.25*self.dt*self.vxi[1]) + 0.25*self.dt*G1*ti.exp(-0.125*self.dt*self.vxi[1])
        self.vxi[1] += 0.25*self.dt/self.Q2*(self.Q1*self.vxi[0]**2 - self.temp[None])
        for i in self.velocity:
            self.velocity[i] *= s

    '''
    Integrate the motion of particles. Use Newton'w law of motion and
    verlet integration scheme. Also calculates the kinetic and potential energies.
    '''
    @ti.kernel
    def integrate_motion(self):
        self.ek[None] = 0
        self.ep[None] = 0
        for i in self.position:
            self.position[i] = self.wrap(self.position[i] + 0.5*self.dt*self.velocity[i])
            self.force[i].fill(0)
        for i, j in ti.ndrange(self.n_particles, self.n_particles):
            if i < j:
                d = self.calc_distance(self.position[i], self.position[j])
                r2 = (d ** 2).sum()
                if r2 < self.rcut ** 2:
                    rf_norm = 24*(2/r2**6 - 1/r2**3)/r2
                    self.force[i] += rf_norm * d
                    self.force[j] -= rf_norm * d
                    self.ep[None] += 4*(1/r2**6 - 1/r2**3) - self.ecut

        for i in self.position:
            self.velocity[i] = self.velocity[i] + self.force[i] * self.dt
            self.ek[None] += (self.velocity[i] ** 2).sum() / 2
            self.position[i] = self.wrap(self.position[i] + self.velocity[i] * self.dt * 0.5)


if __name__ == "__main__":
    num_particle = 4000
    density = 0.1
    temperature = 0.5
    dt = 5e-3
    boxlength = (num_particle/density) ** (1/DIM) #34
    md = MolecularDynamics(density, temperature, boxlength, dt)
    gui = ti.GUI("MD", res=WINDOW_SIZE)

    # color
    bg = np.array([17, 47, 65])
    circ = np.array([122, 200, 225])

    # initially run a few steps at a high temperature to randomize the structure
    md.temp.fill(1.5)
    for _ in range(1000):
        if not gui.running:
            break
        md.integrate_thermostat_half_step()
        md.integrate_motion()
        md.integrate_thermostat_half_step()

    md.temp.fill(temperature)
    # Press UP to increase the temperature and press DOWN to decrease
    while gui.running:
        for _ in range(10): #render every 10 frame
            md.integrate_thermostat_half_step()
            md.integrate_motion()
            md.integrate_thermostat_half_step()

        gui.clear(rgb2hex(bg))
        while gui.get_event(ti.GUI.PRESS):
            if gui.event.key == ti.GUI.ESCAPE:
                exit()
            if gui.event.key == ti.GUI.UP:
                md.temp[None] = round(md.temp[None] + 0.1, 1)
            if gui.event.key == ti.GUI.DOWN:
                if md.temp[None] <= 0.15:
                    md.temp[None] /= 2
                else:
                    md.temp[None] = round(md.temp[None] - 0.1, 1)
        xy = md.position.to_numpy()
        z = xy[:, 2]
        xy = xy[:, :2]
        z_order = np.argsort(z)[::-1] #the larger z comes first
        sizes = 8 * boxlength / (boxlength + z) #the larger z is, the smaller the circle will be
        z = (1 - z / np.max(z))
        colors = rgb2hex(np.outer(bg, 1 - z) + np.outer(circ, z))
        t_actual = 2 * md.ek[None] / (md.n_particles * DIM)
        color_t = 0xf56060 if abs(t_actual - md.temp[None]) > 0.02 else 0x74e662
        gui.circles(xy / boxlength, radius=sizes[z_order], color=colors[z_order])
        gui.text("T_set = %.3g" % md.temp[None], (0.05, 0.2), font_size=36)
        gui.text("T_actual = %.3g" % t_actual, (0.05, 0.15), font_size=36, color=color_t)
        gui.text("Internal energy = %.3f" % (md.ek[None] + md.ep[None]), (0.05, 0.1), font_size=36)
        gui.show()
