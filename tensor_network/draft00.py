# lectures on quantum tensor networks [arxiv-link](https://arxiv.org/abs/1912.10049)
import numpy as np
import opt_einsum #same as np.einsum

hfe = lambda x,y,eps=1e-5: np.max(np.abs(x-y)/(np.abs(x)+np.abs(y)+eps))

t_hadamard = np.array([[1,1],[1,-1]])/np.sqrt(2) #symmetry index ii
t_cnot = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]], dtype=np.int_).reshape((2,2,2,2)) #ijij
t_copy3 = np.array([[[1,0],[0,0]], [[0,0],[0,1]]], dtype=np.int_) #iii
t_xor3 = np.array([[[1,0],[0,1]], [[0,1],[1,0]]], dtype=np.int_).reshape((2,2,2)) #iii
t_paulix = np.array([[0,1],[1,0]], dtype=np.int_) #ii
t_not = t_paulix
t_epsilon = np.array([[0,1],[-1,0]], dtype=np.int_)
t_pauliy = np.array([[0,-1j],[1j,0]])
t_pauliz = np.array([[1,0],[0,-1]]) #ii
t_and = np.array([[[1,1],[1,1]], [[0,0],[0,1]]], dtype=np.int_) #ijj
t_bool0 = np.array([1,0], dtype=np.int_)
t_bool1 = np.array([0,1], dtype=np.int_)
t_bool_plus = np.array([1,1])/np.sqrt(2)
t_bool_minus = np.array([1,-1])/np.sqrt(2)
t_and = np.array([[[1,1],[1,1]], [[0,0],[0,1]]], dtype=np.int_)

# more than boolean class
t_swap = np.array([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]], dtype=np.int_).reshape((2,2,2,2)) #ijji
# t_swap = np.eye(4, dtype=np.int_).reshape((2,2,2,2)).transpose(0,1,3,2)


assert all(t_copy3[x,y,z]==(1 if ((x==y) and (y==z)) else 0) for x in [0,1] for y in [0,1] for z in [0,1] if (x,y,z)) #fig-above-(eq-1.15a)
assert all(t_xor3[x,y,z]==(1 if ((x+y+z)%2==0) else 0) for x in [0,1] for y in [0,1] for z in [0,1] if (x,y,z)) #fig-above-(eq-1.16)
assert np.all(t_cnot==opt_einsum.contract(t_copy3, [0,1,2], t_xor3, [3,1,4], [0,3,2,4])) #fig-above-above-(eq-1.15a)

tmp0 = opt_einsum.contract(t_copy3, [0,1,2], t_hadamard, [0,3], t_hadamard, [1,4], t_hadamard, [2,5], [3,4,5])
assert hfe(tmp0*np.sqrt(2), t_xor3) < 1e-7 #eq-1.16
tmp0 = opt_einsum.contract(t_xor3, [0,1,2], t_hadamard, [0,3], t_hadamard, [1,4], t_hadamard, [2,5], [3,4,5])
assert hfe(tmp0/np.sqrt(2), t_copy3) #eq-1.16

tmp0 = opt_einsum.contract(t_bool0,[0],t_hadamard,[0,1],t_copy3,[1,2,3],t_bool0,[4],t_xor3,[4,3,5],[2,5])
assert hfe(tmp0*np.sqrt(2), np.eye(2)) < 1e-7 #eq-1.20
tmp0 = opt_einsum.contract(t_bool1,[0],t_hadamard,[0,1],t_copy3,[1,2,3],t_bool1,[4],t_xor3,[4,3,5],[2,5])
assert hfe(tmp0*np.sqrt(2), t_epsilon) < 1e-7 #eq-1.21

tmp0 = opt_einsum.contract(t_copy3,[0,1,2],t_xor3,[2,3,4],t_copy3,[4,5,6],t_xor3,[7,1,8],t_copy3,[8,3,9],t_xor3,[9,5,10],[0,7,6,10])
assert hfe(tmp0, t_swap) < 1e-7 #fig-above-(eq-2.1)
