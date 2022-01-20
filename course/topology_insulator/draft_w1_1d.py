# https://topocondmat.org/w1_topointro/1D.html
import numpy as np
import pfapack.pfaffian
import matplotlib
import matplotlib.pyplot as plt
plt.ion()

import kwant

tableau_colorblind = [x['color'] for x in plt.style.library['tableau-colorblind10']['axes.prop_cycle']]

from utils import pauli

def plt_animation_finite_chain(mus, energy, density0, density1):
    N0,N1 = density0.shape
    fig, (ax0,ax1) = plt.subplots(1, 2, figsize=(8,5))
    ax0.plot(mus, energy, color=tableau_colorblind[1])
    h0_vline = ax0.axvline(mus[0], color=tableau_colorblind[0], linestyle=':')
    ax0.set_ylim(-3,3)
    ax0.set_xlabel(r'$\mu/t$')
    ax0.set_ylabel('$E/t$')
    xdata1 = np.arange(N1)
    tmp0,_,tmp1 = np.sort(np.abs(energy[0]))[:3]
    h1_line0, = ax1.plot(xdata1, density0[0], label=f'E={tmp0:.3f}')
    h1_line1, = ax1.plot(xdata1, density1[0], label=f'E={tmp1:.3f}')
    h1_legend = ax1.legend()
    ax1.set_xlabel('x')
    ax1.set_ylabel('amplitude')
    ax1.set_xlim(0, N1-1)
    ax1.set_ylim(0, 1.5)

    def hf_frame(ind0):
        tmp0 = h0_vline.get_data()[1]
        h0_vline.set_data([mus[ind0],mus[ind0]], tmp0)
        h1_line0.set_data(xdata1, density0[ind0])
        h1_line1.set_data(xdata1, density1[ind0])
        tmp0,_,tmp1 = np.sort(np.abs(energy[ind0]))[:3]
        htext0,htext1 = h1_legend.get_texts()
        htext0.set_text(f'E={tmp0:.3f}')
        htext1.set_text(f'E={tmp1:.3f}')
        return h1_line0,h1_line1,htext0,htext1
    ani = matplotlib.animation.FuncAnimation(fig, hf_frame, frames=N0, interval=200)
    return ani


def plt_animation_infinite_chain(kx, mus, energy, e_dirac_cone, is_topological):
    fig, ax = plt.subplots()
    hline0, = ax.plot(kx, energy[0,:,0], color=tableau_colorblind[1], label='band')
    hline1, = ax.plot(kx, energy[0,:,1], color=tableau_colorblind[1])
    hline2, = ax.plot(kx, e_dirac_cone[0], linestyle=':', color=tableau_colorblind[0], label='dirac cone')
    hline3, = ax.plot(kx, -e_dirac_cone[0], linestyle=':', color=tableau_colorblind[0])
    ax.set_xlim(kx.min(), kx.max())
    ax.set_ylim(energy.min(), energy.max())
    ax.set_xlabel('kx')
    ax.legend(loc='upper right')
    title_str = '$\\mu/t={:.3f}$ {}'
    htitle = ax.set_title(title_str.format(mus[0], 'topological' if is_topological[0] else 'trivial'))

    def hf_frame(ind0):
        htitle.set_text(title_str.format(mus[ind0], 'topological' if is_topological[ind0] else 'trivial'))
        hline0.set_data(kx, energy[ind0,:,0])
        hline1.set_data(kx, energy[ind0,:,1])
        hline2.set_data(kx, e_dirac_cone[ind0])
        hline3.set_data(kx, -e_dirac_cone[ind0])
        return htitle,hline0,hline1,hline2,hline3
    ani = matplotlib.animation.FuncAnimation(fig, hf_frame, frames=len(e_dirac_cone), interval=200)
    return ani


def plt_animation_periodic_chain(lambda_, mus, energy):
    fig, ax = plt.subplots()
    hline_list = ax.plot(lambda_, energy[0], color=tableau_colorblind[1])
    ax.set_xlim(lambda_.min(), lambda_.max())
    ax.set_ylim(energy.min(), energy.max())
    ax.set_xlabel(r'$\lambda$')
    ax.set_ylabel(r'$E/t$')
    title_str = '$\\mu/t={:.3f}$'
    htitle = ax.set_title(title_str.format(mus[0]))

    def hf_frame(ind0):
        htitle.set_text(title_str.format(mus[ind0]))
        for hline_i,energy_i in zip(hline_list,energy[ind0].T):
            hline_i.set_data(lambda_,energy_i)
        return htitle,hline_list
    ani = matplotlib.animation.FuncAnimation(fig, hf_frame, frames=len(mus), interval=200)
    return ani

def calculate_BdG_pfaffian(ham):
    U = np.array([[1.0, 1.0], [1.0j, -1.0j]]) / np.sqrt(2)
    ret = np.sign(pfapack.pfaffian.pfaffian(1j * U @ ham @ U.T.conj()).real)
    return ret


