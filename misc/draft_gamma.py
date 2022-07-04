import numpy as np
import itertools
import types
import functools


# https://www.zhihu.com/question/42888092
# https://en.wikipedia.org/wiki/Clifford_algebra
# https://en.wikipedia.org/wiki/Gamma_matrices
s0 = np.array([[1.0, 0.0], [0.0, 1.0]])
sx = np.array([[0.0, 1.0], [1.0, 0.0]])
sy = np.array([[0.0, -1j], [1j, 0.0]])
sz = np.array([[1.0, 0.0], [0.0, -1.0]])
gamma0 = np.array([[1,0,0,0],[0,1,0,0],[0,0,-1,0],[0,0,0,-1]])
gamma1 = np.array([[0,0,0,1],[0,0,1,0],[0,-1,0,0],[-1,0,0,0]])
gamma2 = np.array([[0,0,0,-1j],[0,0,1j,0],[0,1j,0,0],[-1j,0,0,0]])
gamma3 = np.array([[0,0,1,0],[0,0,0,-1],[-1,0,0,0],[0,1,0,0]])
gamma5 = np.array([[0,0,1,0],[0,0,0,1],[1,0,0,0],[0,1,0,0]])
pauli = types.SimpleNamespace(
    s0 = s0,
    sx = sx,
    sy = sy,
    sz = sz,
    gamma0 = gamma0,
    gamma1 = gamma1,
    gamma2 = gamma2,
    gamma3 = gamma3,
    gamma5 = gamma5,
    s0s0 = np.kron(s0, s0),
    s0sx = np.kron(s0, sx),
    s0sy = np.kron(s0, sy),
    s0sz = np.kron(s0, sz),
    sxs0 = np.kron(sx, s0),
    sxsx = np.kron(sx, sx),
    sxsy = np.kron(sx, sy),
    sxsz = np.kron(sx, sz),
    sys0 = np.kron(sy, s0),
    sysx = np.kron(sy, sx),
    sysy = np.kron(sy, sy),
    sysz = np.kron(sy, sz),
    szs0 = np.kron(sz, s0),
    szsx = np.kron(sz, sx),
    szsy = np.kron(sz, sy),
    szsz = np.kron(sz, sz),
)


def check_gamma_property():
    # https://en.wikipedia.org/wiki/Gamma_matrices
    tmp0 = [pauli.gamma0,pauli.gamma1,pauli.gamma2,pauli.gamma3,pauli.gamma5]
    eta = np.diag(np.array([1,-1,-1,-1,1]))
    for i,j in itertools.product(range(len(tmp0)),range(len(tmp0))):
        tmp1 = tmp0[i] @ tmp0[j] + tmp0[j] @ tmp0[i]
        tmp2 = 2*eta[i,j]*np.eye(4)
        assert np.abs(tmp1-tmp2)<1e-7


def angular_matrix(J, kind):
    # https://en.wikipedia.org/wiki/Angular_momentum_operator
    # http://publish.illinois.edu/davidchen/files/2012/10/Matrix-representation-of-angular-momentum.pdf
    assert kind in 'xyzpm'
    hf_is_integer = lambda x: abs(x-int(x)) < 1e-7
    assert J>0.1
    assert hf_is_integer(J) or hf_is_integer(J*2)
    J2 = int(J*2)
    m = J-np.arange(J2+1)
    if hf_is_integer(J):
        J = int(J)
    else:
        J2 = int(J*2)
        J = J2/2
    tmp0 = np.sqrt(J*(J+1) - m[1:]*m[:-1])
    if kind=='x':
        tmp1 = tmp0 / 2
        ret = np.diag(tmp1, 1) + np.diag(tmp1, -1)
    elif kind=='y':
        tmp1 = tmp0 / 2j
        ret = np.diag(tmp1, 1) + np.diag(-tmp1, -1)
    elif kind=='z':
        ret = np.diag(m)
    elif kind=='p':
        ret = np.diag(tmp0, 1)
    else: #m
        ret = np.diag(tmp0, -1)
    return ret


def pauli_matrix_decomposition4(np0, check=False):
    assert np0.shape==(4,4)
    tmp0 = [('0',pauli.s0), ('x',pauli.sx), ('y',pauli.sy), ('z',pauli.sz)]
    ret = []
    hf_trace = lambda x,y: (x*y.T).sum()
    for stri,si in tmp0:
        for strj,sj in tmp0:
            tmp1 = hf_trace(np.kron(si, sj), np0)/4
            ret.append((stri+strj,tmp1))
    if check:
        tmp0 = dict(tmp0)
        tmp1 = 0
        for x,y in ret:
            tmp1 = tmp1 + np.kron(tmp0[x[0]], tmp0[x[1]])*y
        print(np.abs(np0-tmp1).max())
    return ret



