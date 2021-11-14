import os
import numpy as np
import scipy.linalg
import scipy.sparse
import scipy.sparse.linalg
import scipy.special
import matplotlib
import matplotlib.pyplot as plt
# import matplotlib.animation
import mpl_toolkits

hf_file = lambda *x: os.path.join('data',*x)
if not os.path.exists(hf_file()):
    os.makedirs(hf_file())

plt.ion()

def plt_subplots_3d(nrols=1, ncols=1, **kwargs):
    fig = plt.figure(**kwargs)
    ax_list = []
    grid = matplotlib.gridspec.GridSpec(nrols, ncols)
    hf0 = lambda x,y: grid[x,y].get_position(fig)
    for ind0 in range(nrols):
        tmp0 = []
        for ind1 in range(ncols):
            ax = mpl_toolkits.mplot3d.Axes3D(fig, rect=hf0(ind0,ind1), auto_add_to_figure=False)
            fig.add_axes(ax)
            tmp0.append(ax)
        ax_list.append(tmp0)
    if nrols==1:
        ax_list = ax_list[0]
    return fig, ax_list


def solve_triangular(npb, mid_element, up_element, down_element):
    ab = np.block([[np.array([0]), up_element], [mid_element], [down_element, np.array([0])]])
    ret = scipy.linalg.solve_banded((1,1), ab, npb)
    return ret


def plt_line_animation(data_dict, xdata=None, frame_interval_ms=100):
    assert all(x.ndim==2 for x in data_dict.values())
    assert len({x.shape for x in data_dict.values()})==1
    key_list = list(data_dict.keys()) #use this for order
    num_frame,num0 = data_dict[key_list[0]].shape
    if xdata is None:
        xdata = np.arange(num0)
    assert xdata.shape==(num0,)

    tmp0 = min(xdata),max(xdata)
    tmp1 = min(x.min() for x in data_dict.values()), max(x.max() for x in data_dict.values())
    fig = plt.figure()
    ax = fig.add_subplot(autoscale_on=False, xlim=tmp0, ylim=tmp1)
    tmp0 = np.empty(num0, dtype=np.float64)
    tmp0[:] = np.nan
    line_list = [ax.plot(xdata,tmp0,label=x)[0] for x in key_list]
    ax.legend(frameon=False)
    def hf_frame(ind0):
        for hline,key in zip(line_list, key_list):
            hline.set_ydata(data_dict[key][ind0])
        return line_list
    ani = matplotlib.animation.FuncAnimation(fig, hf_frame, frames=num_frame, interval=frame_interval_ms)
    # frame_interval(millisecond)
    return fig,ax,ani


def pde_forward_time_backward_space(wave_speed, xspan, tspan, ut0):
    num_x = xspan.shape[0]
    num_t = tspan.shape[0]
    dx = xspan[1] - xspan[0]
    dt = tspan[1] - tspan[0]
    c = wave_speed*dt/dx #courant_number
    u = np.zeros((num_t, num_x), dtype=np.float64)
    u[0] = ut0
    for i in range(1,num_t):
        ulast = u[i-1]
        u[i,1:-1] = (1-c)*ulast[1:-1] + c*ulast[:-2]
        u[i,0] = ulast[0]
        u[i,-1] = np.interp(xspan[-1]-wave_speed*dt, xspan[-2:], ulast[-2:])
    return u

def ftbs(u): # forward time backward space
    u[1:-1] = (1-c)*u[1:-1] + c*u[:-2]
    return u[1:-1]


def pde_upwind(wave_speed, xspan, tspan, ut0):
    # periodict BC
    num_x = xspan.shape[0]
    num_t = tspan.shape[0]
    dx = xspan[1] - xspan[0]
    dt = tspan[1] - tspan[0]
    u = np.zeros((num_t, num_x), dtype=np.float64)
    u[0] = ut0
    c = wave_speed*dt/dx #courant_number
    coeff0 = (abs(c)+c)/2
    coeff1 = 1 - abs(c)
    coeff2 = (abs(c)-c)/2
    for i in range(1,num_t):
        u0 = u[i-1]
        u[i,1:-1] = coeff0*u0[:-2] + coeff1*u0[1:-1] + coeff2*u0[2:]
        u[i,0] = coeff0*u0[-1] + coeff1*u0[0] + coeff2*u0[1]
        u[i,-1] = coeff0*u0[-2] + coeff1*u0[-1] + coeff2*u0[0]
    return u

