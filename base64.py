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

base64_encode('test')
