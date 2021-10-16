import numpy as np
import scipy.linalg
import scipy.fft
import scipy.sparse
import scipy.sparse.linalg
import scipy.special
import matplotlib
import matplotlib.pyplot as plt
import mpl_toolkits

hfe = lambda x,y:np.max(np.abs(x-y)/(np.abs(x)+np.abs(y)+1e-3))

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

def _heat_diffusion_hf_analytical(diffusion_coeff, x_length, num_x, t_length, num_t, num_order=100):
    xspan = np.linspace(0, x_length, num_x)
    tspan = np.linspace(0, t_length, num_t)
    ret = []
    tmp0 = np.pi**2*diffusion_coeff/x_length**2
    tmp1 = np.pi/x_length
    for t in tspan:
        tmp2 = sum(np.exp(-t*tmp0*n**2)*np.sin(n*tmp1*xspan)/n for n in range(1,num_order+1))
        ret.append(1-xspan/x_length-(2/np.pi)*tmp2)
    ret = np.stack(ret)
    return ret


def _heat_diffusion_hf_FTCS(diffusion_coeff, x_length, num_x, t_length, num_t, ux0, ux1, ut0):
    # Method that solves the transient Couette Flow using the FTCS-scheme..
    u = np.zeros((num_t, num_x), dtype=np.float64)
    u[0] = ut0
    u[:,0] = ux0
    u[:,-1] = ux1
    tmp0 = diffusion_coeff*(t_length/(num_t-1))*((num_x-1)/x_length)**2
    for n in range(1, num_t):
        u[n,1:-1] = u[n-1,1:-1] + tmp0*(u[n-1,:-2] + u[n-1,2:] - 2*u[n-1,1:-1])
    return u


def demo_heat_diffusion():
    # u_t=D u_xx
    # u(x,0)=0
    # u(0,t)=0, u(1,t)=1
    # https://folk.ntnu.no/leifh/teaching/tkt4140/._main059.html
    diffusion_coeff = 1
    x_length = 1
    num_x = 50
    t_length = 0.05
    num_t = 500
    ux0 = 1 #must be 1 for analytical solution
    ux1 = 0 #must be 0 for analytical solution
    ut0 = np.zeros(num_x)

    dx = x_length/(num_x-1)
    dt = t_length/(num_t-1)
    xspan = np.linspace(0, x_length, num_x)
    tspan = np.linspace(0, t_length, num_t)
    numerical_diffusion_number = diffusion_coeff * dt / dx**2
    if numerical_diffusion_number > 0.5:
        #Bender-Schmidt formula
        print('[WARNING] FTCS scheme maybe unstable')

    ret_ = _heat_diffusion_hf_analytical(diffusion_coeff, x_length, num_x, t_length, num_t, num_order=100)
    ret0 = _heat_diffusion_hf_FTCS(diffusion_coeff, x_length, num_x, t_length, num_t, ux0, ux1, ut0)

    #Crank-Nicolson scheme, theta-scheme
    # TODO non-ignorable error
    # https://folk.ntnu.no/leifh/teaching/tkt4140/._main065.html
    u = np.zeros((num_t,num_x), dtype=np.float64)
    theta = 0.5
    u[0] = ut0
    u[:,0] = ux0
    u[:,-1] = ux1
    matA = scipy.sparse.lil_matrix((num_x-2,num_x-2), dtype=np.float64)
    matA.setdiag(-2*theta-1/numerical_diffusion_number, k=0)
    matA.setdiag(theta, k=1)
    matA.setdiag(theta, k=-1)
    matA = matA.tocsr()
    tmp0 = 2-2*theta-1/numerical_diffusion_number
    for n in range(1,num_t):
        matB = -(1-theta)*(u[n-1,2:]+u[n-1,:-2]) + tmp0*u[n-1,1:-1]
        u[n,1:-1] = scipy.sparse.linalg.spsolve(matA, matB)
    ret1 = u

    xdata,ydata = np.meshgrid(xspan, tspan)
    fig,((ax0,ax1),(ax2,ax3)) = plt_subplots_3d(nrols=2, ncols=2)
    ax_list = [ax0,ax1,ax2,ax3]
    ax0.plot_surface(xdata, ydata, ret_, rstride=1, cstride=1, cmap=matplotlib.cm.coolwarm, linewidth=0, antialiased=True)
    ax1.plot_surface(xdata, ydata, ret0, rstride=1, cstride=1, cmap=matplotlib.cm.coolwarm, linewidth=0, antialiased=True)
    ax2.plot_surface(xdata, ydata, ret1, rstride=1, cstride=1, cmap=matplotlib.cm.coolwarm, linewidth=0, antialiased=True)
    for ax in [ax0,ax1,ax2]:
        ax.set_xlabel('x')
        ax.set_ylabel('t')
    ax0.set_title('analytical')
    ax1.set_title('FTCS')
    ax1.set_title('theta')

    # fig = plt.figure(figsize=(5, 4))
    # tmp0 = min(ret0.min(), ret_.min()), max(ret0.max(), ret_.max())
    # ax = fig.add_subplot(autoscale_on=False, xlim=(xspan.min(), xspan.max()), ylim=tmp0)
    # hline0 = ax.plot([], [], lw=2, label='FTCS')[0]
    # hline1 = ax.plot([], [], lw=2, label='analytic')[0]
    # htext = ax.text(0.3, 0.9, '', transform=ax.transAxes)
    # ax.legend()
    # def hf_frame(ind0):
    #     hline0.set_data(xspan, ret0[ind0])
    #     hline1.set_data(xspan, ret_[ind0])
    #     htext.set_text(f'time = {tspan[ind0]:.3f}s')
    #     return hline0,hline1,htext
    # ani = matplotlib.animation.FuncAnimation(fig, hf_frame, frames=len(ret0), interval=20)
    # ani._start()
    # ani.pause()
    # ani.resume()
    # return ani #animation will stop if the variable ani is garbage-collected


