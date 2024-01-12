# https://topocondmat.org/w2_majorana/signatures.html
import numpy as np
import itertools
import matplotlib
import matplotlib.pyplot as plt
from tqdm import tqdm
plt.ion()

import kwant

from utils import pauli

tableau_colorblind = [x['color'] for x in plt.style.library['tableau-colorblind10']['axes.prop_cycle']]


def plt_animation_NS_conductance(energy, V_barrier, Gs_trivial, Gs_topological):
    fig,ax = plt.subplots()
    hline0, = ax.plot(energy, Gs_trivial[0], label='trival')
    hline1, = ax.plot(energy, Gs_topological[0], label='topological')
    ax.set_xlabel('energy')
    ax.set_ylabel('$G/G_0$')
    ax.legend()
    htitle = ax.set_title('$V_{barrier}='+f'{V_barrier[0]:.3}$')
    ax.set_xlim(energy.min(), energy.max())
    ax.set_ylim(0, max(Gs_trivial.max(), Gs_topological.max()))

    def hf_frame(ind0):
        hline0.set_data(energy,Gs_trivial[ind0])
        hline1.set_data(energy,Gs_topological[ind0])
        htitle.set_text('$V_{barrier}='+f'{V_barrier[ind0]:.3}$')
        return hline0,hline1,htitle
    ani = matplotlib.animation.FuncAnimation(fig, hf_frame, frames=len(V_barrier), interval=200)
    return ani


lat = kwant.lattice.chain(norbs=4)


def onsite_barrier(site, t, mu_n, V_barrier, Ez):
    return (2 * t - mu_n + V_barrier) * pauli.s0sz + Ez * pauli.sxs0
# The scattering region: one site with a tunnel barrier
tunnel_spectroscopy_device = kwant.Builder()
tunnel_spectroscopy_device[lat(0)] = onsite_barrier

# Normal lead: charge conservation and no gap
def onsite_normal(site, t, mu_n, Ez):
    return (2 * t - mu_n) * pauli.s0sz + Ez * pauli.sxs0
normal_lead = kwant.Builder(kwant.TranslationalSymmetry([1]), conservation_law=-pauli.s0sz)
normal_lead[lat(0)] = onsite_normal

# Superconductor has a gap.
def onsite_sc(site, t, mu_sc, Ez, delta):
    return (2 * t - mu_sc) * pauli.s0sz + Ez * pauli.sxs0 + delta * pauli.s0sx
def hop(site1, site2, t, alpha):
    return -t * pauli.s0sz + 0.5j * alpha * pauli.sysz
superconductor = kwant.Builder(kwant.TranslationalSymmetry([1]))
superconductor[lat(0)] = onsite_sc
normal_lead[lat(1), lat(0)] = hop
superconductor[lat(1), lat(0)] = hop

# Attach leads to the scattering region
tunnel_spectroscopy_device.attach_lead(normal_lead)
tunnel_spectroscopy_device.attach_lead(superconductor.reversed())
tunnel_spectroscopy_device_f = tunnel_spectroscopy_device.finalized()


def Andreev_conductance(syst, params, energy=0):
    smatrix = kwant.smatrix(syst, energy=energy, params=params, in_leads=[0], out_leads=[0])
    n_modes = smatrix.lead_info[0].block_nmodes[0]
    ret = n_modes - smatrix.transmission((0, 0), (0, 0)) + smatrix.transmission((0, 1), (0, 0))
    return ret


V_barrier = np.arange(1, 4.25, 0.25)
energy = np.linspace(-0.15, 0.15, 101)
Gs_trivial = []
Gs_topological = []
for x,y in tqdm(itertools.product(V_barrier,energy), total=len(V_barrier)*len(energy)):
    # Ez: magnetic field
    tmp0 = {'t':1, 'mu_n':0.5, 'mu_sc':0, 'alpha':0.3, 'delta':0.1, 'Ez':0, 'V_barrier':x}
    Gs_trivial.append(Andreev_conductance(tunnel_spectroscopy_device_f, tmp0, y))
    tmp0 = {'t':1, 'mu_n':0.5, 'mu_sc':0, 'alpha':0.3, 'delta':0.1, 'Ez':0.25, 'V_barrier':x}
    Gs_topological.append(Andreev_conductance(tunnel_spectroscopy_device_f, tmp0, y))
Gs_trivial = np.array(Gs_trivial).reshape(len(V_barrier),-1)
Gs_topological = np.array(Gs_topological).reshape(len(V_barrier),-1)
ani = plt_animation_NS_conductance(energy, V_barrier, Gs_trivial, Gs_topological)



# Make a finite ring.
def junction_hopping(site1, site2, t, alpha, flux):
    phase = np.exp(1j * flux / 2)
    phase_factors = np.kron(pauli.s0, np.diag([phase, phase.conj()]))
    reduction = 0.7  # Make the hopping weaker by this factor.
    return reduction * phase_factors @ hop(site1, site2, t, alpha)
L = 100
ring_length = 100
ring = kwant.Builder()
ring.fill(superconductor, shape=(lambda site: 0 <= site.pos[0] < ring_length), start=[0])
ring[lat(0), lat(ring_length-1)] = junction_hopping
ring_f = ring.finalized()

fluxes = np.linspace(0, 4 * np.pi, 51)
params = dict(mu_sc=0.4, t=1.0, alpha=0.2, delta=0.1, Ez=1)
tag_topological = False
if tag_topological:
    tmp0 = ({'mu_sc':0.4, 't':1, 'alpha':0.2, 'delta':0.1, 'Ez':1, 'flux':x} for x in fluxes) #topological
else:
    tmp0 = ({'mu_sc':0.4, 't':1, 'alpha':0.2, 'delta':0.1, 'Ez':0.2, 'flux':x} for x in fluxes) #trival
energy = np.stack([np.linalg.eigvalsh(ring_f.hamiltonian_submatrix(params=x)) for x in tmp0], axis=0)

# Exchange two lowest energy states if parity is odd.
if tag_topological:
    N = energy.shape[1] // 2
    ind0 = np.logical_and(fluxes > np.pi, fluxes < 3 * np.pi)
    energy[ind0, (N-1):(N+1)] *= -1

energy_gs = np.sum(energy[:, :N], axis=1)
energy_gs -= np.max(energy_gs)
current = np.diff(energy_gs) * len(energy_gs)


fig,ax = plt.subplots()
ax.plot(fluxes/(2*np.pi), energy, color=tableau_colorblind[0])
ax.plot(fluxes/(2*np.pi), energy[:,energy.shape[1]//2-1], color='r')
ax.set_xlim(0, 2)
ax.set_ylim(-0.11, 0.11)
ax.set_xlabel(r'$\Phi/\Phi_0$')
ax.set_ylabel('energy')

fig,(ax0,ax1) = plt.subplots(1, 2, figsize=(8,5))
ax0.plot(fluxes/(2*np.pi), energy_gs)
ax0.set_xlabel(r'$\Phi/\Phi_0$')
ax0.set_ylabel('$E_{total}$')
ax0.set_xlim(0, 2)
ax0.set_ylim(-0.06, 0)
ax1.plot((fluxes[:-1]+fluxes[1:])/(2*2*np.pi), current)
ax1.set_xlabel(r'$\Phi/\Phi_0$')
ax1.set_ylabel('$I$')
ax1.set_xlim(0, 2)
fig.tight_layout()
