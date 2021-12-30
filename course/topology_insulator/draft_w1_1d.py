# https://topocondmat.org/w1_topointro/1D.html
import numpy as np
import types
import pfapack.pfaffian
import matplotlib
import matplotlib.pyplot as plt
plt.ion()

import kwant

tableau_colorblind = [x['color'] for x in plt.style.library['tableau-colorblind10']['axes.prop_cycle']]


pauli = types.SimpleNamespace(
    s0=np.array([[1.0, 0.0], [0.0, 1.0]]),
    sx=np.array([[0.0, 1.0], [1.0, 0.0]]),
    sy=np.array([[0.0, -1j], [1j, 0.0]]),
    sz=np.array([[1.0, 0.0], [0.0, -1.0]]),
)

def plt_animation_finite_chain(xdata, ydata, density0, density1):
    # xdata = mus
    # ydata = energies
    # density0 = density0
    # density1 = density1
    N0,N1 = density0.shape
    fig, (ax0,ax1) = plt.subplots(1, 2, figsize=(8,5))
    ax0.plot(xdata, ydata, color=tableau_colorblind[1])
    h0_vline = ax0.axvline(xdata[0], color=tableau_colorblind[0], linestyle=':')
    ax0.set_ylim(-3,3)
    ax0.set_xlabel(r'$\mu/t$')
    ax0.set_ylabel('$E/t$')
    xdata1 = np.arange(N1)
    tmp0,_,tmp1 = np.sort(np.abs(ydata[0]))[:3]
    h1_line0, = ax1.plot(xdata1, density0[0], label=f'E={tmp0:.3f}')
    h1_line1, = ax1.plot(xdata1, density1[0], label=f'E={tmp1:.3f}')
    h1_legend = ax1.legend()
    ax1.set_xlabel('x')
    ax1.set_ylabel('amplitude')
    ax1.set_xlim(0, N1-1)
    ax1.set_ylim(0, 1.5)

    def hf_frame(ind0):
        tmp0 = h0_vline.get_data()[1]
        h0_vline.set_data([xdata[ind0],xdata[ind0]], tmp0)
        h1_line0.set_data(xdata1, density0[ind0])
        h1_line1.set_data(xdata1, density1[ind0])
        tmp0,_,tmp1 = np.sort(np.abs(ydata[ind0]))[:3]
        # h1_line0.set_label(f'E={tmp0:.3f}')
        # h1_line1.set_label(f'E={tmp1:.3f}')
        htext0,htext1 = h1_legend.get_texts()
        htext0.set_text(f'E={tmp0:.3f}')
        htext1.set_text(f'E={tmp1:.3f}')
        return h1_line0,h1_line1,htext0,htext1
    ani = matplotlib.animation.FuncAnimation(fig, hf_frame, frames=N0, interval=100)
    return ani #animation will stop if the variable ani is garbage-collected


def plt_animation_infinite_chain(kx, xdata, ydata0, ydata1, ydata2):
    fig, ax = plt.subplots()
    hline0,hline1 = ax.plot(kx, ydata0[0], color=tableau_colorblind[1])
    hline2, = ax.plot(kx, ydata1[0], linestyle=':', color=tableau_colorblind[0])
    hline3, = ax.plot(kx, -ydata1[0], linestyle=':', color=tableau_colorblind[0])
    ax.set_xlim(kx.min(), kx.max())
    ax.set_ylim(min(ydata0.min(),-ydata1.max()), min(ydata0.max(),ydata1.max()))
    ax.set_xlabel('kx')
    tmp0 = 'topological' if ydata2[0] else 'trivial'
    tmp1 = r'\mu'
    htitle = ax.set_title(f'${tmp1}/t={xdata[0]:.3f}$ {tmp0}')

    def hf_frame(ind0):
        tmp0 = 'topological' if ydata2[ind0] else 'trivial'
        tmp1 = r'\mu'
        htitle.set_text(f'${tmp1}/t={xdata[ind0]:.3f}$ {tmp0}')
        hline0.set_data(kx, ydata0[ind0,:,0])
        hline1.set_data(kx, ydata0[ind0,:,1])
        hline2.set_data(kx, ydata1[ind0])
        hline3.set_data(kx, -ydata1[ind0])
        return htitle,hline0,hline1,hline2,hline3
    ani = matplotlib.animation.FuncAnimation(fig, hf_frame, frames=len(ydata1), interval=100)
    return ani


def plt_animation_periodic_chain(lambda_, mus, energy):
    fig, ax = plt.subplots()
    hline_list = ax.plot(lambda_, energy[0], color=tableau_colorblind[1])
    ax.set_xlim(lambda_.min(), lambda_.max())
    ax.set_ylim(energy.min(), energy.max())
    ax.set_xlabel(r'$\lambda$')
    ax.set_ylabel(r'$E/t$')
    tmp0 = r'\mu'
    htitle = ax.set_title(f'${tmp0}/t={mus[0]:.3f}$')

    def hf_frame(ind0):
        tmp0 = r'\mu'
        htitle.set_text(f'${tmp0}/t={mus[ind0]:.3f}$')
        for hline_i,energy_i in zip(hline_list,energy[ind0].T):
            hline_i.set_data(lambda_,energy_i)
        return htitle,hline_list
    ani = matplotlib.animation.FuncAnimation(fig, hf_frame, frames=len(mus), interval=100)
    return ani


