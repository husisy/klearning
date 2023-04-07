import string

def hf_decode(key, ct_list, kind='keep'):
    assert kind in {'keep', 'drop', '?'}
    if kind=='keep':
        ret = [''.join((y1 if y0 is None else hf_xor_str(y0,y1)) for y0,y1 in zip(key,x)) for x in ct_list]
    elif kind=='drop':
        ret = [''.join(hf_xor_str(y0,y1) for y0,y1 in zip(key,x) if y0 is not None) for x in ct_list]
    else:
        ret = [''.join(('?' if y0 is None else hf_xor_str(y0,y1)) for y0,y1 in zip(key,x)) for x in ct_list]
    return ret

hf_print_key = lambda key: ''.join([('?' if x is None else 'x') for x in key])


hf_hex_to_str = lambda x: ''.join([chr(int(x0,16)*16+int(x1,16)) for x0,x1 in zip(x[::2],x[1::2])])

hf_str_equal_len = lambda x,y: (x[:len(y)],y) if len(x)>len(y) else (x,y[:len(x)])
hf_xor_str = lambda x0,x1: ''.join(chr(ord(y0)^ord(y1)) for y0,y1 in zip(x0,x1))

''.join([chr(ord(x)^ord(' ')) for x in string.ascii_uppercase])
''.join([chr(ord(x)^ord(' ')) for x in string.ascii_lowercase])



with open('data/cyphertext00.txt', 'r') as fid:
    tmp0 = fid.read().strip().split('\n')
    cyphertext_list = [x[:len(tmp0[-1])] for x in tmp0]
    ct_ascii_list = [hf_hex_to_str(x) for x in cyphertext_list]

valid_str = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,. !?\.')
accept_str = set(string.printable[:-3])

z0 = [[hf_xor_str(x,y) for y in ct_ascii_list if y!=x] for x in ct_ascii_list]
key_list = [None]*len(ct_ascii_list[0])
space_list = [['0']*len(ct_ascii_list[0]) for _ in range(len(ct_ascii_list))]
for ind0,str_i_list in enumerate(z0):
    for ind1 in range(len(ct_ascii_list[0])):
        tmp0 = ''.join(x[ind1] for x in str_i_list)
        if set(tmp0)<=valid_str:
            space_list[ind0][ind1] = '1'
            old_key = key_list[ind1]
            assert key_list[ind1]==None
            key_list[ind1] = hf_xor_str(' ', ct_ascii_list[ind0][ind1])

assert {y for x in hf_decode(key_list, ct_ascii_list, kind='drop') for y in x}<=valid_str

def hf_guess(ind0, ind1, str_i):
    key_list[ind1] = hf_xor_str(str_i, ct_ascii_list[ind0][ind1])

# hf_guess(9, 2, 'h')
# hf_guess(0, 3, 'c')
# hf_guess(0, 5, 'n')
# hf_guess(0, 6, ' ')
# hf_guess(10, 13, 's')
# hf_guess(10, 14, 's')
# hf_guess(10, 17, 'e')
# hf_guess(8, 7, 'a')
# hf_guess(8, 9, 'e')
# hf_guess(10, 10, ' ')
# hf_guess(2, 19, 't')
# # number
# hf_guess(0, 20, 'm')
# hf_guess(0, 21, 'b')
# hf_guess(0, 22, 'e')
# hf_guess(0, 23, 'r')
# # OxfordDictionary
# hf_guess(9, 25, 'n')
# hf_guess(9, 26, 'a')
# hf_guess(9, 27, 'r')
# hf_guess(9, 28, 'y')
# # cryptog??????? cryptography
# hf_guess(5, 30, 'r')
# hf_guess(5, 31, 'a')
# hf_guess(5, 32, 'p')
# hf_guess(5, 33, 'h')
# hf_guess(5, 34, 'y')
# # qu??t??? quantum
# hf_guess(0, 35, 'a')
# hf_guess(0, 36, 'n')
# hf_guess(0, 38, 'u')
# hf_guess(0, 39, 'm')
# hf_guess(0, 40, ' ')
# hf_guess(0, 41, 'c')
# hf_guess(0, 42, 'o')
# hf_guess(0, 44, 'p')
# hf_guess(0, 46, 't')
# # algo???h??? algorithm
# hf_guess(3, 49, 'r')
# hf_guess(3, 50, 'i')
# hf_guess(3, 51, 't')
# hf_guess(3, 53, 'm')
# # never use the key more than once
# hf_guess(10, 54, 'e')
# hf_guess(10, 55, 'r')
# hf_guess(10, 56, ' ')
# hf_guess(10, 57, 'u')
# hf_guess(10, 58, 's')
# hf_guess(10, 59, 'e')
# hf_guess(10, 60, ' ')
# hf_guess(10, 63, 'e')
# hf_guess(10, 64, ' ')
# hf_guess(10, 66, 'e')
# hf_guess(10, 68, ' ')
# hf_guess(10, 69, 'm')
# hf_guess(10, 70, 'o')
# hf_guess(10, 71, 'r')
# hf_guess(10, 72, 'e')
# hf_guess(10, 73, ' ')
# hf_guess(10, 74, 't')
# hf_guess(10, 74, 't')
# hf_guess(10, 78, ' ')
# hf_guess(10, 79, 'o')
# hf_guess(10, 81, 'c')
# hf_guess(10, 82, 'e')

index_str = '#####' + ''.join([str(x%10) for x in range(len(key_list))]) + '###'

for test0 in accept_str:
    index = 57
    hf_guess(0, index, test0)

    pt_list = hf_decode(key_list, ct_ascii_list, kind='?')
    print(f'\n{test0}####{hf_print_key(key_list)}###')
    print(index_str)
    for i,x in enumerate(pt_list):
        print(f'{i:2}###{x}###')

    tag = {y for x in pt_list for y in x}<=accept_str
    if not ({x[index] for x in pt_list} <= accept_str):
        continue
    tmp0 = input('type q to quit:').strip()
    if tmp0=='q':
        break

