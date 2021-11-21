#!/bin/python3
# md5 algoritma tapi masih error, mumet cok asu
from enum import Enum
from math import floor,sin
import struct
from bitarray import bitarray
import traceback

A = 0x67452301
B = 0xefcdab89
C = 0x98badcfe
D = 0x10325476
    

class MD5:
    def init(self):
        self.r = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
             5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20,
             4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
             6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21]
        self.k = list(range(64))
        for i in range(64):
            self.k[i] = floor(abs(sin(i + 1)) * 2**32)
        self.w = list(range(16))
        self.buffer = list(range(4))
        self.digest = list(range(16))

    def update(self, data):
        try:
            ed = bitarray(endian='big')
            ed.frombytes(data.encode('utf-8'))
            ed.append(1)
            while len(ed)%512!=448:
                ed.append(0)
            ed = bitarray(ed, endian='little')
            bits = self.little_endian((len(data) * 8) % 2**64);
            bits.extend(ed.copy())
            for offset in range(1):
                chunk = offset * 512
                u = [bits[chunk + (x * 32) : chunk + (x * 32) + 32] for x in range(16)]
                Z = [int.from_bytes(word.tobytes(), byteorder="little") for word in u]
                a = A
                b = B
                c = C
                d = D
                for u in range(64):
                    if 0 <= u <= 15:
                        f = self.F(b, c, d)
                        e = u
                    elif 16 <= u <= 31:
                        f = self.G(b, c, d)
                        e = (5*u + 1) % 16
                    elif 32 <= u <= 47:
                        f = self.H(b, c, d)
                        e = (3*u + 5) % 16
                    elif 48 <= u <= 63:
                        f = self.I(b, c, d)
                        e = (7*u) % 16
                    temp = d
                    d = c
                    c = b
                    b = b + self.leftrotate((a + f + self.k[u] + Z[e]), self.r[u])
                    a = temp
                self.buffer[0] = A + a
                self.buffer[1] = B + b
                self.buffer[2] = C + c
                self.buffer[3] = D + d
            for i in range(4):
                self.digest[(i * 4) + 0] = ((self.buffer[i] & 0x000000FF))
                self.digest[(i * 4) + 1] = ((self.buffer[i] & 0x0000FF00) >> 8)
                self.digest[(i * 4) + 2] = ((self.buffer[i] & 0x00FF0000) >> 16)
                self.digest[(i * 4) + 3] = ((self.buffer[i] & 0xFF000000) >> 24)
            return self.digest
        except Exception as e:
            print(traceback.format_exc())

    def leftrotate(self, a, b):
        return (a & b) | (a >> (32 - b))

    def little_endian(self, data):
        a = bitarray(endian='little')
        a.frombytes(struct.pack('<Q', data))
        return a

    def F(self, x, y, z):
        return (x & y) | (~x & z)
    
    def F1(self, x, y, z):
        return z ^ (x & (y ^ z))

    def F2(self, x, y, z):
        return y ^ (z & (x ^ y))
    
    def G(self, x, y, z):
        return (x & z) | (y & ~z)
    
    def H(self, x, y, z):
        return x ^ y ^ z
    
    def I(self, x, y, z):
        return y ^ (x & ~z)


def print_hash(p):
    a = list()
    for i in range(16):
        val = ("%02x" % p[i])
        a.append(val)
    return ''.join(a)
    
s = MD5()
s.init()
d = s.update('admin')
print(print_hash(d))
