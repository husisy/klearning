import functools
import numpy as np

hf2 = lambda x,y: np.kron(x,y)
hf3 = lambda x,y,z: np.kron(np.kron(x, y), z)
hf_rx = lambda x: np.array([[np.cos(x/2),-1j*np.sin(x/2)],[-1j*np.sin(x/2),np.cos(x/2)]])
hf_ry = lambda x: np.array([[np.cos(x/2),-np.sin(x/2)],[np.sin(x/2),np.cos(x/2)]])
hf_rz = lambda x: np.array([[np.cos(x/2)-1j*np.sin(x/2),0],[0,np.cos(x/2)+1j*np.sin(x/2)]])

hf_fft = lambda N0: np.exp(-2j*np.pi/N0*(np.arange(N0)[:,np.newaxis]*np.arange(N0))) / np.sqrt(N0)
hf_c = lambda x: np.block([[np.eye(2),np.zeros((2,2))],[np.zeros((2,2)),x]])
hf_swap01 = lambda x: x[np.array([0,2,1,3])[:,np.newaxis], np.array([0,2,1,3])]
hf_insert = lambda x,y: (x.reshape(2,1,2,2,1,2)*y.reshape(1,2,1,1,2,1)).reshape(8,8)
hf_circuit = lambda x: functools.reduce(np.matmul, reversed(x))
def hfe_unitary_op(op0, op1):
    tmp0 = op0 @ op1.T.conj()
    error_offdiagonal = np.abs(tmp0 - np.diag(np.diag(tmp0))).max()
    error_diagal = np.abs(np.diag(tmp0)-tmp0[0,0]).max()
    return max(error_offdiagonal,error_diagal)
hfe = lambda x,y,eps=1e-5: np.max(np.abs(x-y)/(np.abs(x)+np.abs(y)+eps))

I = np.eye(2)
I2 = np.eye(4)
CNOT = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
CNOT10 = np.array([[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,0,0]])
SWAP = np.array([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
H = np.array([[1,1],[1,-1]])/np.sqrt(2)
X = np.array([[0,1],[1,0]])
Y = np.array([[0,-1j],[1j,0]])
Z = np.array([[1,0],[0,-1]])
S = np.array([[1,0],[0,1j]])
T = np.array([[1,0],[0,(1+1j)/np.sqrt(2)]])


QFT2 = hf_circuit([
    hf2(H,I),
    hf_swap01(hf_c(S.T.conj())),
    hf2(I,H),
    SWAP,
])
fft4 = hf_fft(4)
assert hfe_unitary_op(QFT2, fft4) < 1e-10


QFT3 = hf_circuit([
    hf2(H,I2),
    hf2(hf_swap01(hf_c(S.conj())),I),
    hf_insert(hf_swap01(hf_c(T.conj())), I),
    hf3(I,H,I),
    hf2(I,hf_swap01(hf_c(S.conj()))),
    hf2(I2, H),
    hf_insert(SWAP,I),
])
fft8 = hf_fft(8)
assert hfe_unitary_op(QFT3, fft8) < 1e-10
