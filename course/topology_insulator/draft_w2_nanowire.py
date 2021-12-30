# https://topocondmat.org/w1_topointro/1D.html
import numpy as np
import itertools
import matplotlib
import matplotlib.pyplot as plt
from tqdm import tqdm
plt.ion()

import kwant

from utils import pauli

tableau_colorblind = [x['color'] for x in plt.style.library['tableau-colorblind10']['axes.prop_cycle']]


lat = kwant.lattice.chain(norbs=4)


def plt_animation_band(kx, p_list, energy, name=''):
    fig,ax = plt.subplots()
    hline_list = ax.plot(kx, energy[0])
    htitle = ax.set_title(f'{name}={p_list[0]:.3f}')
    def hf_frame(ind0):
        for hline_i,energy_i in zip(hline_list,energy[ind0].T):
            hline_i.set_data(kx, energy_i)
        htitle.set_text(f'{name}={p_list[ind0]:.3f}')
        return hline_list,htitle
    ani = matplotlib.animation.FuncAnimation(fig, hf_frame, frames=len(p_list), interval=200)
    return ani


def onsite(site, t, mu, B):
    return (2 * t - mu) * pauli.szs0 + B * pauli.szsz
def hop(site1, site2, t, delta):
    return -t * pauli.szs0 - 1j * delta * pauli.sys0
spinful_kitaev_chain = kwant.Builder(kwant.TranslationalSymmetry([1]))
spinful_kitaev_chain[lat(0)] = onsite
spinful_kitaev_chain[kwant.HoppingKind((1,), lat)] = hop
spinful_kitaev_chain_f = kwant.wraparound.wraparound(spinful_kitaev_chain).finalized()


kx = np.linspace(-np.pi, np.pi, 101)
tmp0 = ({'mu':-0.3,'t':1,'delta':0.1,'B':0,'alpha':0,'k_x':x} for x in kx)
hamiltonians = np.stack([spinful_kitaev_chain_f.hamiltonian_submatrix(params=x) for x in tmp0], axis=0)
e_trivial = np.linalg.eigvalsh(hamiltonians)
tmp0 = ({'mu':0.3,'t':1,'delta':0.1,'B':0,'alpha':0,'k_x':x} for x in kx)
hamiltonians = np.stack([spinful_kitaev_chain_f.hamiltonian_submatrix(params=x) for x in tmp0], axis=0)
e_topological = np.linalg.eigvalsh(hamiltonians)

fig,(ax0,ax1) = plt.subplots(1,2,figsize=(8,5))
ax0.plot(kx, e_trivial)
ax1.plot(kx, e_topological)
for ax in [ax0,ax1]:
    ax.set_xlabel('$k$')
    ax.set_ylabel('$E/t$')
ax0.set_title('trivial')
ax1.set_title('topological')



Bs = np.linspace(0, 0.4, 10)
kx = np.linspace(-1, 1, 101)
energy = []
for B_i in Bs:
    tmp0 = ({'mu':0.3,'t':1,'delta':0.1,'B':B_i,'alpha':0,'k_x':x} for x in kx)
    hamiltonians = np.stack([spinful_kitaev_chain_f.hamiltonian_submatrix(params=x) for x in tmp0], axis=0)
    energy.append(np.linalg.eigvalsh(hamiltonians))
energy = np.stack(energy, axis=0)
ani = plt_animation_band(kx, Bs, energy, name='B')


# s-wave singlet
def onsite(onsite, t, mu, B, delta):
    return (2 * t - mu) * pauli.szs0 + B * pauli.s0sz + delta * pauli.sxs0
def hop(site1, site2, t, alpha):
    return -t * pauli.szs0 - 0.5j * alpha * pauli.szsx
nanowire_chain = kwant.Builder(kwant.TranslationalSymmetry([1]))
nanowire_chain[lat(0)] = onsite
nanowire_chain[kwant.HoppingKind((1,), lat)] = hop
nanowire_chain_f0 = kwant.wraparound.wraparound(nanowire_chain).finalized()
nanowire_chain_f1 = nanowire_chain.finalized() #what's the difference

