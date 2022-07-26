import numpy as np
import itertools
import torch


np_rng = np.random.default_rng()

def gellmann_matrix(i, j, d):
    # https://en.wikipedia.org/wiki/Gell-Mann_matrices
    # https://en.wikipedia.org/wiki/Generalizations_of_Pauli_matrices
    # https://github.com/CQuIC/pysme/blob/master/src/pysme/gellmann.py
    # https://arxiv.org/pdf/0806.1174.pdf
    assert (d>0) and (0<=i<d) and (0<=j<d)
    if i > j:
        ind0 = [i, j]
        ind1 = [j, i]
        data = [1j, -1j]
    elif j > i:
        ind0 = [i, j]
        ind1 = [j, i]
        data = [1, 1]
    elif i==j and i==0:
        ind0 = np.arange(d)
        ind1 = ind0
        data = np.ones(d)
    else:
        ind0 = np.arange(i+1)
        ind1 = ind0
        data = np.sqrt(2/(i*(i+1)))*np.array([1]*i + [-i])
    ret = np.zeros((d, d), dtype=np.complex128)
    ret[ind0, ind1] = data
    return ret


_all_gellman_matrix_cache = dict()
def all_gellman_matrix(d):
    d = int(d)
    assert d>=2
    if d in _all_gellman_matrix_cache:
        ret = _all_gellman_matrix_cache[d]
    else:
        ret = np.stack([gellmann_matrix(i,j,d) for i in range(d) for j in range(d)][1:])
        _all_gellman_matrix_cache[d] = ret
    return ret


_gellman_matrix_structure_factor = dict()
def gellman_matrix_structure_factor(d):
    # https://math.stackexchange.com/a/3172748
    d = int(d)
    assert d>=2
    if d in _gellman_matrix_structure_factor:
        ret = _gellman_matrix_structure_factor[d]
    else:
        all_gm = [gellmann_matrix(i,j,d) for i in range(d) for j in range(d)][1:]
        hf_trace = lambda x,y: np.dot(x.T.reshape(-1), y.reshape(-1))
        sym_factor = []
        antisym_factor = []
        for j,k in itertools.product(range(d**2-1), range(d**2-1)):
            tmp0 = all_gm[j] @ all_gm[k] + all_gm[k] @ all_gm[j]
            sym_factor.append([hf_trace(all_gm[i],tmp0).real/4 for i in range(d**2-1)])
            tmp0 = all_gm[j] @ all_gm[k] - all_gm[k] @ all_gm[j]
            antisym_factor.append([hf_trace(all_gm[i],tmp0).imag*0.25 for i in range(d**2-1)])
        sym_factor = np.array(list(zip(*sym_factor)), dtype=np.float64).reshape(d**2-1, d**2-1, d**2-1)
        antisym_factor = np.array(list(zip(*antisym_factor)), dtype=np.float64).reshape(d**2-1, d**2-1, d**2-1)
        ret = sym_factor,antisym_factor
        _gellman_matrix_structure_factor[d] = ret
    return ret


def test_all_gellmann_matrix():
    # https://arxiv.org/abs/1705.01523
    for d in [3,4,5]:
        all_term = all_gellman_matrix(d)
        for ind0,x in enumerate(all_term):
            for ind1,y in enumerate(all_term):
                assert abs(np.trace(x @ y)-2*(ind0==ind1)) < 1e-7


def test_gellman_matrix_structure_factor():
    for d in range(2, 5):
        sym_factor, antisym_factor = gellman_matrix_structure_factor(d)
        all_gm = [gellmann_matrix(i,j,d) for i in range(d) for j in range(d)][1:]
        for i,j in itertools.product(range(d**2-1), range(d**2-1)):
            tmp0 = all_gm[i] @ all_gm[j] - all_gm[j] @ all_gm[i]
            tmp1 = 2j * sum(x*y for x,y in zip(antisym_factor[i,j], all_gm))
            assert np.abs(tmp0-tmp1).max() < 1e-7
            tmp0 = all_gm[i] @ all_gm[j] + all_gm[j] @ all_gm[i]
            tmp1 = (4*(i==j)/(d))*np.eye(d) + 2*sum(x*y for x,y in zip(sym_factor[i,j], all_gm))
            assert np.abs(tmp0-tmp1).max() < 1e-7
        # Fierz completeness relation
        tmp0 = sum([x.reshape(d,d,1,1)*x for x in all_gm]) / 2
        tmp1 = np.eye(d).reshape(d,1,1,d) * np.eye(d).reshape(1,d,d,1) - np.eye(d).reshape(d,d,1,1)*(np.eye(d)/d)
        assert np.abs(tmp0-tmp1).max() < 1e-7


