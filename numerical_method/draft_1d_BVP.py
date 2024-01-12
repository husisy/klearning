import numpy as np
import scipy.linalg
import scipy.special
import matplotlib.pyplot as plt
plt.ion()

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


def solve_triangular(npb, mid_element, up_element, down_element):
    ab = np.block([[np.array([0]), up_element], [mid_element], [down_element, np.array([0])]])
    ret = scipy.linalg.solve_banded((1,1), ab, npb)
    return ret


def demo_BVP_couette_flow_posieulle():
    # y'' = -p
    # y(0)=0, y(1)=1
    # https://folk.ntnu.no/leifh/teaching/tkt4140/._main029.html
    L = 1.0
    x1 = 1
    y1 = 1 #boundary value at y = L
    num_point = 100
    p_list = [-5.0, -2.5, -1.0, 0.0, 1.0, 2.5, 5.0]
    ret_x = np.linspace(0, x1, num_point)
    hf_analytical = lambda x,p: x*(1 + p*(1-x)/2)

    fig,ax = plt.subplots()
    for p in p_list:
        hf0 = lambda x,y: np.array([y[1], -p], dtype=y.dtype)
        s_guess = [1, 1.5]
        phi = [
            pde_runge_kutta4(hf0, ret_x, np.array([0,s_guess[0]]))[-1,0] - y1,
            pde_runge_kutta4(hf0, ret_x, np.array([0,s_guess[1]]))[-1,0] - y1,
        ]
        s_star = (s_guess[0]*phi[1]-s_guess[1]*phi[0])/(phi[1]-phi[0])
        ret_y = pde_runge_kutta4(hf0, ret_x, np.array([0,s_star]))
        ax.plot(ret_x, hf_analytical(ret_x, p), 'x')
        ax.plot(ret_x, ret_y[:,0], '-.', label=f'rk4: p={p}')
    ax.legend()


def demo_beam_deflect_shoot_constant():
    # y'' + theta^2*y - theta^2*(1-x^2)/2 = 0
    # y(-1)=0, y(1)=0
    # https://folk.ntnu.no/leifh/teaching/tkt4140/._main030.html
    num_point = 20
    x0 = -1
    x1 = 1
    theta = 1 # PL**2/EI
    ret_x = np.linspace(x0, x1, num_point)

    ret_ = (1/theta**2)*(np.cos(theta*ret_x)/np.cos(theta) - 1)-(1 - ret_x**2)/2 # analytical solution
    hf0 = lambda x,y: np.array([y[1],-(theta**2)*(y[0]+0.5*(1-x**2))], dtype=y.dtype)
    hf1 = lambda x,y: np.array([y[1], -(theta**2)*y[0]], dtype=y.dtype)
    u0 = pde_runge_kutta4(hf0, ret_x, np.array([0,0]))[:,0]
    u1 = pde_runge_kutta4(hf1, ret_x, np.array([0,1]))[:,0]
    ret0 = u0 -(u0[-1]/u1[-1])*u1 # interpolate to find correct solution

    fig,ax = plt.subplots()
    ax.plot(ret_x, ret0, 'y', label='shooting technique')
    ax.plot(ret_x, ret_, 'r:', label='analytical solution')
    ax.legend()

def demo_beam_deflect_shoot_varying():
    # y'' + (1+x^n)*y + 1 = 0
    # y'(0)=0, y(1)=0
    # https://folk.ntnu.no/leifh/teaching/tkt4140/._main031.html
    para_n = 2
    ret_x = np.linspace(0, 1, 100)
    hf0 = lambda x,y: np.array([y[1], -1-(1+x**para_n)*y[0]], dtype=y.dtype)
    s_guess = [0,1]
    u0 = pde_runge_kutta4(hf0, ret_x, np.array([s_guess[0],0]))[-1,0]
    u1 = pde_runge_kutta4(hf0, ret_x, np.array([s_guess[1],0]))[-1,0]
    s_star = (u0*s_guess[1]-u1*s_guess[0])/(u0-u1)
    ret_y = pde_runge_kutta4(hf0, ret_x, np.array([s_star,0]))

    fig,ax = plt.subplots()
    ax.plot(ret_x, ret_y[:,0], label='RK4')


