# elliptic pde, BVP
import numpy as np
import scipy.linalg
import scipy.sparse
import scipy.sparse.linalg
import matplotlib
import matplotlib.pyplot as plt
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

def _elliptic_dirichletBVP_analytical(num_x, num_y, uy1, order=10):
    print('[WARNING] analytical results is WRONG')
    x = np.linspace(0, 1, num_x)
    y = np.linspace(0, 1, num_y)
    n = np.arange(1, order)
    pin = np.pi*n
    An = (4/(pin*np.sinh(3/2*pin))).reshape(-1,1)
    ret = []
    for ind0 in range(num_x):
        xi = x[ind0]
        tmp0 = An*(np.sin(pin*xi)).reshape(-1,1)
        ret.append(uy1*np.sum(tmp0 * np.sinh(pin[:,np.newaxis]*y), axis=0))
    ret = np.stack(ret)
    return ret

def demo_elliptic_dirichletBVP():
    # https://folk.ntnu.no/leifh/teaching/tkt4140/._main055.html
    x0 = 0
    x1 = 1
    y0 = 0
    y1 = 1
    num_x = 100
    num_y = 100
    ux0 = np.zeros(num_y)
    ux1 = np.zeros(num_y)
    uy0 = np.zeros(num_x)
    uy1 = np.ones(num_x)

    # xdata,ydata = np.meshgrid(np.linspace(x0,x1,num_x), np.linspace(y0,y1,num_y))
    # tmp0 = (np.sin(4*np.pi*xdata+0.5) * np.cos(3*np.pi*ydata)).T
    # ux0 = tmp0[0]
    # ux1 = tmp0[-1]
    # uy0 = tmp0[:,0]
    # uy1 = tmp0[:,-1]

    # delta_x = (x1-x0)/(num_x-1)
    # delta_y = (y1-y0)/(num_y-1)
    # assert abs(delta_x-delta_y) < 1e-5 #TODO

    N0 = (num_x-2)*(num_y-2)
    matA = scipy.sparse.lil_matrix((N0,N0), dtype=np.float64)
    matA.setdiag(-4)
    tmp0 = np.arange(N0).reshape(num_x-2, num_y-2)
    matA[tmp0[:-1].reshape(-1), tmp0[1:].reshape(-1)] = 1
    matA[tmp0[1:].reshape(-1), tmp0[:-1].reshape(-1)] = 1
    matA[tmp0[:,:-1].reshape(-1), tmp0[:,1:].reshape(-1)] = 1
    matA[tmp0[:,1:].reshape(-1), tmp0[:,:-1].reshape(-1)] = 1
    matA = matA.tocsr()
    matB = np.zeros(N0, dtype=np.float64)
    matB[tmp0[:,0]] -= uy0[1:-1]
    matB[tmp0[:,-1]] -= uy1[1:-1]
    matB[tmp0[0]] -= ux0[1:-1]
    matB[tmp0[-1]] -= ux1[1:-1]
    ret0 = np.zeros((num_x,num_y), dtype=np.float64)
    ret0[0] = ux0
    ret0[-1] = ux1
    ret0[:,0] = uy0
    ret0[:,-1] = uy1
    ret0[1:-1,1:-1] = scipy.sparse.linalg.spsolve(matA, matB).reshape(num_x-2,num_y-2)

    ret_ = _elliptic_dirichletBVP_analytical(num_x, num_y, uy1[0], order=10) #TODO wrong results

    xdata,ydata = np.meshgrid(np.linspace(x0,x1,num_x), np.linspace(y0,y1,num_y))
    fig,(ax0,ax1) = plt_subplots_3d(nrols=1, ncols=2, figsize=(10,5))
    ax0.plot_surface(xdata, ydata, ret0.T, rstride=1, cstride=1, cmap=matplotlib.cm.coolwarm, linewidth=0, antialiased=True)
    ax1.plot_surface(xdata, ydata, ret_.T, rstride=1, cstride=1, cmap=matplotlib.cm.coolwarm, linewidth=0, antialiased=True)
    for ax in [ax0,ax1]:
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('T')
    ax0.set_title('finite difference')
    ax1.set_title('analytical')


def _elliptic_robinBVP_analytical(num_x, num_y, order=10):
    print('[WARNING] analytical results is WRONG')
    x = np.linspace(0, 1, num_x)
    y = np.linspace(0, 1, num_y)
    n = np.arange(1, order)
    pin = (n-1/2)*np.pi
    An = (2*((n+1)%2) / (pin*np.cosh(pin))).reshape(-1,1)
    ret = []
    for ind0 in range(num_x):
        xi = x[ind0]
        tmp0 = An*(np.cos(pin*xi)).reshape(-1,1)
        ret.append(np.sum(tmp0 * np.cosh(pin[:,np.newaxis]*y), axis=0))
    ret = np.stack(ret)
    return ret


