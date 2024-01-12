# https://github.com/tamuhey/python_1d_dft
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.ion()

num_x = 200
num_electron = 17
xspan = np.linspace(-5, 5, num_x)
delta_x = xspan[1]-xspan[0]

def get_exchange(xspan, density):
    dx = xspan[1]-xspan[0]
    tmp0 = density**(1/3)
    tmp1 = (3/np.pi)**(1/3)
    potential = -tmp1 * tmp0
    energy = -(3/4*tmp1*dx)*(tmp0*density).sum()
    return energy, potential

def fake_hatree_energy(xspan, density, epsilon):
    # coulomb potential not converged in 1D, so we add epsilon here
    dx = xspan[1]-xspan[0]
    tmp0 = 1/np.sqrt((xspan[:,None]-xspan)**2+epsilon)
    potential = (density*tmp0).sum(axis=1)*dx
    energy = (density*potential).sum()*dx/2
    return energy,potential

def DFT_1D_LDA(xspan, hamiltonian, num_electron, density=None, max_iteration=1000, epsilon=0.1):
    num_x = xspan.shape[0]
    if density is None:
        density = np.zeros(num_x)
    energy_history = [float('inf')]
    dx = xspan[1] - xspan[0]
    num_occupation = (np.arange(2*num_x).reshape(-1,2) < num_electron).sum(axis=1)
    for i in range(max_iteration):
        ex_energy, ex_potential = get_exchange(xspan, density)
        ha_energy, ha_potential = fake_hatree_energy(xspan, density, epsilon)
        energy, EVC= np.linalg.eigh(hamiltonian + np.diag(ex_potential+ha_potential))
        density = ((EVC**2)*num_occupation).sum(axis=1) / dx

        energy_diff = energy[0] - energy_history[-1]
        energy_history.append(energy[0])
        print(f"[step={i}] energy={energy[0]:.4f} energy_diff={energy_diff:.10f}")

        if abs(energy_diff) < 1e-5:
            break
    return density, EVC, energy

def plot_EVC(system_dict, xspan, num0=3, tag_DFT=False):
    fig,tmp0 = plt.subplots(2, 2, figsize=(8,6))
    ax_list = [tmp0[0][0],tmp0[0][1],tmp0[1][0],tmp0[1][1]]
    key_list = sorted(system_dict.keys())
    for ax,key in zip(ax_list,key_list):
        EVL = system_dict[key]['DFT_EVL' if tag_DFT else 'EVL']
        EVC = system_dict[key]['DFT_EVC' if tag_DFT else 'EVC']
        for ind0 in range(min(num0,len(xspan))):
            ax.plot(xspan, EVC[:,ind0], label=f'{EVL[ind0]:.2}')
        ax.legend()
        ax.set_title(key)
    fig.suptitle('DFT' if tag_DFT else 'no interaction')
    fig.tight_layout()

kinetic_op = np.eye(num_x)*(1/delta_x**2) + np.eye(num_x,k=1)*(-0.5/delta_x**2) + np.eye(num_x,k=-1)*(-0.5/delta_x**2)
tmp0 = np.zeros(num_x)
tmp0[np.abs(xspan)>2]=1e10
tmp1 = {
    '1D_well': kinetic_op,
    '1D_constrained_well': kinetic_op + np.diag(tmp0),
    'harmonic': kinetic_op + np.diag(xspan**2),
}
system_dict = dict()
num_occupation = (np.arange(2*num_x).reshape(-1,2) < num_electron).sum(axis=1)
for key,value in tmp1.items():
    EVL,EVC = np.linalg.eigh(value)
    density = ((EVC**2)*num_occupation).sum(axis=1) / delta_x
    system_dict[key] = {'hamiltonian':value, 'EVL':EVL, 'EVC':EVC, 'density':density}


for key,value in system_dict.items():
    density, EVC, energy = DFT_1D_LDA(xspan, value['hamiltonian'], num_electron)
    value['DFT_EVL'] = energy
    value['DFT_density'] = density
    value['DFT_EVC'] = EVC


plot_EVC(system_dict, xspan, tag_DFT=False)
plot_EVC(system_dict, xspan, tag_DFT=True)

fig,tmp0 = plt.subplots(2, 2, figsize=(8,6))
ax_list = [tmp0[0][0],tmp0[0][1],tmp0[1][0],tmp0[1][1]]
key_list = sorted(system_dict.keys())
for ax,key in zip(ax_list,key_list):
    ax.plot(xspan, system_dict[key]['DFT_density'], label='DFT density')
    ax.plot(xspan, system_dict[key]['density'], label="no-interaction")
    ax.legend()
fig.tight_layout()
