import numpy as np
import matplotlib.pyplot as plt
plt.ion()

# the ABC of DFT, chap5.3, table5-1
tmp0 = '''
atom atom_number E_HF E_exact E_correlation
H 1 -0.5 -0.5 0
He 2 -2.862 -2.904 -0.042
Li 3 -7.433 -7.478 -0.045
Be 4 -14.573 -14.667 -0.094
B 5 -24.529 -24.654 -0.125
C 6 -37.689 -37.845 -0.156
N 7 -54.401 -54.589 -0.188
O 8 -74.809 -75.067 -0.258
F 9 -99.409 -99.733 -0.324
Ne 10 -128.547 -128.937 -0.39
Ar 18 -526.817 -527.539 -0.722
Kr 36 -2752.055 -2753.94 -1.89
Xe 54 -7232.138 -7235.23 -3.09
Rn 86 -22866.745 -22872.5 -5.7
'''
tmp1 = [x.split() for x in tmp0.strip().split('\n')]
z0 = {
    'atom': [x[0] for x in tmp1[1:]],
    'atom_number': np.array([float(x[1]) for x in tmp1[1:]]),
    'E_HF': np.array([float(x[2]) for x in tmp1[1:]]),
    'E_exact': np.array([float(x[3]) for x in tmp1[1:]]),
    'E_correlation': np.array([float(x[4]) for x in tmp1[1:]]),
}
assert np.all(np.abs(z0['E_exact'] - (z0['E_HF']+z0['E_correlation']))<0.1)
fig,ax = plt.subplots()
ax.plot(np.log(z0['atom_number']), np.log(-z0['E_exact']), 'x', label='ln(-E_exact)')
ax.plot(np.log(z0['atom_number']), np.log(-z0['E_HF']), label='ln(-E_HF)')
ax.set_xlabel('atom number')
ax.legend()