def demo_BVP_nonlinear():
    # y''=3/2*y^2
    # y(0)=4, y(1)=1
    # https://folk.ntnu.no/leifh/teaching/tkt4140/._main032.html
    bc_y1 = 1
    ret_x = np.linspace(0, 1, 100)
    hf0 = lambda x,y: np.array([y[1], 3/2*y[0]**2], dtype=y.dtype)
    hf_analytical = lambda x: 4/(1+x)**2

    # s_guess0,s_guess1 = -3,-9 #converge at s=-8
    s_guess0,s_guess1 = -40,-10 #converge at s=-35.86

    phi0 = pde_runge_kutta4(hf0, ret_x, [4,s_guess0])[-1,0] - bc_y1
    for ind0 in range(10):
        ret0 = pde_runge_kutta4(hf0, ret_x, [4,s_guess1])
        phi1 = ret0[-1,0] - bc_y1
        if abs(phi1-phi0) < 1e-7:
            break
        s_guess0, phi0, s_guess1 = s_guess1, phi1, (phi0*s_guess1 - phi1*s_guess0)/(phi0-phi1)
        if abs(s_guess0-s_guess1) < 1e-7:
            break

    fig,ax = plt.subplots()
    ax.plot(ret_x, ret0[:,0], label='RK4')
    ax.plot(ret_x, hf_analytical(ret_x), label='analytical')
    ax.legend()


def demo_BVP_nonlinear_linearization():
    # y''=3/2*y^2
    # y(0)=4, y(1)=1
    # https://folk.ntnu.no/leifh/teaching/tkt4140/._main044.html
    x0 = 0
    x1 = 1
    y0 = 4
    y1 = 1
    num_point = 100
    ret_x = np.linspace(x0, x1, num_point)
    delta_x = (x1-x0)/(num_point-1)
    max_iteration = 30
    hf_analytical = lambda x: 4/(1+x)**2
    ret_ = hf_analytical(ret_x)

    # picard linearization
    b_element = np.zeros(num_point-2)
    b_element[0] = -y0
    b_element[-1] = -y1
    up_element = np.ones(num_point-3)
    down_element = up_element
    yiter = np.linspace(y0, y1, num_point)[1:-1]
    for _ in range(max_iteration): #8 iterations
        yiter_last = yiter
        mid_element = -2*np.ones(num_point-2) - (3/2*delta_x**2)*yiter
        yiter = solve_triangular(b_element, mid_element, up_element, down_element)
        if np.abs(yiter_last-yiter).max()<1e-5:
            break
    ret0 = np.concatenate([[y0],yiter,[y1]])

    # Newton linearization
    up_element = np.ones(num_point-3)
    down_element = up_element
    yiter = np.linspace(y0, y1, num_point)[1:-1]
    for _ in range(max_iteration): #3 iterations
        yiter_last = yiter
        mid_element = -2*np.ones(num_point-2) - (3*delta_x**2)*yiter
        b_element = -(3/2*delta_x**2)*yiter**2
        b_element[0] -= y0
        b_element[-1] -= y1
        yiter = solve_triangular(b_element, mid_element, up_element, down_element)
        if np.abs(yiter_last-yiter).max()<1e-5:
            break
    ret1 = np.concatenate([[y0],yiter,[y1]])

    fig,ax = plt.subplots()
    ax.plot(ret_x, ret_, 'x', label='analytical')
    ax.plot(ret_x, ret0, label='Picard-linearization')
    ax.plot(ret_x, ret1, label='Newton-linearization')
    ax.legend()


