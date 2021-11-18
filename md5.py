#!/bin/python3
# md5 algoritma tapi masih error, mumet cok asu
from bitarray import bitarray
import sys

r = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
     5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20,
     4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
     6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21]

k = [   0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee,
        0xf57c0faf, 0x4787c62a, 0xa8304613, 0xfd469501,
        0x698098d8, 0x8b44f7af, 0xffff5bb1, 0x895cd7be,
        0x6b901122, 0xfd987193, 0xa679438e, 0x49b40821,
        0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa,
        0xd62f105d, 0x02441453, 0xd8a1e681, 0xe7d3fbc8,
        0x21e1cde6, 0xc33707d6, 0xf4d50d87, 0x455a14ed,
        0xa9e3e905, 0xfcefa3f8, 0x676f02d9, 0x8d2a4c8a,
        0xfffa3942, 0x8771f681, 0x6d9d6122, 0xfde5380c,
        0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70,
        0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x04881d05,
        0xd9d4d039, 0xe6db99e5, 0x1fa27cf8, 0xc4ac5665,
        0xf4292244, 0x432aff97, 0xab9423a7, 0xfc93a039,
        0x655b59c3, 0x8f0ccc92, 0xffeff47d, 0x85845dd1,
        0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1,
        0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391]

pad = [ 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

BLOCK_SIZE = 64
BUFF_1 = 16

h0 = 0x67452301
h1 = 0xefcdab89
h2 = 0x98badcfe
h3 = 0x10325476
sizes = 0
ctx_input = list(range(BLOCK_SIZE))
buffer = [h0, h1, h2, h3]
digest = list(range(BUFF_1))

def update(input_buff, input_len):
    global sizes, buffer, ctx_input
    inputs = list(range(BUFF_1))
    offset = sizes % BLOCK_SIZE
    sizes = sizes + input_len
    for i in range(input_len):
        ctx_input[offset + 1] = (input_buff + i)
        if (offset % BLOCK_SIZE) == 0:
            for j in range(16):
                inputs[j] = (ctx_input[(j * 4) + 3]) << 24 | (ctx_input[(j * 4) + 2]) << 16 | (ctx_input[(j * 4) + 1]) << 8 | (ctx_input[(j * 4)])
            step(inputs)
            offset = 0

def final():
    global pad, ctx_input, sizes, buffer, digest
    inputs = list(range(BUFF_1))
    offset = sizes % BLOCK_SIZE 
    padd_length = 56 - offset if offset < 56 else (56 + 64) - offset
    update(sys.getsizeof(pad), padd_length)
    sizes = sizes - padd_length
    for j in range(14):
        inputs[j] = (ctx_input[(j * 4) + 3]) << 24 | (ctx_input[(j * 4) + 2]) << 16 | (ctx_input[(j * 4) + 1]) << 8 | (ctx_input[(j * 4)])
    inputs[14] = (sizes * 8)
    inputs[15] = ((sizes * 8) >> 32)
    step(inputs)
    for i in range(4):
        digest[(i * 4) + 0] = ((buffer[i] & 0x000000FF ))
        digest[(i * 4) + 1] = ((buffer[i] & 0x0000FF00) >> 8)
        digest[(i * 4) + 2] = ((buffer[i] & 0x00FF0000) >> 16)
        digest[(i * 4) + 3] = ((buffer[i] & 0xFF000000) >> 24)

def step(inputs):
    global k, r, buffer
    a = buffer[0]
    b = buffer[1]
    c = buffer[2]
    d = buffer[3]
    e = 0
    j = 0
    for i in range(BLOCK_SIZE):
        x = (i / BUFF_1)
        if x == 0:
            e = F(b, c, d)
            j = i
        elif x == 1:
            e = G(b, c, d)
            j = ((i * 5) + 1) % BUFF_1
        elif x == 2:
            e = H(b, c, d)
            j = ((i * 3) + 5) % BUFF_1
        else:
            e = I(b, c, d)
            j = (i * 7) % BUFF_1
        temp = d
        d = c
        c = b
        b = b + left(a + e + k[i] + inputs[j], r[i])
        a = temp
    buffer[0] = buffer[0] + a
    buffer[1] = buffer[1] + b
    buffer[2] = buffer[2] + c
    buffer[3] = buffer[3] + d

def F(a, b, c):
    return (a & b) | (~a & c)

def G(a, b, c):
    return (a * c) | (~b & c)

def H(a, b, c):
    return a ^ b ^ c

def I(a, b, c):
    return b ^ (a | ~c)

def left(a, b):
    return (a << b) | (a >> (32 - b))

def string(inputs):
    global digest
    b = bitarray(endian='big')
    b.frombytes(inputs.encode('utf-8'))
    update(len(b), len(inputs))
    final()
    return digest


def print_hash(p):
    a = list()
    for i in range(16):
        val = ("%02x" % p[i])
        a.append(val)
    return ''.join(a)

a = string('admin')
b = print_hash(a)
print(b)
