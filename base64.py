#!/bin/python3

table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
def base64_encode(data):
    d = str()
    for z in data:
        d += bin(int('0x' + z.encode('utf-8').hex(), 0)).replace('b','')
    while len(d) % 3:
        d += '00000000'
    for z in range(6, len(d) + int(len(d)/6), 7):
        d = d[:z] + "|" + d[z:]
    d = d.split('|')
    z = ''
    for u in d:
        if u == '000000':
            z += '='
        else:
            if u != '':
                z += table[int(u, 2)]
    return z

def base64_decode(data):
    d = str()
    for z in data:
        if z == '=':
            break; continue
        d += '{:0>6}'.format(bin(table.index(z)).replace('0b',''))
    for z in range(8, len(d) + int(len(d)/8), 9):
        d = d[:z] + '|' + d[z:]
    u = str()
    for z in d.split('|'):
        if z != '':
            if not len(z) < 6:
                u += chr(int(z, 2))
    return u


def test():
    t1 = 'admin'
    t1_enc = base64_encode(t1)
    print(t1_enc)
    t2_dec = base64_decode(t1_enc)
    if t2_dec == t1:
        print('OK')

test()