def pde_forward_time_central_space(wave_speed, xspan, tspan, ut0):
    # periodict BC
    num_x = xspan.shape[0]
    num_t = tspan.shape[0]
    dx = xspan[1] - xspan[0]
    dt = tspan[1] - tspan[0]
    c = wave_speed*dt/dx #courant_number
    u = np.zeros((num_t, num_x), dtype=np.float64)
    u[0] = ut0
    coeff = -wave_speed*dt/(2*dx)
    coeff0 = c/2
    coeff1 = 1
    coeff2 = -c/2
    for i in range(1,num_t):
        u0 = u[i-1]
        u[i,1:-1] = coeff0*u0[:-2] + coeff1*u0[1:-1] + coeff2*u0[2:]
        u[i,0] = coeff0*u0[-1] + coeff1*u0[0] + coeff2*u0[1]
        u[i,-1] = coeff0*u0[-2] + coeff1*u0[-1] + coeff2*u0[0]
    return u

def pde_lax_wendroff(wave_speed, xspan, tspan, ut0):
    num_x = xspan.shape[0]
    num_t = tspan.shape[0]
    dx = xspan[1] - xspan[0]
    dt = tspan[1] - tspan[0]
    c = wave_speed*dt/dx #courant_number
    u = np.zeros((num_t, num_x), dtype=np.float64)
    u[0] = ut0
    coeff0 = (c**2+c)/2
    coeff1 = (1-c**2)
    coeff2 = (c**2-c)/2
    for i in range(1,num_t):
        u0 = u[i-1]
        u[i,1:-1] = coeff0*u0[:-2] + coeff1*u0[1:-1] + coeff2*u0[2:]
        u[i,0] = coeff0*u0[-1] + coeff1*u0[0] + coeff2*u0[1]
        u[i,-1] = coeff0*u0[-2] + coeff1*u0[-1] + coeff2*u0[0]
    return u


def pde_lax_friedrich(wave_speed, xspan, tspan, ut0):
    # periodict BC
    num_x = xspan.shape[0]
    num_t = tspan.shape[0]
    dx = xspan[1] - xspan[0]
    dt = tspan[1] - tspan[0]
    c = wave_speed*dt/dx #courant_number
    u = np.zeros((num_t, num_x), dtype=np.float64)
    u[0] = ut0
    coeff0 = (1+c)/2
    coeff1 = 0
    coeff2 = (1-c)/2
    for i in range(1,num_t):
        u0 = u[i-1]
        u[i,1:-1] = coeff0*u0[:-2] + coeff1*u0[1:-1] + coeff2*u0[2:]
        u[i,0] = coeff0*u0[-1] + coeff1*u0[0] + coeff2*u0[1]
        u[i,-1] = coeff0*u0[-2] + coeff1*u0[-1] + coeff2*u0[0]
    return u


def pde_macCormack(wave_speed, xspan, tspan, ut0):
    num_x = xspan.shape[0]
    num_t = tspan.shape[0]
    dx = xspan[1] - xspan[0]
    dt = tspan[1] - tspan[0]
    c = wave_speed*dt/dx #courant_number
    u = np.zeros((num_t, num_x), dtype=np.float64)
    u[0] = ut0
    for i in range(1,num_t):
        ulast = u[i-1]
        up = ulast.copy()
        up[:-1] = ulast[:-1] - c*(ulast[1:]-ulast[:-1])
        u[i,1:] = 0.5*(ulast[1:]+up[1:] - c*(up[1:]-up[:-1]))
        u[i,0] = ulast[0]
        # u[i,1:-1] = (ulast[:-2]+ulast[2:])/2 - c*(ulast[2:]-ulast[:-2])/2
        # u[i,0] = ulast[0]
        # u[i,-1] = np.interp(xspan[-1]-wave_speed*dt, xspan[-2:], ulast[-2:])
    return u

