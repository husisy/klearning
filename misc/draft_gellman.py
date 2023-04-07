import numpy as np
import functools
import itertools
import sympy
import scipy.linalg
import sympy.physics.quantum
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


_all_gellmann_matrix_cache = dict()
def all_gellmann_matrix(d):
    d = int(d)
    assert d>=2
    if d in _all_gellmann_matrix_cache:
        ret = _all_gellmann_matrix_cache[d]
    else:
        sym_mat = [gellmann_matrix(i,j,d) for i in range(d) for j in range(i+1,d)]
        antisym_mat = [gellmann_matrix(j,i,d) for i in range(d) for j in range(i+1,d)]
        diag_mat = [gellmann_matrix(i,i,d) for i in range(1,d)]
        tmp0 = [gellmann_matrix(0, 0, d)]
        ret = np.stack(sym_mat+antisym_mat+diag_mat+tmp0, axis=0)
        _all_gellmann_matrix_cache[d] = ret
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
        all_term = all_gellmann_matrix(d)
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


def matrix_to_gellmann_basis(A):
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


def test_matrix_to_gellmann_basis():
    for N0 in [3,4,5]:
        np0 = np.random.rand(N0,N0) + np.random.rand(N0,N0)*1j
        coeff = matrix_to_gellmann_basis(np0)
        tmp0 = all_gellmann_matrix(N0)
        ret0 = sum(x*y for x,y in zip(coeff,tmp0))
        assert np.abs(np0-ret0).max()<1e-7


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
        vec = matrix_to_gellmann_basis(np0)
        np1 = gellman_basis_to_matrix(vec)
        assert np.abs(np0-np1).max() < 1e-13


def get_angular_momentum_op(j_double:int):
    # https://en.wikipedia.org/wiki/Clebsch%E2%80%93Gordan_coefficients
    assert j_double>=0
    if j_double==0:
        jx = jy = jz = np.zeros((1,1), dtype=np.float64)
    else:
        jz = np.diag((np.arange(j_double+1)[::-1]-j_double/2))
        tmp0 = np.arange(1, j_double+1)
        tmp1 = np.sqrt(tmp0 * tmp0[::-1])/2
        jx = np.diag(tmp1, 1) + np.diag(tmp1, -1)
        jy = np.diag(-1j*tmp1, 1) + np.diag(1j*tmp1, -1)
    return jx,jy,jz

levi_civita = np.zeros((3,3,3), dtype=np.int64)
levi_civita[[0,1,2],[1,2,0],[2,0,1]] = 1
levi_civita[[0,1,2],[2,0,1],[1,2,0]] = -1

def test_get_angular_momentum_op():
    for j2 in range(10):
        jx,jy,jz = get_angular_momentum_op(j2)
        jvec = jx,jy,jz
        jsquare = ((j2/2)*(j2/2+1)) * np.eye(j2+1)
        for ind0,ind1,ind2 in zip(*np.nonzero(levi_civita)):
            assert np.abs(jvec[ind0] @ jvec[ind1] - jvec[ind1] @ jvec[ind0] - 1j*levi_civita[ind0,ind1,ind2] * jvec[ind2]).max() < 1e-10
        assert np.abs(jx @ jx + jy @ jy + jz @ jz - jsquare).max() < 1e-10


@functools.lru_cache
def get_clebsch_gordan_coeffient(j1_double:int, j2_double:int):
    # https://en.wikipedia.org/wiki/Table_of_Clebsch%E2%80%93Gordan_coefficients
    assert j1_double>=0
    assert j2_double>=0
    jmax_double = j1_double + j2_double
    jmin_double = abs(j1_double - j2_double)
    j1_sym = sympy.S(j1_double)/2
    j2_sym = sympy.S(j2_double)/2
    ret = []
    for j_double in range(jmin_double, jmax_double+1, 2):
        coeff = np.zeros((j_double+1, j1_double+1, j2_double+1), dtype=np.float64)
        j_sym = sympy.S(j_double)/2
        int_shift = (j1_double+j2_double-j_double)//2
        for n in range(j_double, -1, -1):
            for n1 in range(max(0, n+int_shift-j2_double), min(j1_double, n+int_shift)+1):
                n2 = n + int_shift - n1
                tmp0 = sympy.physics.quantum.cg.CG(j1_sym, -j1_sym+n1, j2_sym, -j2_sym+n2, j_sym, -j_sym+n)
                coeff[j_double-n, j1_double-n1, j2_double-n2] = float(tmp0.doit().evalf())
        ret.append((j_double, coeff))
    return ret


def test_get_clebsch_gordan_coeffient():
    tmp0 = [(x,y) for x in range(1,5) for y in range(1,5)]
    for j1_double,j2_double in tmp0:
        # j1_double = 1
        # j2_double = 1
        j1_vec = np.stack(get_angular_momentum_op(j1_double)) #jx jy jz
        j2_vec = np.stack(get_angular_momentum_op(j2_double)) #jx jy jz
        z0 = get_clebsch_gordan_coeffient(j1_double, j2_double)
        tmp0 = [get_angular_momentum_op(x) for x,_ in z0]
        j1_vec_plus_j2_vec_new_basis = np.stack([scipy.linalg.block_diag(*x) for x in zip(*tmp0)])
        unitary = np.concatenate([x for _,x in z0], axis=0).reshape(-1, (j1_double+1)*(j2_double+1))

        tmp0 = np.eye(j2_double+1)
        tmp0 = np.einsum(j1_vec, [0,1,2], tmp0, [3,4], [0,1,3,2,4], optimize=True).reshape(3, (j1_double+1)*(j2_double+1), -1)
        tmp1 = np.eye(j1_double+1)
        tmp1 = np.einsum(tmp1, [1,2], j2_vec, [0,3,4], [0,1,3,2,4], optimize=True).reshape(3, (j1_double+1)*(j2_double+1), -1)
        j1_vec_plus_j2_vec = tmp0 + tmp1
        assert np.abs(unitary @ j1_vec_plus_j2_vec @ unitary.T - j1_vec_plus_j2_vec_new_basis).max() < 1e-10


