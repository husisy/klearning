import numpy as np
import scipy.linalg
import scipy.sparse
import scipy.sparse.linalg
import scipy.special
import matplotlib
import matplotlib.pyplot as plt
# import matplotlib.animation
import mpl_toolkits

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


import scipy.interpolate #TODO


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

def pde_lax_wendroff(wave_speed, xspan, tspan, ut0):
    num_x = xspan.shape[0]
    num_t = tspan.shape[0]
    dx = xspan[1] - xspan[0]
    dt = tspan[1] - tspan[0]
    c = wave_speed*dt/dx #courant_number
    u = np.zeros((num_t, num_x), dtype=np.float64)
    u[0] = ut0
    for i in range(1,num_t):
        ulast = u[i-1]
        u[i,1:-1] = c/2*(1+c)*ulast[:-2] + (1-c**2)*ulast[1:-1] - c/2*(1-c)*ulast[2:]
        u[i,0] = ulast[0]
        u[i,-1] = np.interp(xspan[-1]-wave_speed*dt, xspan[-2:], ulast[-2:])
    return u


def pde_lax_friedrich(wave_speed, xspan, tspan, ut0):
    num_x = xspan.shape[0]
    num_t = tspan.shape[0]
    dx = xspan[1] - xspan[0]
    dt = tspan[1] - tspan[0]
    c = wave_speed*dt/dx #courant_number
    u = np.zeros((num_t, num_x), dtype=np.float64)
    u[0] = ut0
    for i in range(1,num_t):
        ulast = u[i-1]
        u[i,1:-1] = (ulast[:-2]+ulast[2:])/2 - c*(ulast[2:]-ulast[:-2])/2
        u[i,0] = ulast[0]
        u[i,-1] = np.interp(xspan[-1]-wave_speed*dt, xspan[-2:], ulast[-2:])
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
