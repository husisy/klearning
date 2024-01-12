# https://topocondmat.org/w3_pump_QHE/Laughlinargument.html
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from tqdm import tqdm
plt.ion()

import kwant

from utils import pauli, tableau_colorblind

lat = kwant.lattice.square()

def plt_bar_conductance(Bs, conductance_xx, conductance_xy):
    xdata = 1/Bs
    fig,ax = plt.subplots()
    ax.plot(xdata, conductance_xx, label=r'$\sigma_{xx}$')
    ax.plot(xdata, conductance_xy, label=r'$\sigma_{xy}$')
    ax.legend()
    ax.set_xlabel('$B^{-1} [a.u.]$')
    ax.set_ylabel('conductance ($e^2/h$)')
    ax.set_xlim(xdata.min(), xdata.max())
    return fig,ax

def plt_animation_QHE(phis, mus, charges, kx, energy):
    fig,(ax0,ax1) = plt.subplots(1, 2, figsize=(8,5))
    hline, = ax0.plot(phis/(2*np.pi), charges[0])
    htitle0 = ax0.set_title(r'$\mu={:.2f}, \sigma_H={:.2f}e^2/h$'.format(mus[0], charges[0,-1]))
    ax0.set_xlim(0, 1)
    ax0.set_ylim(0, charges.max())
    ax0.set_xlabel('$\phi (2\pi)$')
    ax0.set_ylabel('#pumped charge')
    hline_list = []
    for energy_i in energy[0].T:
        hline_list.append(ax1.plot(kx, energy_i, color=tableau_colorblind[1])[0])
    ax1.axhline(0, linestyle=':', color='r')
    ax1.set_xlim(kx.min(), kx.max())
    ax1.set_ylim(-1.2, 1.2)
    ax1.set_xlabel('kx')
    ax1.set_title('Landau band')
    fig.tight_layout()
    def hf_frame(ind0):
        hline.set_data(phis/(2*np.pi), charges[ind0])
        for hline_i,energy_i in zip(hline_list,energy[ind0].T):
            hline_i.set_data(kx, energy_i)
        htitle0.set_text(r'$\mu={:.2f}, \sigma_H={:.2f}e^2/h$'.format(mus[ind0], charges[ind0,-1]))
        return hline,hline_list,htitle0
    ani = matplotlib.animation.FuncAnimation(fig, hf_frame, frames=len(mus), interval=300)
    return ani

'''
    L0     L1
    |      |
L4 --- C ---- L5
    |      |
    L2     L3
'''


def onsite(site, t, mu):
    return 4 * t - mu
def lead_onsite(site, t, mu_lead):
    return 4 * t - mu_lead
def hopping(xy0, xy1, t, B):
    x0, y0 = xy0.pos
    x1, y1 = xy1.pos
    ret = -t * np.exp(-0.5j * B * (x0 - x1) * (y0 + y1))
    return ret
def hopping_Ax(xy0, xy1, t, B):
    x0,y0 = xy0.pos
    x1,y1 = xy1.pos
    ret = -t * np.exp(-0.5j * B * (x0+x1) * (y0-y1))
    return ret
def make_lead_hop_y(x0):
    def hopping_Ay(site1, site2, t, B):
        y1 = site1.pos[1]
        y2 = site2.pos[1]
        ret = -t * np.exp(-1j * B * x0 * (y1 - y2))
        return ret
    return hopping_Ay

def hf_shape_bar(xy):
    x,y = xy
    ret = (x>=-param_bar['length']/2) and (x<=param_bar['length']/2) and (y>=-param_bar['width']/2) and (y<=param_bar['width']/2)
    return ret
def hf_shape_lead1(pos):
    x,y = pos
    ret = ((-param_bar['length']/4-param_bar['V_lead_width']/2)<=x) and (x<=(-param_bar['length']/4+param_bar['V_lead_width']/2))
    return ret
def hf_shape_lead2(pos):
    x,y = pos
    ret = ((param_bar['length']/4-param_bar['V_lead_width']/2)<=x) and (x<=(param_bar['length']/4+param_bar['V_lead_width']/2))
    return ret
def hf_shape_lead5(pos):
    x, y = pos
    ret = (-param_bar['H_lead_width']/2<=y) and (y<=param_bar['H_lead_width']/2)
    return ret

param_bar = {
    'length': 60,
    'width': 80,
    'H_lead_width': 70,
    'V_lead_width': 28,
}
dev_bar = kwant.Builder()
dev_bar[lat.shape(hf_shape_bar, (0,0))] = onsite
dev_bar[lat.neighbors()] = hopping_Ax
lead0 = kwant.Builder(kwant.TranslationalSymmetry((0, 1)))
lead1 = kwant.Builder(kwant.TranslationalSymmetry((0, 1)))
lead4 = kwant.Builder(kwant.TranslationalSymmetry((-1, 0)))
lead5 = kwant.Builder(kwant.TranslationalSymmetry((-1, 0)))
lead0[lat.shape(hf_shape_lead1, (-param_bar['length']/4,0))] = lead_onsite
lead0[lat.neighbors()] = make_lead_hop_y(0)
lead1[lat.shape(hf_shape_lead2, (param_bar['length']/4,0))] = lead_onsite
lead1[lat.neighbors()] = make_lead_hop_y(0)
lead4[lat.shape(hf_shape_lead5, (-1, 0))] = lead_onsite
lead4[lat.neighbors()] = make_lead_hop_y(-param_bar['length']/2)
lead5[lat.shape(hf_shape_lead5, (-1, 0))] = lead_onsite
lead5[lat.neighbors()] = make_lead_hop_y(param_bar['length']/2)
dev_bar.attach_lead(lead0)
dev_bar.attach_lead(lead1)
dev_bar.attach_lead(lead0.reversed())
dev_bar.attach_lead(lead1.reversed())
dev_bar.attach_lead(lead4)
dev_bar.attach_lead(lead5.reversed())
dev_bar_f = dev_bar.finalized()

