# https://forum.taichi.graphics/t/homework1-2d-thermal-time-implicit-and-poisson-solver-based-on-fdm-with-cg-and-mgpcg/999
# https://github.com/Trigolds/TaichiX
import numpy as np
import taichi as ti

ti.init(arch=ti.gpu, kernel_profiler=True)


@ti.data_oriented
class ConjugateGradientSolver:
    def __init__(self, Ngrid):
        self.K = 5 #thermal diffusivity
        self.h = 1
        self.dt = 5
        self.max_cg_step = 400
        self.Ngrid = Ngrid
        self.init_T = 293.15 # inital temperature
        self.bc_T = self.init_T + 300.0 # Boundary temperature
        # PDE equation see https://en.wikipedia.org/wiki/Thermal_diffusivity

        shape = Ngrid, Ngrid
        self.r = ti.field(ti.f32, shape=shape)
        self.x = ti.field(ti.f32, shape=shape)
        self.p = ti.field(ti.f32, shape=shape)
        self.Ap = ti.field(ti.f32, shape=shape)
        self.pAp = ti.field(ti.f32, shape=())
        self.rTr = ti.field(ti.f32, shape=())
        self.pixel = ti.Vector.field(3, dtype=ti.f32, shape=(Ngrid, Ngrid))

        self.r.fill(0)
        self.Ap.fill(0)
        self.pixel.fill(0)
        tmp0 = np.ones(shape, dtype=np.float32) * self.bc_T
        tmp0[1:-1,1:-1] = self.init_T
        self.x.from_numpy(tmp0)

    @ti.kernel
    def init_step(self):
        # x_t is the b_{t+1}
        tmp0 = self.K*self.dt/self.h**2
        for i,j in ti.ndrange((1,self.Ngrid-1), (1,self.Ngrid-1)):
            self.r[i,j] = self.x[i,j] - ((1.0 + 4.0*tmp0)*self.x[i,j] - tmp0*(self.x[i+1,j] + self.x[i-1,j] + self.x[i,j+1] + self.x[i,j-1]))
        self.rTr[None] = 0
        for i,j in self.p:
            self.p[i,j] = self.r[i,j]
            self.rTr[None] += self.r[i,j] * self.r[i,j]

    @ti.kernel
    def cg_substep(self):
        rTr_old = self.rTr[None]
        tmp0 = self.K*self.dt/self.h**2
        for i,j in ti.ndrange((1,self.Ngrid-1), (1,self.Ngrid-1)):
            self.Ap[i,j] = (1+4*tmp0)*self.p[i,j] - tmp0*(self.p[i+1,j] + self.p[i-1,j] + self.p[i,j+1] + self.p[i,j-1])
        self.pAp[None] = 0
        for i,j in self.p:
            self.pAp[None] += self.p[i,j]*self.Ap[i,j]
        alpha = rTr_old / self.pAp[None]
        for i,j in self.p:
            self.x[i,j] += alpha * self.p[i,j]
            self.r[i,j] -= alpha * self.Ap[i,j]

        self.rTr[None] = 0
        for i,j in self.r:
            self.rTr[None] += self.r[i,j] * self.r[i,j]
        beta = self.rTr[None] / rTr_old
        for i,j in self.p:
            self.p[i,j] = self.r[i,j] + beta * self.p[i,j]

    def step(self):
        self.init_step()
        for ind_iter in range(self.max_cg_step):
            self.cg_substep()
            if self.rTr[None] < 1e-5:
                break
        print(f'[iter={ind_iter}], residual={self.rTr[None]}')
        self.render()

    @ti.kernel
    def render(self):
        for i, j in self.pixel:
            val = (self.x[i,j] - self.init_T) / (self.bc_T - self.init_T)
            self.pixel[i,j][0] = val
            self.pixel[i,j][2] = 1-val


if __name__=='__main__':
    Ngrid = 2**10 + 1 #around 4FPS
    solver = ConjugateGradientSolver(Ngrid)
    gui = ti.GUI("Thermal2D", res=(Ngrid, Ngrid))
    while gui.running:
        if gui.get_event(ti.GUI.ESCAPE):
            break
        solver.step()
        solver.render()
        gui.set_image(solver.pixel.to_numpy())
        gui.show()
    ti.print_kernel_profile_info()