lat_chain = kwant.lattice.chain()


def hf_onsite(site, mu):
    return -mu*pauli.sz
param_chain0 = {
    'length': 25,
    't': 1,
    'delta': 1,
}
dev_chain0 = kwant.Builder()
dev_chain0[(lat_chain(x) for x in range(param_chain0['length']))] = hf_onsite
dev_chain0[kwant.builder.HoppingKind((-1,), lat_chain, lat_chain)] = -param_chain0['t']*pauli.sz - 1j*param_chain0['delta']*pauli.sy
dev_chain2_f = dev_chain0.finalized()
mus = np.arange(0, 4, 0.2) + 1e-5 # At mu=0 the first excited state is not well-defined due to the massive degeneracy.
hamiltonians = np.stack([dev_chain2_f.hamiltonian_submatrix(params={'mu':x}) for x in mus], axis=0)
energy,EVC = np.linalg.eigh(hamiltonians)
ind0 = np.argsort(np.abs(energy), axis=1)[:,:4]
hf0 = lambda x: (np.abs(EVC[np.arange(EVC.shape[0]),:,x])**2).reshape(EVC.shape[0],-1,2).sum(axis=2)
density0 = hf0(ind0[:,0]) + hf0(ind0[:,1])
density1 = hf0(ind0[:,2]) + hf0(ind0[:,3])
ani = plt_animation_finite_chain(mus, energy, density0, density1)


# infinite 1D Kitaev chain
def hf_onsite(site, mu):
    return -mu * pauli.sz
param_chain1 = {
    't': 1,
    'delta': 1,
}
dev_chain1 = kwant.Builder(kwant.TranslationalSymmetry((1,)))
dev_chain1[lat_chain(0)] = hf_onsite
dev_chain1[kwant.HoppingKind((-1,), lat_chain)] = -param_chain1['t'] * pauli.sz - 1j * param_chain1['delta'] * pauli.sy
dev_chain1_f = kwant.wraparound.wraparound(dev_chain1).finalized()
mus = np.linspace(-3, 3, 25) + 1e-5 # mu=0, the first excited state is not well-defined due to the massive degeneracy.
kx = np.linspace(-np.pi, np.pi, 101)
energy = []
e_dirac_cone = []
pfaffian = []
for mu_i in mus:
    tmp0 = ({'mu':mu_i, 'k_x':x} for x in kx)
    energy.append(np.stack([np.linalg.eigvalsh(dev_chain1_f.hamiltonian_submatrix(params=x)) for x in tmp0], axis=0))
    tmp0 = [{'mu':mu_i, 'k_x':x} for x in [0,np.pi]]
    pfaffian.append([calculate_BdG_pfaffian(dev_chain1_f.hamiltonian_submatrix(params=x)) for x in tmp0])
    e_dirac_cone.append(np.sqrt((mu_i+2*param_chain1['t'])**2 + 4*(param_chain1['delta']*kx)**2))
energy = np.stack(energy) #(np,float64,(20,101,2))
e_dirac_cone = np.stack(e_dirac_cone) #(np,float64,(20,101))
pfaffian = np.array(pfaffian)
is_topological = (pfaffian[:,0]*pfaffian[:,1])<0
ani = plt_animation_infinite_chain(kx, mus, energy, e_dirac_cone, is_topological)


## circular chain
def hf_onsite(site, mu):
    return -mu*pauli.sz
def hf_hop1(site0, site1, lambda_):
    assert (site1.tag[0]-site0.tag[0]) % param_chain2['length'] == 1
    ret = -param_chain2['t']*pauli.sz - 1j*param_chain2['delta']*pauli.sy
    if site1.tag[0]==0:
        ret = ret*(1-2*lambda_)
    return ret
param_chain2 = {
    'length': 25,
    't': 1,
    'delta': 1,
}
dev_chain2 = kwant.Builder()
dev_chain2[(lat_chain(x) for x in range(param_chain2['length']))] = hf_onsite
dev_chain2[kwant.builder.HoppingKind((-1,), lat_chain, lat_chain)] = hf_hop1
dev_chain2[lat_chain(param_chain2['length']-1), lat_chain(0)] = hf_hop1
dev_chain0_f = dev_chain2.finalized()
mus = np.linspace(0, 4, 40)
lambda_ = np.linspace(0.0, 1.0, 101)
energy = []
for mu_i in mus:
    tmp0 = ({'mu':mu_i,'lambda_':x} for x in lambda_)
    energy.append(np.stack([np.linalg.eigvalsh(dev_chain0_f.hamiltonian_submatrix(params=x)) for x in tmp0], axis=0))
energy = np.stack(energy) #(np,float64,(40,101,50))
ani = plt_animation_periodic_chain(lambda_, mus, energy)
