# https://topocondmat.org/w2_majorana/signatures.html
import numpy as np
import itertools
import matplotlib
import matplotlib.pyplot as plt
from tqdm import tqdm
plt.ion()

import kwant

from utils import pauli, tableau_colorblind


def plt_animation_band(kx, p_list, energy, name='', ylim=None):
    fig,ax = plt.subplots()
    hline_list = ax.plot(kx, energy[0])
    htitle = ax.set_title(f'{name}={p_list[0]:.3f}')
    if ylim is not None:
        ax.set_ylim(*ylim)
    ax.set_xlabel('k')
    def hf_frame(ind0):
        for hline_i,energy_i in zip(hline_list,energy[ind0].T):
            hline_i.set_data(kx, energy_i)
        htitle.set_text(f'{name}={p_list[ind0]:.3f}')
        return hline_list,htitle
    ani = matplotlib.animation.FuncAnimation(fig, hf_frame, frames=len(p_list), interval=200)
    return ani

def plt_colored_line_pump(xdata, ydata, cdata):
    N0,N1 = ydata.shape
    assert xdata.shape==(N0,)
    assert cdata.shape==(N0,N1)
    cdata = (cdata[:-1]+cdata[1:])/2

    tmp0 = np.repeat(xdata[:,np.newaxis], N1, axis=1)
    tmp1 = np.stack([tmp0,ydata], axis=2)
    segments = np.stack([tmp1[:-1],tmp1[1:]], axis=2).reshape(-1,2,2)
    fig,ax = plt.subplots()
    norm = plt.Normalize(cdata.min(), cdata.max())
    lc = matplotlib.collections.LineCollection(segments, cmap='seismic', norm=norm)
    lc.set_array(cdata.reshape(-1))
    line = ax.add_collection(lc)
    ax.set_xlim(xdata.min(), xdata.max())
    ax.set_ylim(0, 0.5)
    ax.set_xlabel(r'phase ($2\pi$)')
    ax.set_ylabel('energy')
    fig.tight_layout()
    return fig,ax


lat = kwant.lattice.chain(norbs=1)

# Plot of the potential in the pumping system as a function of coordinate.
# Some part of the leads is shown with a constant potential.
# Regions with E < 0 should be shaded to emulate Fermi sea.
A = 0.6
L = 10
lamb = (10 / 5.3) / (2 * np.pi)
mu = -0.4
mu_lead = -0.8


def f(x):
    if x < 0.0:
        return mu_lead
    if x >= 0.0 and x <= L:
        return mu + A * (1.0 - np.cos(x / lamb))
    if x > L:
        return mu_lead
x = np.linspace(-5, 15, 1000)
y = np.array([f(i) for i in x])

fig,ax = plt.subplots()
ax.plot(x, y, "k", lw=1.2)
tmp0 = np.minimum(0, y)
ax.fill_between(x, tmp0, 0, color="r", where=(y<0), alpha=0.5, edgecolor="k", lw=1.5)
ax.arrow(2.0, 1.25, 5, 0, head_width=0.15, head_length=1.0, fc="k", ec="k")
ax.set_xlabel("$x$")
ax.set_ylabel("$U(x)$")
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(-2.5, 12.5)
ax.set_ylim(-2, 2)



def hopping(site1, site2, t):
    return -t
def onsite(site, t, mu, A, phase, omega):
    return 2*t - mu + A * (np.cos(omega * site.pos[0] + phase) + 1)
param_pump = {
    'length': 17,
}
pump = kwant.Builder(kwant.TranslationalSymmetry([-param_pump['length']]))
pump[lat.shape((lambda x: True), [0])] = onsite
pump[lat.neighbors()] = hopping
pump_f = kwant.wraparound.wraparound(pump).finalized()

kx = np.linspace(-np.pi, np.pi, 100)
As = np.linspace(0, 0.8, 10)
energy = []
for A_i in As:
    tmp0 = ({'mu':0,'t':1,'phase':0,'A':A_i,'omega':2*np.pi/param_pump['length'], 'k_x':x} for x in kx)
    energy.append([np.linalg.eigvalsh(pump_f.hamiltonian_submatrix(params=x)) for x in tmp0])
energy = np.stack(energy, axis=0)
ani = plt_animation_band(kx, As, energy, name='A', ylim=(-0.2,1.3))