def get_irreducible_tensor_operator(S_double:int):
    # https://en.wikipedia.org/wiki/Tensor_operator
    # https://en.wikipedia.org/wiki/Spherical_basis
    # https://doi.org/10.1006/jmre.2001.2416
    # multiplication operator http://www.physics.umd.edu/grt/taj/623d/tops2.pdf
    assert S_double>=1
    cg_coeff = get_clebsch_gordan_coeffient(S_double, S_double)
    ret = []
    for k_double,coeff in cg_coeff:
        k = k_double//2 #k=0,1,2,...,2S
        tmp0 = np.sqrt(S_double+1)*(1 if (k % 2==0) else -1) * (1 - 2*(np.arange(S_double+1) % 2))
        # q = k,k-1,...,1-k,-k
        # m,mp = S,S-1,...,1-S,S
        ret.append(tmp0[:,np.newaxis]*(coeff[:,:,::-1]))
    return ret


def test_get_irreducible_tensor_operator():
    for S_double in [1,2,3,4]:
        z0 = get_irreducible_tensor_operator(S_double)
        assert np.abs(z0[0][0] - np.eye(S_double+1)).max() < 1e-10


    jx,jy,jz = get_angular_momentum_op(1)
    T = get_irreducible_tensor_operator(1)
    # TODO strange sign
    T_jx =  (T[1][2] - T[1][0]) / (2*np.sqrt(2))
    T_jy =  (T[1][0] + T[1][2]) * (1j / (2*np.sqrt(2)))
    T_jz = - T[1][1] / 2 #TODO strange minus sign
    assert np.abs(T_jx-jx).max() < 1e-10
    assert np.abs(T_jy-jy).max() < 1e-10
    assert np.abs(T_jz-jz).max() < 1e-10


    # https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Supplemental_Modules_(Physical_and_Theoretical_Chemistry)/Spectroscopy/Magnetic_Resonance_Spectroscopies/Nuclear_Magnetic_Resonance/NMR_-_Theory/Rotations_and_Irreducible_Tensor_Operators
    for S_double in range(1, 5):
        # S_double = 3
        T = get_irreducible_tensor_operator(S_double)
        jx,jy,jz = get_angular_momentum_op(S_double)
        jplus = jx + 1j*jy
        jminus = jx - 1j*jy
        for k, T_i in enumerate(T):
            q = np.arange(k, -1-k, -1)
            assert np.abs(jz @ T_i - T_i @ jz - q.reshape(-1,1,1)*T_i).max() < 1e-10
            tmp0 = T_i @ jplus - jplus @ T_i
            if len(q)>1:
                assert np.abs(tmp0[1:] - np.sqrt(k*(k+1)-q[1:]*(q[1:]+1)).reshape(-1,1,1)*T_i[:-1]).max() < 1e-10
            assert np.abs(tmp0[0]).max() < 1e-10

            tmp0 = T_i @ jminus - jminus @ T_i
            if len(q)>1:
                assert np.abs(tmp0[:-1] - np.sqrt(k*(k+1)-q[:-1]*(q[:-1]-1)).reshape(-1,1,1)*T_i[1:]).max() < 1e-10
            assert np.abs(tmp0[-1]).max() < 1e-10


def get_irreducible_hermitian_matrix_basis(S_double:int, tag_norm=False, tag_stack=False):
    # https://doi.org/10.1006/jmre.2001.2416
    T = get_irreducible_tensor_operator(S_double)
    cx = []
    cy = []
    cz = []
    factor = np.sqrt((S_double/2)*(S_double/2+1)/3)
    for k,T_i in enumerate(T):
        q = np.arange(k,-1-k,-1)
        if k==0:
            cz.append(T_i[0] * factor)
        else:
            # q=1,2,...,k
            tmp0 = 1-2*(np.arange(1,k+1)%2)
            tmp_positive = T_i[:k][::-1] * tmp0.reshape(-1,1,1)
            tmp_negative = T_i[(k+1):]
            cx.append((tmp_negative+tmp_positive)*(factor/np.sqrt(2)))
            cy.append((tmp_negative-tmp_positive)*(1j*factor/np.sqrt(2)))
            cz.append(T_i[k]*factor)
    cx = np.concatenate(cx, axis=0)
    cy = np.concatenate(cy, axis=0)
    cz = np.stack(cz, axis=0)
    if tag_norm:
        tmp0 = 1 / np.sqrt((S_double/2)*(S_double/2+1)*(S_double+1)/3)
        cx *= tmp0
        cy *= tmp0
        cz *= tmp0
    #make identity the first term
    ret = np.concatenate([cz,cx,cy], axis=0) if tag_stack else (cz,cx,cy)
    return ret


def test_get_irreducible_hermitian_matrix_basis():
    for S_double in [1,2,3,4,5]:
        op_list = get_irreducible_hermitian_matrix_basis(S_double, tag_norm=True, tag_stack=True)
        assert np.abs(op_list - op_list.transpose(0,2,1).conj()).max() < 1e-10
        assert np.abs(op_list[0] - np.eye(S_double+1)/np.sqrt(S_double+1)).max() < 1e-10
        tmp0 = op_list.reshape(-1, (S_double+1)**2)
        assert np.abs(tmp0.conj() @ tmp0.T - np.eye((S_double+1)**2)).max() < 1e-10