def matrix_to_gellman_basis(A):
    shape0 = A.shape
    N0 = shape0[-1]
    assert len(shape0)>=2 and shape0[-2]==N0
    A = A.reshape(-1,N0,N0)
    if isinstance(A, torch.Tensor):
        indU0,indU1 = torch.triu_indices(N0, N0, offset=1)
        aS = (A + A.transpose(1,2))[:,indU0,indU1]/2
        aA = (A - A.transpose(1,2))[:,indU0,indU1] * (0.5j)
        tmp0 = torch.diagonal(A, dim1=1, dim2=2)
        tmp1 = torch.sqrt(2*torch.arange(1,N0,dtype=torch.float64)*torch.arange(2,N0+1))
        aD = (torch.cumsum(tmp0,dim=1)[:,:-1] - torch.arange(1,N0)*tmp0[:,1:])/tmp1
        aI = torch.einsum(A, [0,1,1], [0]) / N0
        ret = torch.concat([aS,aA,aD,aI.view(-1,1)], dim=1)
    else:
        indU0,indU1 = np.triu_indices(N0,1)
        aS = (A + A.transpose(0,2,1))[:,indU0,indU1]/2
        aA = (A - A.transpose(0,2,1))[:,indU0,indU1] * (0.5j)
        tmp0 = np.diagonal(A, axis1=1, axis2=2)
        tmp1 = np.sqrt(2*np.arange(1,N0)*np.arange(2,N0+1))
        aD = (np.cumsum(tmp0,axis=1)[:,:-1] - np.arange(1,N0)*tmp0[:,1:])/tmp1
        aI = np.trace(A, axis1=1, axis2=2) / N0
        ret = np.concatenate([aS,aA,aD,aI[:,np.newaxis]], axis=1)
    if len(shape0)==2:
        ret = ret[0]
    else:
        ret = ret.reshape(*shape0[:-2], -1)
    return ret


def test_matrix_to_gellman_basis():
    for d in range(2, 6):
        np0 = np_rng.normal(size=(d,d)) + 1j*np_rng.normal(size=(d,d))
        vec = matrix_to_gellman_basis(np0)
        gmS = [gellmann_matrix(i,j,d) for i in range(d) for j in range(i+1,d)]
        gmA = [gellmann_matrix(j,i,d) for i in range(d) for j in range(i+1,d)]
        tmp0 = [gellmann_matrix(i,i,d) for i in range(d)]
        gmD = tmp0[1:]
        gmI = [tmp0[0]]
        tmp0 = gmS + gmA + gmD + gmI
        tmp1 = sum(x*y for x,y in zip(vec,tmp0))
        assert np.abs(np0-tmp1).max() < 1e-13


def gellman_basis_to_matrix(vec):
    # TODO torch
    # TODO batch
    N0 = int(np.sqrt(vec.shape[0]))
    N1 = N0*(N0-1)//2
    assert vec.shape==(N0*N0,)
    ret = np.zeros((N0,N0), dtype=np.complex128)
    indU0,indU1 = np.triu_indices(N0,1)
    indL0,indL1 = np.tril_indices(N0,-1)
    ind0 = np.arange(N0, dtype=np.int64)
    ret[indU0,indU1] = vec[:N1] - 1j*vec[N1:(2*N1)]
    tmp0 = np.zeros_like(ret)
    tmp0[indU0,indU1] = vec[:N1] + 1j*vec[N1:(2*N1)]
    ret += tmp0.T
    # ret[indL0,indL1] = vec[:N1] + 1j*vec[N1:(2*N1)] #not equivalent
    tmp1 = np.concatenate([np.sqrt(2/(ind0[1:]*(ind0[1:]+1)))*vec[(2*N1):-1], vec[-1:]], axis=0)
    ret[ind0,ind0] = ((ind0[:,np.newaxis]<=ind0) + np.diag(-ind0[1:], k=-1)) @ tmp1
    return ret


def test_gellman_basis_to_matrix():
    for d in range(2, 6):
        np0 = np_rng.normal(size=(d,d)) + 1j*np_rng.normal(size=(d,d))
        vec = matrix_to_gellman_basis(np0)
        np1 = gellman_basis_to_matrix(vec)
        assert np.abs(np0-np1).max() < 1e-13