lattice_1d = kwant.lattice.chain(norbs=2)


def onsite(onsite, mu):
    return -mu * pauli.sz
def hop(site1, site2, t, delta):
    return -t * pauli.sz - 1j * delta * pauli.sy
kitaev_chain_infinite = kwant.Builder(kwant.TranslationalSymmetry((-1,)))
kitaev_chain_infinite[lattice_1d(0)] = onsite
kitaev_chain_infinite[kwant.HoppingKind((1,), lattice_1d)] = hop
# kitaev_chain_infinite[lattice_1d.neighbors(n=1)] = hop
chain_length  =25
finite_chain = kwant.Builder()
finite_chain.fill(kitaev_chain_infinite, shape=(lambda site: 0 <= site.pos[0] < chain_length), start=[0])

# At mu=0 the first excited state is not well-defined due to the massive degeneracy.
mus = np.arange(0, 4, 0.2) + 1e-5
finite_chain_f = finite_chain.finalized()
tmp0 = ({'mu':x,'t':1,'delta':1} for x in mus)
hamiltonians = np.stack([finite_chain_f.hamiltonian_submatrix(params=x) for x in tmp0], axis=0)
energies,EVC = np.linalg.eigh(hamiltonians)
ind0 = np.argsort(np.abs(energies), axis=1)[:,:4]
hf0 = lambda x: (np.abs(EVC[np.arange(EVC.shape[0]),:,x])**2).reshape(EVC.shape[0],-1,2).sum(axis=2)
density0 = hf0(ind0[:,0]) + hf0(ind0[:,1])
density1 = hf0(ind0[:,2]) + hf0(ind0[:,3])
ani = plt_animation_finite_chain(mus, energies, density0, density1)



def find_pfaffian(H):
    U = np.array([[1.0, 1.0], [1.0j, -1.0j]]) / np.sqrt(2)
    return np.sign(np.real(pfapack.pfaffian.pfaffian(1j * U @ H @ U.T.conj())))
kx = np.linspace(-np.pi, np.pi, 101)
kitaev_chain_infinite_f = kwant.wraparound.wraparound(kitaev_chain_infinite).finalized()
energy = []
e_dirac_cone = []
param = {'t':1, 'delta':1}
pfaffian = []
for mu_i in mus:
    tmp0 = ({'t':param['t'], 'delta':param['delta'], 'mu':mu_i, 'k_x':x} for x in kx)
    tmp1 = np.stack([kitaev_chain_infinite_f.hamiltonian_submatrix(params=x) for x in tmp0], axis=0)
    energy.append(np.linalg.eigvalsh(tmp1))

    tmp0 = [{'t':param['t'], 'delta':param['delta'], 'mu':mu_i, 'k_x':x} for x in [0,np.pi]]
    pfaffian.append([find_pfaffian(kitaev_chain_infinite_f.hamiltonian_submatrix(params=x)) for x in tmp0])

    tmp0 = np.sqrt((mu_i+2*param['t'])**2 + 4*(param['delta']*kx)**2)
    e_dirac_cone.append(tmp0)
energy = np.stack(energy) #(np,float64,(20,101,2))
e_dirac_cone = np.stack(e_dirac_cone) #(np,float64,(20,101))
pfaffian = np.array(pfaffian)
is_topological = (pfaffian[:,0]*pfaffian[:,1])<0
ani = plt_animation_infinite_chain(kx, mus, energy, e_dirac_cone, is_topological)


periodic_chain = kwant.Builder()
periodic_chain.update(finite_chain)
# Connect the last site to the first:
def last_hop(site1, site2, t, delta, lambda_):
    return hop(site1, site2, t=t, delta=delta) * (1 - 2 * lambda_)
periodic_chain[lattice_1d(0), lattice_1d(chain_length-1)] = last_hop
params = dict(t=1, delta=1, lambda_=np.linspace(0.0, 1.0, 101))
mus = np.linspace(0, 4, 40)
lambda_=np.linspace(0.0, 1.0, 101)

periodic_chain_f = periodic_chain.finalized()
energy = []
for mu_i in mus:
    tmp0 = ({'t':param['t'], 'delta':param['delta'], 'mu':mu_i, 'lambda_':x} for x in lambda_)
    tmp1 = np.stack([periodic_chain_f.hamiltonian_submatrix(params=x) for x in tmp0], axis=0)
    energy.append(np.linalg.eigvalsh(tmp1))
energy = np.stack(energy) #(np,float64,(40,101,50))
ani = plt_animation_periodic_chain(lambda_, mus, energy)