def _heat_diffusion_radial_hf_analytic(num_r, num_t, t_length, num_order=30):
    rspan = np.linspace(0, 1, num_r)
    tspan = np.linspace(0, t_length, num_t)
    bessel_root = scipy.special.jn_zeros(0, num_order)

    ret = np.zeros((num_t, num_r), dtype=np.float64)
    ret[0] = 1-rspan**2
    tmp0 = scipy.special.jv(0, rspan[:,np.newaxis]*bessel_root) / (scipy.special.jv(1, bessel_root)*(bessel_root**3))
    for ind0 in range(1,num_t):
        ret[ind0] = 8 * (np.exp(-tspan[ind0]*bessel_root**2) * tmp0).sum(axis=1)
    return ret


def _heat_diffusion_radial_hf_theta_scheme_v1(diffusion_coeff, theta, t_length, num_t, r_length, num_r, ut0, ur1):
    # using L'hopital for the boundary condition at r=0
    dr = r_length/(num_r-1)
    dt = t_length/(num_t-1)
    rspan = np.linspace(0, r_length, num_r)
    D = diffusion_coeff * dt / (dr**2) #numerical_diffusion_number
    D_tilde = (diffusion_coeff+1) * dt / (dr**2)
    mid_element = np.ones(num_r-1)*(1+2*theta*D)
    mid_element[0] = 1 + 2*D_tilde*theta
    up_element = np.zeros(num_r-2, dtype=np.float64)
    up_element[1:] = -D*theta - (dr*D*theta/2)/rspan[1:-2]
    up_element[0] = -2*D_tilde*theta
    down_element = -D*theta + (dr*D*theta/2)/rspan[1:-1]

    u = np.zeros((num_t,num_r), dtype=np.float64)
    u[:,-1] = ur1
    u[0] = ut0
    for n in range(1,num_t):
        ulast = u[n-1]
        b_element = np.zeros(num_r-1)
        b_element[1:] = ulast[1:-1] + D*(1-theta)*(ulast[2:]+ulast[:-2]-2*ulast[1:-1]) + (1-theta)*dr*D/2/rspan[1:-1]*(ulast[2:]-ulast[:-2])
        b_element[0] = 2*(1-theta)*D_tilde*ulast[1] + (1-2*D_tilde*(1-theta))*ulast[0]
        b_element[-1] += (D*theta + (dr*D/2)/rspan[-2])*ur1
        tmp0 = solve_triangular(b_element, mid_element, up_element, down_element)
        u[n,:-1] = solve_triangular(b_element, mid_element, up_element, down_element)
    return u