param = {
    'length': 60,
    'lead_length': 80,
}
syst = kwant.Builder()
syst.fill(pump, shape=(lambda site: 0 <= site.pos[0] < param['length']), start=[0])
lead = kwant.Builder(kwant.TranslationalSymmetry([-1]))
lead[lat(0)] = lambda site, t, mu_lead: 2 * t - mu_lead
lead[lat.neighbors()] = hopping
syst.attach_lead(lead, add_cells=param['lead_length'])
syst.attach_lead(lead.reversed(), add_cells=param['lead_length'])
syst_f = syst.finalized()

phases = np.linspace(0, 2*np.pi, 251)
energy = []
centers = []
# coord_operator = kwant.operator.Density(syst_f, onsite=(lambda site: site.pos[0] / (param['length'] + 2*param['lead_length'])), sum=True)
position_operator = np.arange(-param['lead_length'], param['length']+param['lead_length']) / (param['length']+2*param['lead_length'])
for phase_i in tqdm(phases):
    tmp0 = {'mu':0,'t':1,'phase':phase_i,'A':0.3,'omega':0.3,'mu_lead':0.1}
    # energy.append(np.linalg.eigvalsh(syst_f.hamiltonian_submatrix(params=tmp0)))
    EVL,EVC = np.linalg.eigh(syst_f.hamiltonian_submatrix(params=tmp0))
    energy.append(EVL)
    centers.append(np.abs(EVC.T)**2 @ position_operator)
energy = np.stack(energy)
centers = np.stack(centers)

fig,ax = plt.subplots()
ax.plot(phases/(2*np.pi), energy, color=tableau_colorblind[1])
ax.set_xlim(0, 1)
ax.set_ylim(0, 0.5)
ax.set_xlabel(r'phase ($2\pi$)')
ax.set_ylabel('energy')

plt_colored_line_pump(phases/(2*np.pi), energy, centers)



param = {
    'length': 100,
}
pump1 = kwant.Builder()
pump1.fill(pump, shape=(lambda site: 0 <= site.pos[0] < param['length']), start=[0])
lead = kwant.Builder(kwant.TranslationalSymmetry([-1]))
lead[lat(0)] = lambda site, t, mu_lead: 2 * t - mu_lead
lead[lat.neighbors()] = hopping
pump1.attach_lead(lead, add_cells=0)
pump1.attach_lead(lead.reversed(), add_cells=0)
pump1_f = pump1.finalized()

kx = np.linspace(-np.pi, np.pi, 100)
tmp0 = ({'mu':0, 't':1, 'phase':0, 'A':0.6, 'omega':2*np.pi/param_pump['length'], 'mu_lead':0, 'k_x':x} for x in kx)
pump_band = np.stack([np.linalg.eigvalsh(pump_f.hamiltonian_submatrix(params=x)) for x in tmp0], axis=0)

energy = [0.1, 0.3, 0.6, 0.9]
phases = np.linspace(0, 2 * np.pi, 100)
charge = []
for energy_i in energy:
    tmp0 = ({'mu':0, 't':1, 'phase':x, 'A':0.6, 'omega':0.3, 'mu_lead':0} for x in phases)
    determinants = np.array([np.linalg.det(kwant.smatrix(pump1_f, energy_i, params=x).submatrix(0, 0)) for x in tmp0])
    tmp1 = -np.unwrap(np.angle(determinants)) / (2*np.pi)
    charge.append(tmp1 - tmp1[0])
charge = np.stack(charge, axis=0)

fig,(ax0,ax1) = plt.subplots(1, 2, figsize=(8,5))
ax0.plot(kx, pump_band, color=tableau_colorblind[1])
for x,color_i in zip(energy,tableau_colorblind):
    ax0.axhline(x, linestyle=':', color=color_i)
ax0.set_xlim(-np.pi, np.pi)
ax0.set_ylim(-0.2, 1.3)
ax0.set_xlabel('kx')
ax0.set_ylabel('energy')
for energy_i,charge_i,color_i in zip(energy, charge, tableau_colorblind):
    ax1.plot(phases/(2*np.pi), charge_i, label=f'E={energy_i:.3f}', color=color_i)
ax1.legend()
ax1.set_xlabel(r'phase ($2\pi$)')
ax1.set_ylabel('pumped charge $q/e$')
ax1.set_xlim(0, 1)
fig.tight_layout()
