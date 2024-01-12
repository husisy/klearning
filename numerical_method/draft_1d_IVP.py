import numpy as np
import scipy.special
import matplotlib.pyplot as plt
plt.ion()

def pde_euler_forward(hf0, xarray, y0):
    num_point = len(xarray)
    y0 = np.asarray(y0)
    ret_y = np.zeros((num_point,)+y0.shape, dtype=np.float64)
    ret_y[0] = y0
    for i in range(1,num_point):
        xi = xarray[i-1]
        yi = ret_y[i-1]
        h = xarray[i]-xi
        ret_y[i] = yi + h*hf0(xi, yi)
    return ret_y


def pde_heun_method(hf0, xarray, y0):
    num_point = len(xarray)
    y0 = np.asarray(y0)
    ret_y = np.zeros((num_point,)+y0.shape, dtype=np.float64)
    ret_y[0] = y0
    for i in range(1,num_point):
        xi = xarray[i-1]
        xi1 = xarray[i]
        h = xi1-xi
        yi = ret_y[i-1]
        k0 = hf0(xi, yi)
        k1 = hf0(xi1, yi + h*k0)
        ret_y[i] = yi + h/2 * (k0 + k1)
    return ret_y


def pde_runge_kutta4(hf0, xarray, y0):
    num_point = len(xarray)
    y0 = np.asarray(y0)
    ret_y = np.zeros((num_point,)+y0.shape, dtype=np.float64)
    ret_y[0] = y0
    for i in range(1,num_point):
        xi = xarray[i-1]
        xi1 = xarray[i]
        h = xi1-xi
        yi = ret_y[i-1]
        k0 = hf0(xi, yi)
        k1 = hf0(xi+h/2, yi + h/2*k0)
        k2 = hf0(xi+h/2, yi + h/2*k1)
        k3 = hf0(xi+h, yi + h*k2)
        ret_y[i] = yi + h/6*(k0+2*k1+2*k2+k3)
    return ret_y


def plot_results(xdata, ydata_dict):
    fig,ax = plt.subplots()
    for key,ydata in ydata_dict.items():
        linestyle = '-' if key=='analytical' else '--'
        ax.plot(xdata, ydata, linestyle=linestyle, label=key)
    ax.legend()


def demo00():
    # y' = y
    x0 = 0
    y0 = 1
    x1 = 1
    num_point = 100
    hf0 = lambda x,y: y

    ret_x = np.linspace(x0, x1, num_point)
    ret_ = np.exp(ret_x)
    ret0 = pde_euler_forward(hf0, ret_x, y0)
    ret1 = pde_heun_method(hf0, ret_x, y0)
    ret2 = pde_runge_kutta4(hf0, ret_x, y0)
    plot_results(ret_x, {'analytical':ret_, 'Euler':ret0, 'Heun':ret1, 'RK4':ret2})


def demo01():
    # y''+y=0
    x0 = 0
    y0 = np.array([0.1, 0])
    x1 = 2*np.pi
    num_point = 100
    hf0 = lambda x,y: np.array([y[1], -y[0]])

    ret_x = np.linspace(x0, x1, num_point)
    ret_ = np.cos(ret_x) * y0[0]
    ret0 = pde_euler_forward(hf0, ret_x, y0)
    ret1 = pde_heun_method(hf0, ret_x, y0)
    ret2 = pde_runge_kutta4(hf0, ret_x, y0)
    plot_results(ret_x, {'analytical':ret_, 'Euler':ret0[:,0], 'Heun':ret1[:,0], 'RK4':ret2[:,0]})


def demo02():
    # Newton's first differential equation https://folk.ntnu.no/leifh/teaching/tkt4140/._main016.html
    x0 = 0
    y0 = 0
    x1 = 2
    num_point = 100
    hf0 = lambda x,y: 1 - 3*x + y + x**2 + x*y

    ret_x = np.linspace(x0, x1, num_point)
    tmp0 = np.exp(ret_x + ret_x**2/2)
    tmp1 = scipy.special.erf(np.sqrt(2)/2*(1+ret_x)) - scipy.special.erf(np.sqrt(2)/2)
    ret_ = 3*np.sqrt(2*np.pi*np.e)*tmp0*tmp1 + 4*(1-tmp0) - ret_x
    ret0 = pde_euler_forward(hf0, ret_x, y0)
    ret1 = pde_heun_method(hf0, ret_x, y0)
    ret2 = pde_runge_kutta4(hf0, ret_x, y0)
    plot_results(ret_x, {'analytical':ret_, 'Euler':ret0, 'Heun':ret1, 'RK4':ret2})


def demo03():
    # solitary wave
    x0 = 0
    y0 = np.array([1, 0], dtype=np.float64)
    x1 = 2
    num_point = 100
    hf0 = lambda x,y: np.array([y[1],2*y[0]*(1-3/2*y[0])], dtype=y.dtype)

    ret_x = np.linspace(x0, x1, num_point)
    ret_ = 2/(1+np.cosh(ret_x*np.sqrt(2)))
    ret0 = pde_euler_forward(hf0, ret_x, y0)
    ret1 = pde_heun_method(hf0, ret_x, y0)
    ret2 = pde_runge_kutta4(hf0, ret_x, y0)
    plot_results(ret_x, {'analytical':ret_, 'Euler':ret0[:,0], 'Heun':ret1[:,0], 'RK4':ret2[:,0]})


def demo_order():
    hf0 = lambda x,y: x**(-2) - y/x - y**2
    x0 = 1
    y0 = -1
    x1 = 5
    hf_analytical = lambda x: -1/x
    ode_method = {
        'euler': pde_euler_forward,
        'heun': pde_heun_method,
        'rk4': pde_runge_kutta4,
    }

    for scheme_name,hf_scheme in ode_method.items():
        ret = []
        for N in [40*2**x for x in range(6)]:
            xspan = np.linspace(x0, x1, N)
            ret.append(hf_scheme(hf0, xspan, y0)[-1])
        err_list = np.abs(np.array(ret)-hf_analytical(x1))
        order = -np.polyfit(np.arange(len(err_list)), np.log2(err_list), 1)[0]
        print(f'[{scheme_name}] order={order}')

    for scheme_name,hf_scheme in ode_method.items():
        ret = []
        for N in [40*2**x for x in range(6)]:
            xspan = np.linspace(x0, x1, N)
            ret.append(hf_scheme(hf0, xspan, y0)[-1])
        tmp0 = np.log2(np.array(ret[:-1])-np.array(ret[1:]))
        order = -np.polyfit(np.arange(len(ret)-1), tmp0, 1)[0]
        print(f'[{scheme_name}] order={order}')