def _heat_diffusion_radial_hf_theta_scheme_v2(diffusion_coeff, theta, t_length, num_t, r_length, num_r, ut0, ur1):
    # using 2nd order forward difference for the boundary condition at r=0
    dr = r_length/(num_r-1)
    dt = t_length/(num_t-1)
    rspan = np.linspace(0, r_length, num_r)
    D = diffusion_coeff * dt / (dr**2) #numerical_diffusion_number
    mid_element = np.ones(num_r-2)*(1+2*theta*D)
    mid_element[0] = 1 + 4/3*D*theta
    up_element = np.zeros(num_r-3, dtype=np.float64)
    up_element[1:] = -D*theta - (dr*D*theta/2)/rspan[2:-2]
    up_element[0] = -4/3*D*theta
    down_element = -D*theta + (dr*D*theta/2)/rspan[2:-1]

    u = np.zeros((num_t,num_r), dtype=np.float64)
    u[:,-1] = ur1
    u[0] = ut0
    for n in range(1,num_t):
        ulast = u[n-1]
        b_element = np.zeros(num_r-2)
        b_element[1:] = ulast[2:-1] + D*(1-theta)*(ulast[3:]+ulast[1:-2]-2*ulast[2:-1]) + (1-theta)*dr*D/2/rspan[2:-1]*(ulast[3:]-ulast[1:-2])
        b_element[0] = (1-4/3*D*(1-theta))*ulast[1] + 4/3*D*(1-theta)*ulast[2]
        b_element[-1] += (D*theta + (dr*D/2)/rspan[-2])*ur1
        u[n,1:-1] = solve_triangular(b_element, mid_element, up_element, down_element)
        u[n,0] = (4*u[n,1]-u[n,2])/3
    return u


def demo_heat_diffusion_radial():
    # https://folk.ntnu.no/leifh/teaching/tkt4140/._main068.html
    # dw/dt = w'' + w/r, w = w(r,t), 0 < r < 1
    # w_r(0,t)=0, w(1,t)=0
    # w(r,0)=1-r^2
    diffusion_coeff = 1
    num_t = 500
    num_r = 25
    r_length = 1
    t_length = 0.4
    tspan = np.linspace(0, t_length, num_t)
    rspan = np.linspace(0, r_length, num_r)
    theta = 0.8 #0 for FTCS, 1/2 for Crank-Nicolson, 1 for Laasonen
    ut0 = 1-rspan**2
    ur1 = 0

    dr = r_length/(num_r-1)
    dt = t_length/(num_t-1)
    numerical_diffusion_number = diffusion_coeff * dt / dr**2

    ret_ = _heat_diffusion_radial_hf_analytic(num_r, num_t, t_length)
    ret0 = _heat_diffusion_radial_hf_theta_scheme_v1(diffusion_coeff, theta, t_length, num_t, r_length, num_r, ut0, ur1)
    ret1 = _heat_diffusion_radial_hf_theta_scheme_v2(diffusion_coeff, theta, t_length, num_t, r_length, num_r, ut0, ur1)
    assert np.abs(ret0-ret1).max() < 1e-4

    xdata,ydata = np.meshgrid(rspan, tspan)
    fig,(ax0,ax1) = plt_subplots_3d(nrols=1, ncols=2, figsize=(10,5))
    ax0.plot_surface(xdata, ydata, ret_, rstride=1, cstride=1, cmap=matplotlib.cm.coolwarm, linewidth=0, antialiased=True)
    ax1.plot_surface(xdata, ydata, ret0, rstride=1, cstride=1, cmap=matplotlib.cm.coolwarm, linewidth=0, antialiased=True)
    for ax in [ax0,ax1]:
        ax.set_xlabel('r')
        ax.set_ylabel('t')
    ax0.set_title('analytical')
    ax1.set_title(f'theta={theta} scheme')


