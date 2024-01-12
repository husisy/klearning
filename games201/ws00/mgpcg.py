# Solve Poisson's equation on an NxN grid using MGPCG
import numpy as np

import taichi as ti

ti.init(default_fp=ti.f32, arch=ti.cpu, kernel_profiler=True)

# grid parameters
N = 128

x_a = 5
x_b = 5
x_c = 5

n_mg_levels = 4
pre_and_post_smoothing = 2
bottom_smoothing = 50

N_ext = N // 2  # number of ext cells set so that that total grid size is still power of 2
N_tot = 2 * N

# setup sparse simulation data arrays
r = [ti.field(dtype=ti.f32) for _ in range(n_mg_levels)]  # residual
z = [ti.field(dtype=ti.f32) for _ in range(n_mg_levels)]  # M^-1 r
x = ti.field(dtype=ti.f32)  # solution
p = ti.field(dtype=ti.f32)  # conjugate gradient
Ap = ti.field(dtype=ti.f32)  # matrix-vector product
zTr = ti.field(dtype=ti.f32, shape=())
rTr = ti.field(dtype=ti.f32, shape=())
pAp = ti.field(dtype=ti.f32, shape=())

ti.root.pointer(ti.ijk, N_tot//4).dense(ti.ijk, 4).place(x, p, Ap)

for l in range(n_mg_levels):
    ti.root.pointer(ti.ijk, N_tot//(4*2**l)).dense(ti.ijk,4).place(r[l], z[l])

@ti.kernel
def restrict(l: ti.template()):
    for i, j, k in r[l]:
        res = r[l][i,j,k] - (6.0*z[l][i,j,k] - z[l][i+1,j,k] - z[l][i-1,j,k]
                - z[l][i,j+1,k] - z[l][i,j-1,k] - z[l][i,j,k+1] - z[l][i,j,k-1])
        r[l+1][i//2,j//2,k//2] += res * 0.5


@ti.kernel
def prolongate(l: ti.template()):
    for I in ti.grouped(z[l]):
        z[l][I] = z[l + 1][I // 2]


@ti.kernel
def smooth(l: ti.template(), phase: ti.template()):
    # phase = red/black Gauss-Seidel phase
    for i, j, k in r[l]:
        if (i + j + k) & 1 == phase:
            z[l][i,j,k] = (r[l][i,j,k] + z[l][i+1,j,k] + z[l][i-1,j,k]
                    + z[l][i,j+1,k] + z[l][i,j-1,k] + z[l][i,j,k+1] + z[l][i,j,k-1])/6


def apply_preconditioner():
    z[0].fill(0)
    for l in range(n_mg_levels - 1):
        for _ in range(pre_and_post_smoothing*(2**l)):
            smooth(l, 0)
            smooth(l, 1)
        z[l + 1].fill(0)
        r[l + 1].fill(0)
        restrict(l)

    for _ in range(bottom_smoothing):
        smooth(n_mg_levels - 1, 0)
        smooth(n_mg_levels - 1, 1)

    for l in reversed(range(n_mg_levels - 1)):
        prolongate(l)
        for _ in range(pre_and_post_smoothing*(2**l)):
            smooth(l, 1)
            smooth(l, 0)
@ti.kernel
def init():
    for i, j, k in ti.ndrange((N_ext, N_tot-N_ext), (N_ext, N_tot-N_ext), (N_ext, N_tot-N_ext)):
        xl = (i-N_ext)*2.0/N_tot
        yl = (j-N_ext)*2.0/N_tot
        zl = (k-N_ext)*2.0/N_tot
        # r[0] = b - Ax, where x = 0; therefore r[0] = b
        r[0][i,j,k] = ti.sin(2.0*x_a*np.pi*xl) * ti.sin(2.0*x_b*np.pi*yl) * ti.sin(2.0*x_c*np.pi*zl)
        Ap[i,j,k] = 0.0
        p[i,j,k] = 0.0
        x[i,j,k] = 0.0

@ti.kernel
def initstep():
    zTr[None] = 0
    for I in ti.grouped(r[0]):
        zTr[None] += z[0][I] * r[0][I]
    rTr[None] = 0
    for I in ti.grouped(r[0]):
        rTr[None] += r[0][I] * r[0][I]

@ti.kernel
def substepA():
    for i, j, k in Ap:
        # A is implicitly expressed as a 3-D laplace operator
        Ap[i,j,k] = 6.0 * p[i,j,k] - p[i+1,j,k] - p[i-1,j,k] - p[i,j+1,k] - p[i,j-1,k] - p[i,j,k+1] - p[i,j,k-1]
    pAp[None] = 0
    for I in ti.grouped(p):
        pAp[None] += p[I] * Ap[I]
    alpha = zTr[None] / pAp[None]
    for I in ti.grouped(p):
        x[I] += alpha * p[I]
    for I in ti.grouped(p):
        r[0][I] -= alpha * Ap[I]
    rTr[None] = 0.0
    for I in ti.grouped(r[0]):
        rTr[None] += r[0][I] * r[0][I]

@ti.kernel
def substepB():
    tmp0 = zTr[None]
    zTr[None] = 0.0
    for I in ti.grouped(z[0]):
        zTr[None] += z[0][I] * r[0][I]
    beta = zTr[None] / tmp0
    for I in ti.grouped(p):
        p[I] = z[0][I] + beta * p[I]

init()

# r = b - Ax = b    since x = 0
# p = r = r + 0 p
apply_preconditioner()
p.copy_from(z[0])
initstep()
initial_rTr = rTr[None]

# CG
for i in range(400):
    substepA()
    print(f'Iter = {i:4}, Residual = {rTr[None]:e}')
    if rTr[None] < initial_rTr * 1.0e-12:
        break

    # z = M^-1 r
    apply_preconditioner()

    substepB()

ti.print_kernel_profile_info()

# CPU: AMD-R7-5800H
# GPU: gtx3060
## PCG
# GPU: N=128, step=246, time=0.743s
# GPU: N=256, step=596, time=12.5s
# GPU: N=512, step=1033, time=169s
## MGPCG
# CPU: N=128, time=1.01s
# CPU: N=256, time=7.04s
# CPU: N=512, time=88.3s
# GPU: N=128, step=7, time=0.227s
# GPU: N=256, step=7, time=1.83s
# GPU: N=512, step=12, time=10.6s

ind0 = slice(N_ext, N_ext+N)
zc0 = x.to_numpy()
tmp0 = zc0.copy()
tmp0[ind0,ind0,ind0] = 0
assert (tmp0.max()<1e-7) and (tmp0.min()>-1e-7)
zc1 = zc0[ind0,ind0,ind0].copy()
tmp0 = zc1*6
tmp0[1:] -= zc1[:-1]
tmp0[:-1] -= zc1[1:]
tmp0[:,1:] -= zc1[:,:-1]
tmp0[:,:-1] -= zc1[:,1:]
tmp0[:,:,1:] -= zc1[:,:,:-1]
tmp0[:,:,:-1] -= zc1[:,:,1:]
hf0 = lambda A,x,y,z: 6*A[x,y,z] - A[x+1,y,z] - A[x-1,y,z] - A[x,y+1,z] - A[x,y-1,z] - A[x,y,z+1] - A[x,y,z-1]
tmp1 = np.sin(2*x_a*np.pi*np.linspace(0, 1, N, endpoint=False))
tmp2 = np.sin(2*x_b*np.pi*np.linspace(0, 1, N, endpoint=False))
tmp3 = np.sin(2*x_c*np.pi*np.linspace(0, 1, N, endpoint=False))
print('norm_max(error)', np.abs(tmp0-tmp1[:,np.newaxis,np.newaxis]*tmp2[:,np.newaxis]*tmp3).max())
