pt0 = ''.join([bin(ord(x))[2:].rjust(8,'0') for x in "attack at dawn"])
ct0 = bin(int('6c73d5240a948c86981bc294814d', 16))[2:].rjust(112, '0')
key = ''.join(['0' if x==y else '1' for x,y in zip(ct0,pt0)])

hfE = lambda pt: ''.join(['0' if x==y else '1' for x,y in zip(key,pt)])
hfD = lambda ct: ''.join(['0' if x==y else '1' for x,y in zip(key,ct)])
assert hfE(pt0) == ct0
assert hfD(ct0) == pt0
hfS = lambda pt: int(x,base=2)

pt1 = ''.join([bin(ord(x))[2:].rjust(8,'0') for x in "attack at dusk"])
ct1 = hfE(pt1)
hex(int(ct1, base=2))[2:]