def demo_BVP_finite_difference_method():
    # y''-beta^2*y=0
    # y(x0)=y0, y(x1)=y1
    # https://folk.ntnu.no/leifh/teaching/tkt4140/._main041.html
    x0 = -1
    x1 = 1
    y0 = 2
    y1 = 4
    para_beta = 5
    num_point = 100
    ret_x = np.linspace(x0, x1, num_point)
    delta_x = (x1-x0)/(num_point-1)

    mid_element = np.ones(num_point-2)*(-2-(para_beta*delta_x)**2)
    up_element = np.ones(num_point-3)
    b_element = np.zeros(num_point-2)
    b_element[0] = -y0
    b_element[-1] = -y1
    tmp0 = solve_triangular(b_element, mid_element, up_element, up_element)
    ret0 = np.concatenate([[y0],tmp0,[y1]])

    tmp0 = np.array([[np.sinh(para_beta*x0), np.cosh(para_beta*x0)], [np.sinh(para_beta*x1), np.cosh(para_beta*x1)]])
    coeff0,coeff1 = np.linalg.solve(tmp0, np.array([y0,y1]))
    hf_analytical = lambda x: coeff0*np.sinh(para_beta*x) + coeff1*np.cosh(para_beta*x)
    ret_ = hf_analytical(ret_x)

    fig,ax = plt.subplots()
    ax.plot(ret_x, ret0, label='sparse')
    ax.plot(ret_x, ret_, ':', label='analytical')
    ax.legend()
    ax.grid()


def demo_BVP_finite_difference_method_mixed_BC():
    # y''-beta^2*y=0
    # y'(x0)=dy0, y(x1)=y1
    # https://folk.ntnu.no/leifh/teaching/tkt4140/._main041.html
    para_beta = 3
    x0 = -1
    x1 = 1
    dy0 = -2
    y1 = 2
    num_point = 100
    ret_x = np.linspace(x0, x1, num_point)

    def hf_numerical(num_point):
        delta_x = (x1-x0)/(num_point-1)
        mid_element = np.ones(num_point-1)*(-2-(para_beta*delta_x)**2)
        mid_element[0] = -2
        up_element = np.ones(num_point-2)
        up_element[0] = 2-(para_beta*delta_x)**2
        down_element = np.ones(num_point-2)
        b_element = np.zeros(num_point-1)
        b_element[0] = 2*delta_x*dy0
        b_element[-1] = -y1
        tmp0 = solve_triangular(b_element, mid_element, up_element, down_element)
        ret = np.concatenate([tmp0,[y1]])
        return ret

    ret0 = hf_numerical(num_point)
    tmp0 = np.array([[para_beta*np.cosh(para_beta*x0), para_beta*np.sinh(para_beta*x0)], [np.sinh(para_beta*x1), np.cosh(para_beta*x1)]])
    coeff0,coeff1 = np.linalg.solve(tmp0, np.array([dy0,y1]))
    hf_analytical = lambda x: coeff0*np.sinh(para_beta*x) + coeff1*np.cosh(para_beta*x)
    ret_ = hf_analytical(ret_x)

    fig,ax = plt.subplots()
    ax.plot(ret_x, ret0, label='sparse')
    ax.plot(ret_x, ret_, ':', label='analytical')
    ax.legend()
    ax.grid()

    num_point_list = 5*2**np.arange(3, 9, dtype=np.int64) + 1
    error_list = []
    for num_point in num_point_list:
        ret_x = np.linspace(x0, x1, num_point)
        ret0 = hf_numerical(num_point)
        ret_ = hf_analytical(ret_x)
        error_list.append(np.sqrt(np.sum(((ret_-ret0)/ret_)**2)))
    error_list = np.array(error_list)
    delta_x_list = (x1-x0)/(num_point_list-1)
    convergance_order = np.polyfit(np.log(delta_x_list), np.log(error_list), 1)[0]
    print(f'convergance order: {convergance_order}')