Bs = np.linspace(0.02, 0.15, 200)
conductance = []
conductance_xx = []
conductance_xy = []
for B_i in tqdm(Bs):
    tmp0 = {'t':1, 'mu':0.3, 'mu_lead':0.3, 'B':B_i}
    G = kwant.smatrix(dev_bar_f, params=tmp0).conductance_matrix()
    voltage = np.linalg.solve(G[:-1, :-1], [0, 0, 0, 0, 1]) #GV=I, rank(G)=5, inv(G) not exists
    E_x = voltage[0] - voltage[1] #TODO, what about the length?
    E_y = voltage[1] - voltage[3]
    conductance_xx.append(E_x / (E_x**2 + E_y**2))
    conductance_xy.append(E_y / (E_x**2 + E_y**2))
    conductance.append(G)
conductance = np.stack(conductance, axis=0)
conductance_xx = np.array(conductance_xx)
conductance_xy = np.array(conductance_xy)
plt_bar_conductance(Bs, conductance_xx, conductance_xy)


# also see https://kwant-project.org/doc/1/tutorial/spin_potential_shape#nontrivial-shapes
def hf_shape_ring(xy):
    tmp0 = xy[0]**2 + xy[1]**2
    ret = (param_ring['r_in']**2<tmp0) and (tmp0<param_ring['r_out']**2)
    return ret
def hf_shape_lead(pos):
    (x, y) = pos
    ret = (-param_ring['lead_width']/2<y) and (y<param_ring['lead_width']/2)
    return ret
def branchcut_hopping(site1, site2, t, B, phi):
    ret = hopping(site1, site2, t, B) * np.exp(1j * phi)
    return ret
def hops_across_cut(syst):
    ret = []
    for hop in kwant.builder.HoppingKind((1, 0), lat, lat)(syst):
        x0, y0 = hop[0].pos
        x1, _ = hop[1].pos
        if (y0 < 0) and (x0 > 0.5) and (x1 < 0.5):
            ret.append(hop)
    return ret
param_ring = {
    'width': 20,
    'r_in': 20,
    'lead_width': 10,
}
param_ring['r_out'] = 2*param_ring['width']
dev_ring = kwant.Builder()
dev_ring[lat.shape(hf_shape_ring, (0, param_ring['r_in'] + 1))] = onsite
dev_ring[lat.neighbors()] = hopping
dev_ring[hops_across_cut] = branchcut_hopping
lead = kwant.Builder(kwant.TranslationalSymmetry((-1, 0)))
lead[lat.shape(hf_shape_lead, (0, 0))] = lead_onsite
lead[lat.neighbors()] = lambda site1, site2, t: -t
dev_ring.attach_lead(lead)
dev_ring.attach_lead(lead, origin=lat(0, 0))
dev_ring_f = dev_ring.finalized()

dev_ribbon = kwant.Builder(kwant.TranslationalSymmetry((-1, 0)))
dev_ribbon[lat.shape((lambda pos: 0 <= pos[1] < param_ring['width']), (0, 0))] = onsite
dev_ribbon[lat.neighbors()] = hopping
dev_ribbon[lat(0, 0), lat(0, param_ring['width']-1)] = hopping
dev_ribbon_f = kwant.wraparound.wraparound(dev_ribbon).finalized()

mus = np.linspace(0.4, 1.7, 11)
phis = np.linspace(0, 2*np.pi, 40)
kx = np.linspace(-1, 1, 101)

charges = []
for mu_i in tqdm(mus):
    tmp0 = ({'t':1, 'mu':mu_i, 'B':2*np.pi/param_ring['width'], 'mu_lead':mu_i, 'phi':x} for x in phis)
    rs = [kwant.smatrix(dev_ring_f, energy=0.0, params=x).submatrix(1, 1) for x in tmp0]
    angle = np.array([np.angle(np.linalg.det(x)) for x in rs])
    tmp0 = -np.unwrap(angle) / (2*np.pi)
    charges.append(tmp0-tmp0[0])
charges = np.stack(charges)

energy = []
for mu_i in mus:
    tmp0 = ({'t':1, 'mu':mu_i, 'B':2*np.pi/param_ring['width'], 'mu_lead':mu_i, 'k_x':x} for x in kx)
    energy.append(np.stack([np.linalg.eigvalsh(dev_ribbon_f.hamiltonian_submatrix(params=x)) for x in tmp0]))
energy = np.stack(energy, axis=0)
ani = plt_animation_QHE(phis, mus, charges, kx, energy)