Bs = np.linspace(0, 0.4, 10)
kx = np.linspace(-1, 1, 101)
energy = []
for B_i in Bs:
    tmp0 = ({'mu':0,'t':1,'delta':0.1,'B':B_i,'alpha':0,'k_x':x} for x in kx)
    hamiltonians = np.stack([nanowire_chain_f0.hamiltonian_submatrix(params=x) for x in tmp0], axis=0)
    energy.append(np.linalg.eigvalsh(hamiltonians))
energy = np.stack(energy, axis=0)
ani = plt_animation_band(kx, Bs, energy, name='B')


alphas = np.linspace(0, 0.4, 10)
kx = np.linspace(-1, 1, 101)
energy = []
for alpha_i in alphas:
    tmp0 = ({'mu':0.1,'t':1,'delta':0.1,'B':0.2,'alpha':alpha_i,'k_x':x} for x in kx)
    hamiltonians = np.stack([nanowire_chain_f0.hamiltonian_submatrix(params=x) for x in tmp0], axis=0)
    energy.append(np.linalg.eigvalsh(hamiltonians))
energy = np.stack(energy, axis=0)
ani = plt_animation_band(kx, alphas, energy, name=r'$\alpha$')



## bandgap
def find_gap(syst, params, resolution=1e-4):
    """
    Find gap in an infinite system by doing a binary search in energy.
    assumes that the system has particle-hole symmetry and only searches through positive energies.
    """
    hf_has_mode = lambda e: bool(len(syst.modes(e, params=params)[0].momenta))
    # Check if there are modes at the Fermi energy
    if hf_has_mode(0):
        return 0
    step = min(abs(kwant.physics.Bands(syst, params=params)(k=0))) / 2
    gap = step
    while step > resolution:
        step = step /2
        if hf_has_mode(gap):
            gap -= step
        else:
            gap += step
    return gap

Bs = np.linspace(0, 0.3, 71)
mus = np.linspace(-0.05, 0.15, 5)
alphas = np.array([0.0, 0.1, 0.2, 0.3])
gap = []
for mu_i,B_i,alpha_i in tqdm(list(itertools.product(mus,Bs,alphas))):
    param = {'t':1, 'delta':0.1, 'B':B_i, 'mu':mu_i, 'alpha':alpha_i}
    gap.append(find_gap(nanowire_chain_f1, param))
gap = np.array(gap).reshape(len(mus),len(Bs),len(alphas))

fig,ax = plt.subplots()
hline_list = []
for alpha_i,gap_i in zip(alphas,gap[0].T):
    tmp0 = r'\alpha'
    hline_list.append(ax.plot(Bs, gap_i, label=f'${tmp0}={alpha_i:.3f}$')[0])
ax.legend()
ax.set_xlabel('$B$')
ax.set_ylabel('band gap')
htitle = ax.set_title('$\mu={:.3f}$'.format(mus[0]))
ax.set_xlim(Bs.min(), Bs.max())
ax.set_ylim(0, gap.max())
def hf_frame(ind0):
    for hline_i,gap_i in zip(hline_list,gap[ind0].T):
        hline_i.set_data(Bs, gap_i)
    htitle.set_text('$\mu={:.3f}$'.format(mus[ind0]))
ani = matplotlib.animation.FuncAnimation(fig, hf_frame, frames=len(mus), interval=400)


alphas = np.linspace(0, 0.4, 10)
mus = np.linspace(-0.18, 0.22, 10)
kx = np.linspace(-1, 1, 101)
energy = []
for mu_i in mus:
    tmp0 = ({'mu':mu_i,'t':1,'delta':0.1,'B':0.2,'alpha':0.8,'k_x':x} for x in kx)
    hamiltonians = np.stack([nanowire_chain_f0.hamiltonian_submatrix(params=x) for x in tmp0], axis=0)
    energy.append(np.linalg.eigvalsh(hamiltonians))
energy = np.stack(energy, axis=0)
ani = plt_animation_band(kx, mus, energy, name=r'$\mu$')