def demo_heat_diffusion_bc00():
    # u_t=D u_xx
    # u(x,0)=0
    # u(0,t)=0, u(1,t)=0
    diffusion_coeff = 1
    x_length = 10
    num_x = 50
    t_length = 0.05
    num_t = 500
    ux0 = 0 #must be 1 for analytical solution
    ux1 = 0 #must be 0 for analytical solution
    hf0 = lambda x: np.sin(np.pi*4*(x/x_length)**2) #ux0=ux1=0

    xspan = np.linspace(0, x_length, num_x)
    tspan = np.linspace(0, t_length, num_t)
    ut0 = hf0(xspan)

    Ak = scipy.fft.dst(ut0[1:-1], type=1)/(num_x-1)
    tmp0 = diffusion_coeff*(np.arange(1,num_x-1)*np.pi/x_length)**2
    tmp1 = Ak[:,np.newaxis]*np.exp(-tmp0[:,np.newaxis]*tspan)
    ret_analytical = sum([y[:,np.newaxis]*np.sin(x*np.pi*xspan/x_length) for x,y in enumerate(tmp1,start=1)])
    assert hfe(ret_analytical[0], ut0) < 1e-7

    ret_FTCS = _heat_diffusion_hf_FTCS(diffusion_coeff, x_length, num_x, t_length, num_t, ux0, ux1, ut0)

    xdata,ydata = np.meshgrid(xspan, tspan)
    fig,(ax0,ax1,ax2) = plt_subplots_3d(nrols=1, ncols=3, figsize=(10,4))
    ax0.plot_surface(xdata, ydata, ret_analytical, rstride=1, cstride=1, cmap=matplotlib.cm.coolwarm, linewidth=0, antialiased=True)
    ax1.plot_surface(xdata, ydata, ret_FTCS, rstride=1, cstride=1, cmap=matplotlib.cm.coolwarm, linewidth=0, antialiased=True)
    ax2.plot_surface(xdata, ydata, ret_analytical-ret_FTCS, rstride=1, cstride=1, cmap=matplotlib.cm.coolwarm, linewidth=0, antialiased=True)
    for ax,title in zip([ax0,ax1,ax2],['analytical','finite-difference', 'error']):
        ax.set_xlabel('x')
        ax.set_ylabel('t')
        ax.set_title(title)


def demo_parabolic_instability():
    # u_t=D u_xx
    # u(x,0)=0
    # u(0,t)=0, u(1,t)=0
    diffusion_coeff = 1
    x_length = 10
    num_x = 100
    t_length = 1
    num_t0 = 188
    num_t1 = 200
    ux0 = 0 #must be 1 for analytical solution
    ux1 = 0 #must be 0 for analytical solution
    hf0 = lambda x: np.sin(np.pi*4*(x/x_length)**2) #ux0=ux1=0

    xspan = np.linspace(0, x_length, num_x)
    ut0 = hf0(xspan)

    ret_FTCS0 = _heat_diffusion_hf_FTCS(diffusion_coeff, x_length, num_x, t_length, num_t0, ux0, ux1, ut0)
    ret_FTCS1 = _heat_diffusion_hf_FTCS(diffusion_coeff, x_length, num_x, t_length, num_t1, ux0, ux1, ut0)

    fig,(ax0,ax1) = plt_subplots_3d(nrols=1, ncols=2, figsize=(8,4))
    xdata,ydata = np.meshgrid(xspan, np.linspace(0, t_length, num_t0))
    ax0.plot_surface(xdata, ydata, ret_FTCS0, rstride=1, cstride=1, cmap=matplotlib.cm.coolwarm, linewidth=0, antialiased=True)
    xdata,ydata = np.meshgrid(xspan, np.linspace(0, t_length, num_t1))
    ax1.plot_surface(xdata, ydata, ret_FTCS1, rstride=1, cstride=1, cmap=matplotlib.cm.coolwarm, linewidth=0, antialiased=True)
    stable_factor0 = diffusion_coeff*(t_length/(num_t0-1))/(x_length/(num_x-1))**2
    stable_factor1 = diffusion_coeff*(t_length/(num_t1-1))/(x_length/(num_x-1))**2
    for ax,tmp0 in zip([ax0,ax1], [stable_factor0,stable_factor1]):
        ax.set_xlabel('x')
        ax.set_ylabel('t')
        ax.set_title(f'stable-factor: {tmp0:.5f}')
