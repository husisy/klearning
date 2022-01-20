import numpy as np
import pfapack.pfaffian
import matplotlib.pyplot as plt
plt.ion()

tableau_colorblind = [x['color'] for x in plt.style.library['tableau-colorblind10']['axes.prop_cycle']]

from utils import pauli

def rand_hermite_matrix(N, tag_complex=True, np_rng=None):
    np_rng = np.random.default_rng() if np_rng is None else np_rng
    if tag_complex:
        tmp0 = np_rng.normal(size=(N,N)) + 1j*np_rng.normal(size=(N,N))
    else:
        tmp0 = np_rng.normal(size=(N,N))
    ret = (tmp0 + tmp0.T.conj()) / 2
    return ret


def rand_symplectic_matrix(N, np_rng=None):
    assert N%2==0
    sy = np.kron(np.eye(N//2), pauli.sy)
    tmp0 = rand_hermite_matrix(N, tag_complex=True, np_rng=np_rng)
    tmp1 = sy @ tmp0.conj() @ sy
    ret = (tmp0 + tmp1) / 2
    return ret


def rand_chiral_ham(N, np_rng=None):
    assert N%2==0
    np_rng = np.random.default_rng() if np_rng is None else np_rng
    tmp0 = np_rng.normal(size=(N//2,N//2)) + 1j*np_rng.normal(size=(N//2,N//2))
    tmp1 = np.zeros_like(tmp0)
    ret = np.block([[tmp1,tmp0],[tmp0.T.conj(),tmp1]])
    # sublattice symmetry sigma_z*H*sigma_z=-H
    tmp0 = np.kron(pauli.sz, np.eye(N//2))
    assert np.abs(tmp0 @ ret @ tmp0 + ret).max() < 1e-10
    return ret


def rand_BdG_ham(N, np_rng=None):
    # antisymmetric hermitian matrix
    np_rng = np.random.default_rng() if np_rng is None else np_rng
    tmp0 = np_rng.normal(size=(N,N))
    ret = 1j*(tmp0 - tmp0.T)
    return ret


def H0_to_H1_spectrum(H0, H1, N=1000):
    tmp0 = np.linspace(0, 1, N)
    ret = np.stack([np.linalg.eigvalsh((1-x)*H0 + x*H1) for x in tmp0])
    return ret


def H0_to_H1_pfaffian(H0, H1, N=1000):
    tmp0 = np.linspace(0, 1, N)
    tmp1 = (1j*((1-x)*H0 + x*H1) for x in tmp0)
    ret = np.array([np.sign(pfapack.pfaffian.pfaffian(x).real) for x in tmp1])
    return ret


def plot_spectrum(ydata, ydata1=None, title=''):
    xdata = np.linspace(0, 1, ydata.shape[0])
    if ydata1 is None:
        ydata1 = (ydata<0).sum(axis=1)
    fig,ax0 = plt.subplots()
    ax1 = ax0.twinx()
    ax0.plot(xdata, ydata, color=tableau_colorblind[1])
    ax0.axhline(0, linestyle=':')
    ax1.fill_between(xdata, ydata1, alpha=0.3)
    ax1.set_ylim(ydata1.min()-1, ydata1.max()*2.5)
    ax0.set_xlim(0, 1)
    ax0.set_title(title)
    fig.tight_layout()
    return fig


# nothing special
H0 = rand_hermite_matrix(10, tag_complex=False)
H1 = rand_hermite_matrix(10, tag_complex=False)
spectrum = H0_to_H1_spectrum(H0, H1)
plot_spectrum(spectrum, title='time-reversal symmetry + spinless = real')

# Krammer degeneracy
H0 = rand_symplectic_matrix(10)
H1 = rand_symplectic_matrix(10)
spectrum = H0_to_H1_spectrum(H0, H1)
plot_spectrum(spectrum, title='time-reversal spin-1/2 symmetry')


# sigma_z @ H @ sigma_z = -H
# (E,-E) and no cross zero
H0 = rand_chiral_ham(10)
H1 = rand_chiral_ham(10)
spectrum = H0_to_H1_spectrum(H0, H1)
plot_spectrum(spectrum, title='sublattice symmetry')


H0 = rand_BdG_ham(10)
H1 = rand_BdG_ham(10)
spectrum = H0_to_H1_spectrum(H0, H1, N=1000)
pfaffian = H0_to_H1_pfaffian(H0, H1, N=1000)
plot_spectrum(spectrum, ydata1=pfaffian, title='BdG, electron-hole symmetry')
