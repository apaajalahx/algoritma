#!/bin/python3
# belajar bg
import codecs

M = 256
KEY = 'jancok12337'

def rc4(key, length):
    key = [ord(k) for k in key]
    # create list from range
    S = list(range(M))
    j = 0
    for i in range(M):
        j = (j + S[i] + key[i % length]) % M
        S[i], S[j] = S[j], S[i]
    return S

def pseudoRandom(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % M
        j = (j + S[i]) % M
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % M]
        yield K
        
def keyStream(key):
    s = rc4(key, len(key))
    return pseudoRandom(s)

def encrypt(key, text):
    s = keyStream(key)
    res = []
    for d in text:
        val = ("%02X" % (d ^ next(s)))
        res.append(val)
    return ''.join(res)

def decrypt(key, ciphertext):
    ciphertext = codecs.decode(ciphertext, 'hex_codec')
    res = encrypt(key, ciphertext)
    return codecs.decode(res, 'hex_codec').decode('utf-8')

text= 'KONTOLNJEPAT'
hexs = encrypt(KEY, [ord(u) for u in text])
print(hexs)
decode = decrypt(KEY, hexs)
print(decode)
