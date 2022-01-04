# https://topocondmat.org/w3_pump_QHE/Laughlinargument.html
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from tqdm import tqdm
plt.ion()

import kwant

from utils import pauli, tableau_colorblind

lat = kwant.lattice.square()


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
def hopping(site1, site2, t, B):
    x1, y1 = site1.pos
    x2, y2 = site2.pos
    return -t * np.exp(-0.5j * B * (x1 - x2) * (y1 + y2))
def make_lead_hop_y(x0):
    def hopping_Ay(site1, site2, t, B):
        y1 = site1.pos[1]
        y2 = site2.pos[1]
        return -t * np.exp(-1j * B * x0 * (y1 - y2))
    return hopping_Ay
def hf_shape_ribbon(pos):
    x,y = pos
    ret = (-param_ribbon["width"]//2<=y) and (y < (param_ribbon["width"]-param_ribbon["width"]//2))
    return ret

param_ribbon = {'width':20}
dev_ribbon = kwant.Builder(kwant.TranslationalSymmetry((-1, 0)))
dev_ribbon[lat.shape(hf_shape_ribbon, (0,0))] = onsite
dev_ribbon[lat.neighbors()] = hopping
dev_ribbon_f = kwant.wraparound.wraparound(dev_ribbon).finalized()

kx = np.linspace(-np.pi, np.pi, 101)
tmp0 = ({'t':1, 'mu':0.5, 'B':0.15, 'k_x':x} for x in kx)
energy = np.stack([np.linalg.eigvalsh(dev_ribbon_f.hamiltonian_submatrix(params=x)) for x in tmp0])
fig,ax = plt.subplots()
ax.plot(kx, energy, color=tableau_colorblind[1])
ax.axhline(0, linestyle=':', color='r')
ax.set_xlim(kx.min(), kx.max())
ax.set_ylim(-0.5, 0.5)
ax.set_xlabel('kx')
ax.set_ylabel('energy')


## hall bar
param_bar = {
    'length': 200, #L
    'width': 100, #W
    'lead4_width': 10, #w_lead
    'lead0_width': 10, #w_vert_lead
}
def hf_shape_bar(pos):
    (x, y) = pos
    ret = ((x>=-param_bar['length']/2) and (x<=param_bar['length']/2)) and ((y>=-param_bar['width']/2) and (y<=param_bar['width']/2))
    return ret
def hopping_Ax(site1, site2, t, B):
    x1, y1 = site1.pos
    x2, y2 = site2.pos
    ret = -t * np.exp(-0.5j * B * (x1 + x2) * (y1 - y2))
    return ret
def hf_shape_lead4(pos):
    (x, y) = pos
    ret = (-param_bar['lead4_width']/2<=y) and (y<=param_bar['lead4_width']/2)
    return ret
def hf_shape_lead0(pos):
    x,y = pos
    ret = (-param_bar['length']/4-param_bar['lead0_width']/2<=x) and (x<=-param_bar['length']/4+param_bar['lead0_width']/2)
    return ret
def hf_shape_lead1(pos):
    x,y = pos
    ret = (param_bar['length']/4-param_bar['lead0_width']/2<=x) and (x<=param_bar['length']/4+param_bar['lead0_width']/2)
    return ret
dev_bar = kwant.Builder()
dev_bar[lat.shape(hf_shape_bar, (0, 0))] = onsite
dev_bar[lat.neighbors()] = hopping_Ax
lead0 = kwant.Builder(kwant.TranslationalSymmetry((0, 1)))
lead1 = kwant.Builder(kwant.TranslationalSymmetry((0, 1)))
lead4 = kwant.Builder(kwant.TranslationalSymmetry((-1, 0)))
lead5 = kwant.Builder(kwant.TranslationalSymmetry((-1, 0)))
lead0[lat.shape(hf_shape_lead0, (-param_bar['length']/4,0))] = lead_onsite
lead0[lat.neighbors()] = make_lead_hop_y(0)
lead1[lat.shape(hf_shape_lead1, (param_bar['length']/4,0))] = lead_onsite
lead1[lat.neighbors()] = make_lead_hop_y(0)
lead4[lat.shape(hf_shape_lead4, (-1, 0))] = lead_onsite
lead4[lat.neighbors()] = make_lead_hop_y(-param_bar['length']/2)
lead5[lat.shape(hf_shape_lead4, (-1, 0))] = lead_onsite
lead5[lat.neighbors()] = make_lead_hop_y(param_bar['length']/2)
dev_bar.attach_lead(lead0)
dev_bar.attach_lead(lead1)
dev_bar.attach_lead(lead0.reversed())
dev_bar.attach_lead(lead1.reversed())
dev_bar.attach_lead(lead4)
dev_bar.attach_lead(lead5.reversed())
dev_bar_f = dev_bar.finalized()

tmp0 = {'t':1, 'mu':0.6, 'mu_lead':0.6, 'B':0.15, 'phi':0}
ldos = kwant.ldos(dev_bar_f, energy=0.0, params=tmp0) #(np,float64,20301)
fig,ax = plt.subplots()
kwant.plotter.map(dev_bar_f, ldos, num_lead_cells=20, colorbar=False, ax=ax)
ax.axis("off")



## ring
param_ring = {
    'r_out': 120,
    'r_in': 60,
    'lead_width': 10, #w_lead
}
param_ring['lead_width']
def hf_shape_ring(pos):
    (x, y) = pos
    tmp0 = x ** 2 + y ** 2
    ret = (param_ring['r_in']**2<tmp0) and (tmp0<param_ring['r_out']**2)
    return ret
def hf_shape_hops_across_cut(syst):
    ret = []
    for hop in kwant.builder.HoppingKind((1, 0), lat, lat)(syst):
        x1, y1 = hop[0].pos
        x2, y2 = hop[1].pos
        if (y1<0) and (x1>0.5) and (x2<0.5):
            ret.append(hop)
    return ret
def hf_shape_lead(pos):
    (x, y) = pos
    ret = (-param_ring['lead_width']/2<y) and (y<param_ring['lead_width']/2)
    return ret
def branchcut_hopping(site1, site2, t, B, phi):
    ret = hopping(site1, site2, t, B) * np.exp(1j * phi)
    return ret

dev_ring = kwant.Builder()
dev_ring[lat.shape(hf_shape_ring, (0,param_ring['r_in']+1))] = onsite
dev_ring[lat.neighbors()] = hopping
dev_ring[hf_shape_hops_across_cut] = branchcut_hopping
lead = kwant.Builder(kwant.TranslationalSymmetry((-1, 0)))
lead[lat.shape(hf_shape_lead, (0, 0))] = lead_onsite
lead[lat.neighbors()] = lambda site1, site2, t: -t
dev_ring.attach_lead(lead)
dev_ring.attach_lead(lead, origin=lat(0, 0))
dev_ring_f = dev_ring.finalized()

tmp0 = {'t':1, 'mu':0.9, 'mu_lead':0.9, 'B':0.15, 'phi':0}
ldos = kwant.ldos(dev_ring_f, energy=0.0, params=tmp0)
fig,ax = plt.subplots()
kwant.plotter.map(dev_ring_f, ldos, num_lead_cells=20, colorbar=False, ax=ax)
ax.axis("off")