def generate_Z_gamma():
    #https://journals.aps.org/prb/abstract/10.1103/PhysRevB.69.235206
    xi = np.zeros((5,3,3), dtype=np.float64) #[01234, xyz, xyz]
    def hf0(i0, i1, i2, value):
        xi[i0,i1,i2] = value
        if i1!=i2:
            xi[i0,i2,i1] = value
    xi[0,1,2] = 1/(2*np.sqrt(3))
    tmp0 = 1/(2*np.sqrt(3))
    tmp1 = [(0,1,2,tmp0), (1,2,0,tmp0), (2,0,1,tmp0), (3,0,0,tmp0), (3,1,1,-tmp0)]
    for x in tmp1:
        hf0(*x)
    xi[4,0,0] = -1/6
    xi[4,1,1] = -1/6
    xi[4,2,2] = 1/3
    Z_gamma = types.SimpleNamespace(
        gamma1 = np.kron(pauli.sz, pauli.sy),
        gamma2 = np.kron(pauli.sz, pauli.sx),
        gamma3 = np.kron(pauli.sy, pauli.s0),
        gamma4 = np.kron(pauli.sx, pauli.s0),
        gamma5 = np.kron(pauli.sz, pauli.sz),
        xi = xi,
    )
    return Z_gamma
Z_gamma = generate_Z_gamma()

def check_Z_gamma():
    # Gamma^a Gamma^b + Gamma^b Gamma^a = 2 delta_{ab}
    tmp0 = [Z_gamma.gamma1, Z_gamma.gamma2, Z_gamma.gamma3, Z_gamma.gamma4, Z_gamma.gamma5]
    eta = 2*np.eye(5)
    for ind0 in range(5):
        for ind1 in range(5):
            tmp1 = np.abs(tmp0[ind0]@tmp0[ind1] + tmp0[ind1]@tmp0[ind0])
            tmp2 = eta[ind0,ind1]*np.eye(4)
            assert np.abs(tmp1-tmp2).max()<1e-7

    # Gamma^a = xi_a^{ij} {S^i, S^j}
    tmp0 = [Z_gamma.gamma1, Z_gamma.gamma2, Z_gamma.gamma3, Z_gamma.gamma4, Z_gamma.gamma5]
    tmp0 = np.stack(tmp0, axis=0)
    tmp1 = np.stack([angular_matrix(3/2, x) for x in 'xyz'], axis=0)
    tmp2 = (np.einsum(Z_gamma.xi, [0,1,2], tmp1, [1,3,4], tmp1, [2,4,5], [0,3,5])
            + np.einsum(Z_gamma.xi, [0,1,2], tmp1, [2,3,4], tmp1, [1,4,5], [0,3,5]))
    assert np.abs(tmp0-tmp2).max()<1e-7

    # Gamma_1 Gamma_2 Gamma_3 Gamma_4 Gamma_5 = -1
    tmp0 = [Z_gamma.gamma1, Z_gamma.gamma2, Z_gamma.gamma3, Z_gamma.gamma4, Z_gamma.gamma5]
    assert np.abs(functools.reduce(np.matmul, tmp0) + np.eye(4)).max() < 1e-7


def gellmann_matrix(j, k, d, is_sparse=True):
    # TODO is_sparse use scipy.sparse.array (v-1.8 required)
    # https://en.wikipedia.org/wiki/Gell-Mann_matrices
    # https://en.wikipedia.org/wiki/Generalizations_of_Pauli_matrices
    # https://github.com/CQuIC/pysme/blob/master/src/pysme/gellmann.py
    assert (d>0) and (0<=j<d) and (0<=k<d)
    if j > k:
        ind0 = [j, k]
        ind1 = [k, j]
        data = [1, 1]
    elif k > j:
        ind0 = [j, k]
        ind1 = [k, j]
        data = [-1j, 1j]
    elif j == k and j < d-1:
        ind0 = np.arange(j+2)
        ind1 = ind0
        data = np.sqrt(2/((j+1)*(j+2)))*np.array([1]*(j+1) + [-(j+1)])
    else:
        ind0 = np.arange(d)
        ind1 = ind0
        data = np.ones(d)
    ret = np.zeros((d, d), dtype=np.complex128)
    ret[ind0, ind1] = data
    return ret

def all_gellmann_matrix(d):
    symmetry = [gellmann_matrix(x,y,d) for x in range(1,d) for y in range(x)]
    antisymmetry = [gellmann_matrix(x,y,d) for x in range(d-1) for y in range(x+1,d)]
    diagonal = [gellmann_matrix(x,x,d) for x in range(d)]
    return symmetry,antisymmetry,diagonal

def test_all_gellmann_matrix():
    # https://arxiv.org/abs/1705.01523
    for d in [3,4,5]:
        sym_term,antisym_term,diagonal_term = all_gellmann_matrix(d)
        tmp0 = sym_term + antisym_term + diagonal_term[:-1]
        for ind0,x in enumerate(tmp0):
            for ind1,y in enumerate(tmp0):
                assert abs(np.trace(x @ y)-2*(ind0==ind1)) < 1e-7


def gellmann_matrix_decomposition():
    pass