def demo_elliptic_robinBVP():
    # https://folk.ntnu.no/leifh/teaching/tkt4140/._main056.html
    x0 = 0
    x1 = 1
    y0 = 0
    y1 = 1
    num_x = 100
    num_y = 100
    ux1 = np.zeros(num_y)
    uy1 = np.ones(num_x)

    N0 = (num_x-1)*(num_y-1)
    matA = scipy.sparse.lil_matrix((N0,N0), dtype=np.float64)
    matA.setdiag(-4)
    tmp0 = np.arange(N0).reshape(num_x-1, num_y-1)
    matA[tmp0[:-1].reshape(-1), tmp0[1:].reshape(-1)] = 1
    matA[tmp0[1:].reshape(-1), tmp0[:-1].reshape(-1)] = 1
    matA[tmp0[:,:-1].reshape(-1), tmp0[:,1:].reshape(-1)] = 1
    matA[tmp0[:,1:].reshape(-1), tmp0[:,:-1].reshape(-1)] = 1
    matA[tmp0[:,0],tmp0[:,1]] = 2
    matA[tmp0[0],tmp0[1]] = 2
    matA = matA.tocsr()
    matB = np.zeros(N0, dtype=np.float64)
    matB[tmp0[:,-1]] -= uy1[:-1]
    matB[tmp0[-1]] -= ux1[:-1]
    ret0 = np.zeros((num_x,num_y), dtype=np.float64)
    ret0[-1] = ux1
    ret0[:,-1] = uy1
    ret0[:-1,:-1] = scipy.sparse.linalg.spsolve(matA, matB).reshape(num_x-1,num_y-1)

    ret_ = _elliptic_robinBVP_analytical(num_x, num_y, order=20) #TODO wrong

    xdata,ydata = np.meshgrid(np.linspace(x0,x1,num_x), np.linspace(x0,x1,num_x))
    fig,(ax0,ax1) = plt_subplots_3d(nrols=1, ncols=2, figsize=(10,5))
    ax0.plot_surface(xdata, ydata, ret0.T, rstride=1, cstride=1, cmap=matplotlib.cm.coolwarm, linewidth=0, antialiased=True)
    ax1.plot_surface(xdata, ydata, ret_.T, rstride=1, cstride=1, cmap=matplotlib.cm.coolwarm, linewidth=0, antialiased=True)
    for ax in [ax0,ax1]:
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('T')
    ax0.set_title('finite difference')
    ax1.set_title('analytical')


def demo_nonlinear_elliptic_dirichletBVP():
    # u_xx + u_yy + u^2 + 1 = 0
    # https://folk.ntnu.no/leifh/teaching/tkt4140/._main057.html
    x0 = 0
    x1 = 1
    y0 = 0
    y1 = 1
    num_x = 100
    num_y = 100
    ux0 = np.zeros(num_y)
    ux1 = np.zeros(num_y)
    uy0 = np.zeros(num_x)
    uy1 = np.zeros(num_x)
    max_iteration = 100

    xdata,ydata = np.meshgrid(np.linspace(x0,x1,num_x), np.linspace(y0,y1,num_y))
    tmp0 = (np.sin(4*np.pi*xdata+0.5) * np.cos(3*np.pi*ydata)).T
    ux0 = tmp0[0]
    ux1 = tmp0[-1]
    uy0 = tmp0[:,0]
    uy1 = tmp0[:,-1]

    delta_x = (x1-x0)/(num_x-1)
    delta_y = (y1-y0)/(num_y-1)

    N0 = (num_x-2)*(num_y-2)
    dy2_dx2 = (delta_y/delta_x)**2
    matA = scipy.sparse.lil_matrix((N0,N0), dtype=np.float64)
    matA.setdiag(-2-2*dy2_dx2)
    tmp0 = np.arange(N0).reshape(num_x-2, num_y-2)
    matA[tmp0[:-1].reshape(-1), tmp0[1:].reshape(-1)] = dy2_dx2
    matA[tmp0[1:].reshape(-1), tmp0[:-1].reshape(-1)] = dy2_dx2
    matA[tmp0[:,:-1].reshape(-1), tmp0[:,1:].reshape(-1)] = 1
    matA[tmp0[:,1:].reshape(-1), tmp0[:,:-1].reshape(-1)] = 1
    matA = matA.tocsr()
    matB0 = np.zeros(N0, dtype=np.float64)
    matB0[tmp0[:,0]] -= uy0[1:-1]
    matB0[tmp0[:,-1]] -= uy1[1:-1]
    matB0[tmp0[0]] -= ux0[1:-1]
    matB0[tmp0[-1]] -= ux1[1:-1]

    initial_guess = (ux0.mean() + ux1.mean() + uy0.mean() + uy1.mean())/4
    uiter = np.ones((num_x-2)*(num_y-2), dtype=np.float64)*initial_guess
    for ind_iteration in range(max_iteration):
        matB = (-uiter**2-1)*delta_y**2+matB0
        uiter_last = uiter
        uiter = scipy.sparse.linalg.spsolve(matA, matB)
        if (ind_iteration>5) and (np.abs(uiter-uiter_last).max() < 1e-4):
            break
    ret0 = np.zeros((num_x,num_y), dtype=np.float64)
    ret0[0] = ux0
    ret0[-1] = ux1
    ret0[:,0] = uy0
    ret0[:,-1] = uy1
    ret0[1:-1,1:-1] = uiter.reshape(num_x-2,num_y-2)

    fig = plt.figure()
    ax = mpl_toolkits.mplot3d.Axes3D(fig, auto_add_to_figure=False)
    fig.add_axes(ax)
    xdata,ydata = np.meshgrid(np.linspace(x0,x1,num_x), np.linspace(y0,y1,num_y))
    ax.plot_surface(xdata, ydata, ret0.T, rstride=1, cstride=1, cmap=matplotlib.cm.coolwarm, linewidth=0, antialiased=True)