def demo_hyperbolic_pde():
    # u_t-a*u_x=0
    # https://folk.ntnu.no/leifh/teaching/tkt4140/._main072.html
    # Constants and parameters
    wave_speed = 1
    t0 = 0
    t1 = 1
    x0 = 0
    x1 = 2
    num_x = 150
    num_t = 100
    dt = (t1-t0)/(num_t-1)
    dx = (x1-x0)/(num_x-1)

    # hf_wave = lambda x: (x<=0.1).astype(np.float64)
    hf_wave = lambda x,x0=0.25,x1=0.75: np.where((x>x0) & (x<x1), np.sin(np.pi*(x-x0)/(x1-x0))**4, 0)

    xspan = np.linspace(x0, x1, num_x)
    tspan = np.linspace(t0, t1, num_t)
    ut0 = hf_wave(xspan)

    # to get a satisfying solution, courant_number should be very close to 1, but will become unstable
    courant_number = wave_speed*dt/dx
    if courant_number >= 1:
        print(f'[WARNING] courant_number={courant_number}, numerical scheme might be unstable')

    ret_ = hf_wave(xspan-wave_speed*tspan[:,np.newaxis])
    ret_ftbs = pde_forward_time_backward_space(wave_speed, xspan, tspan, ut0)
    ret_lax_wendroff = pde_lax_wendroff(wave_speed, xspan, tspan, ut0)
    ret_lax_friedrich = pde_lax_friedrich(wave_speed, xspan, tspan, ut0)
    ret_macCormack = pde_macCormack(wave_speed, xspan, tspan, ut0)

    # for linear advection, ret_lax_wendroff should be the same as ret_macCormack
    data_dict = {
        'analytical': ret_,
        'ftbs': ret_ftbs,
        'lax_wendroff': ret_lax_wendroff,
        'lax_friedrich': ret_lax_friedrich,
        'macCormack': ret_macCormack,
    }
    fig,ax,ani = plt_line_animation(data_dict, xdata=xspan, frame_interval_ms=100)
    return ani #otherwise animation will not work

def demo_figure_73_75_76():
    # upwind/LxW/LxF scheme fail to converge if not satisfy CFL condition
    # LxW is 2nd order accuracy in time and 2nd order in space
    # LxF is 1nd order accuracy in time and 1nd order in space
    # LxF is more diffusive and smoother
    wave_speed = 1
    t0 = 0
    t1 = 0.5
    x0 = 0
    x1 = 1
    # num_x_t_list = [(50,26),(50,25),(100,51),(100,50)]
    num_x_t_list = [(76,39),(76,38),(151,77),(151,75)]
    hf_ut0 = lambda x: np.logical_and(x<0.3, x>=0.2).astype(np.float64)
    cfl_list = [wave_speed*(t1-t0)/(y-1)*(x-1)/(x1-x0) for x,y in num_x_t_list]

    tmp0 = [
        ('figure_7_3.png',pde_upwind),
        ('figure_7_5.png',pde_lax_wendroff),
        ('figure_7_6.png',pde_lax_friedrich),
    ]
    for filename,hf_scheme in tmp0:
        ret = []
        for num_x,num_t in num_x_t_list:
            xspan = np.linspace(x0, x1, num_x)
            tspan = np.linspace(t0, t1, num_t)
            ut0 = hf_ut0(xspan)
            ut1 = hf_scheme(wave_speed, xspan, tspan, ut0)[-1]
            ret.append((xspan,ut0,ut1))
        fig,tmp0 = plt.subplots(2,2)
        ax_list = [tmp0[0][0],tmp0[0][1],tmp0[1][0],tmp0[1][1]]
        for ax,data,cfl in zip(ax_list,ret,cfl_list):
            xspan, ut0, ut1 = data
            ax.plot(xspan, ut0)
            ax.plot(xspan, ut1, '.-')
            ax.set_title(f'CFL={cfl:.3f}')
            ax.set_xlim(x0, x1)
            ax.set_ylim(-1, 2)
        fig.tight_layout()
        fig.savefig(hf_file(filename))

def demo_figure_7_4():
    # FTCS is unconditional unstable
    wave_speed = 1
    t0 = 0
    t1 = 0.5
    x0 = 0
    x1 = 1
    num_x_t_list = [(50,2450),(50,1226),(100,4950),(100,2475)]
    hf_ut0 = lambda x: np.logical_and(x<0.3, x>=0.2).astype(np.float64)
    cfl_list = [wave_speed*(t1-t0)/(y-1)*(x-1)/(x1-x0) for x,y in num_x_t_list]

    ret = []
    for num_x,num_t in num_x_t_list:
        xspan = np.linspace(x0, x1, num_x)
        tspan = np.linspace(t0, t1, num_t)
        ut0 = hf_ut0(xspan)
        ut1 = pde_forward_time_central_space(wave_speed, xspan, tspan, ut0)[-1]
        ret.append((xspan,ut0,ut1))

    fig,tmp0 = plt.subplots(2,2)
    ax_list = [tmp0[0][0],tmp0[0][1],tmp0[1][0],tmp0[1][1]]
    for ax,data,cfl in zip(ax_list,ret,cfl_list):
        xspan, ut0, ut1 = data
        ax.plot(xspan, ut0)
        ax.plot(xspan, ut1, '.-')
        ax.set_title(f'CFL={cfl:.3f}')
        ax.set_xlim(x0, x1)
        ax.set_ylim(-1, 2)
    fig.tight_layout()
    fig.savefig(hf_file('figure_7_4.png'))
