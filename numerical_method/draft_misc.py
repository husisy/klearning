import os
import numpy as np
import scipy.integrate
import matplotlib.pyplot as plt

plt.ion()

hf_file = lambda *x: os.path.join('data',*x)
if not os.path.exists(hf_file()):
    os.makedirs(hf_file())

def hf_velocity(t, xy, epsilon, omega, A):
    x,y = xy
    a = epsilon*np.sin(omega*t)
    b = 1-2*a
    f = a*x**2 + b*x
    u = -np.pi*A*np.sin(np.pi*f) * np.cos(np.pi*y) * (1+(x>0))
    v = np.pi*A*np.cos(np.pi*f) * np.sin(np.pi*y) * (2*a*x+b)
    ret = np.stack([u,v])
    return ret

def plot_figure_3_9()
    epsilon = 0.1
    omega = np.pi/5
    A = 0.1

    N0 = 1000
    theta = np.linspace(0, 2*np.pi, N0)
    radius = 0.2
    xy_t0 = radius*np.stack([np.cos(theta),np.sin(theta)], axis=1) + np.array([1,0.75])
    tspan = np.linspace(0, 4, 4)
    ret = []
    for xy_i in xy_t0:
        ret.append(scipy.integrate.solve_ivp(hf_velocity, (tspan[0],tspan[-1]), xy_i, args=(epsilon,omega,A), t_eval=tspan).y)
    ret = np.stack(ret).transpose(2,1,0) #(4,2,1000)

    xmesh,ymesh = np.meshgrid(np.linspace(0,2,20), np.linspace(0,1,10), indexing='ij')
    tmp0 = np.stack([xmesh,ymesh])
    uv_list = [hf_velocity(t, tmp0, epsilon, omega, A) for t in tspan] #(4,2,20,10)

    fig,tmp0 = plt.subplots(2,2)
    ax_list = [tmp0[0][0],tmp0[0][1],tmp0[1][0],tmp0[1][1]]
    for xy,uv,ax,t in zip(ret,uv_list,ax_list,tspan):
        ax.quiver(xmesh, ymesh, uv[0], uv[1], color='b')
        ax.plot(xy[0], xy[1], color='r')
        ax.set_title(f't={t:.3f}')
        ax.set_aspect('equal')
    fig.tight_layout()
    fig.savefig(hf_file('fig_3_9.png'))
