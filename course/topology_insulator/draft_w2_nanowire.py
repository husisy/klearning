# https://topocondmat.org/w1_topointro/1D.html
import numpy as np
import itertools
import matplotlib
import matplotlib.pyplot as plt
from tqdm import tqdm
plt.ion()

import kwant

from utils import pauli
cp_tableau = [x['color'] for x in plt.style.library['tableau-colorblind10']['axes.prop_cycle']]

lat_chain = kwant.lattice.chain()


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


def plt_animation_bandgap(alphas, Bs, mus, gap):
    fig,ax = plt.subplots()
    hline_list = []
    for alpha_i,gap_i in zip(alphas,gap[0].T):
        hline_list.append(ax.plot(Bs, gap_i, label=f'$\\alpha={alpha_i:.3f}$')[0])
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
    return ani


def hf_onsite(site, mu, t, B):
    ret = (2*t-mu)*pauli.szs0 + B*pauli.szsz # mu -> mu-2t
    return ret
def hf_hop01(site0, site1, t, delta):
    ret = -t*pauli.szs0 - 1j*delta*pauli.sys0
    return ret
param_chain0 = {'t':1}
dev_chain0 = kwant.Builder(kwant.TranslationalSymmetry([1]))
dev_chain0[lat_chain(0)] = hf_onsite
dev_chain0[kwant.HoppingKind((-1,), lat_chain)] = hf_hop01
dev_chain0_f = kwant.wraparound.wraparound(dev_chain0).finalized()
kx = np.linspace(-np.pi, np.pi, 101)
hf_EVL = lambda p: np.linalg.eigvalsh(dev_chain0_f.hamiltonian_submatrix(params=p))
e_trivial = np.stack([hf_EVL({'mu':-0.3,'t':1,'B':0,'delta':0.1,'k_x':x}) for x in kx], axis=0)
e_topological = np.stack([hf_EVL({'mu':0.3,'t':1,'B':0,'delta':0.1,'k_x':x}) for x in kx], axis=0)
fig,ax = plt.subplots()
hline0 = ax.plot(kx, e_trivial, color=cp_tableau[0])
hline0[0].set_label('trivial')
hline1 = ax.plot(kx, e_topological, color=cp_tableau[1])
hline1[0].set_label('topological')
ax.legend()
ax.set_xlabel('$k$')
ax.set_ylabel('$E/t$')

Bs = np.linspace(0, 0.4, 20)
tmp0 = ({'mu':0.3,'t':1,'B':x,'delta':0.1,'k_x':y} for x in Bs for y in kx)
energy = np.stack([hf_EVL(x) for x in tmp0]).reshape(len(Bs), len(kx), -1)
ani = plt_animation_band(kx, Bs, energy, name='B')

Deltas = np.linspace(0, 0.4, 20)
tmp0 = ({'mu':0.3,'t':1,'B':0,'delta':x,'k_x':y} for x in Deltas for y in kx)
energy = np.stack([hf_EVL(x) for x in tmp0]).reshape(len(Deltas), len(kx), -1)
ani = plt_animation_band(kx, Deltas, energy, name='\\Delta')


# s-wave singlet
def hf_onsite(site, t, mu, B, delta):
    ret = (2*t-mu)*pauli.szs0 + B*pauli.s0sz + delta*pauli.sxs0
    return ret
def hf_hop(site0, site1, t, alpha):
    # alpha is Rashba-SOI strength
    ret = -t*pauli.szs0 - 0.5j * alpha*pauli.szsx
    return ret
dev_chain1 = kwant.Builder(kwant.TranslationalSymmetry([1]))
dev_chain1[lat_chain(0)] = hf_onsite
dev_chain1[kwant.HoppingKind((1,), lat_chain)] = hf_hop #TODO, ham01 or ham10
dev_chain1_f0 = kwant.wraparound.wraparound(dev_chain1).finalized()
dev_chain1_f1 = dev_chain1.finalized()

kx = np.linspace(-1, 1, 101)
hf_EVL = lambda p: np.linalg.eigvalsh(dev_chain1_f0.hamiltonian_submatrix(params=p))
Bs = np.linspace(0, 0.4, 21)
energy = np.stack([hf_EVL({'mu':0,'t':1,'delta':0.1,'B':x,'alpha':0,'k_x':y})
        for x in Bs for y in kx], axis=0).reshape(len(Bs),len(kx),-1)
ani = plt_animation_band(kx, Bs, energy, name='B')

kx = np.linspace(-1, 1, 101)
alphas = np.linspace(0, 0.4, 20)
energy = np.stack([hf_EVL({'mu':0,'t':1,'delta':0.1,'B':0.2,'alpha':x,'k_x':y})
        for x in alphas for y in kx], axis=0).reshape(len(alphas),len(kx),-1)
ani = plt_animation_band(kx, alphas, energy, name=r'$\alpha$')

kx = np.linspace(-1, 1, 101)
mus = np.linspace(-0.18, 0.22, 20)
energy = np.stack([hf_EVL({'mu':x,'t':1,'delta':0.03,'B':0.07,'alpha':0.8,'k_x':y})
        for x in mus for y in kx], axis=0).reshape(len(mus),len(kx),-1)
ani = plt_animation_band(kx, mus, energy, name=r'$\mu$')


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
    gap.append(find_gap(dev_chain1_f1, param))
gap = np.array(gap).reshape(len(mus),len(Bs),len(alphas))
ani = plt_animation_bandgap(alphas, Bs, mus, gap)
