'''import struct


def rotate_left(x, n):
    return ((x << n) & 0xffffffff) | (x >> (32 - n))


def pad_data(data):
    bit_length = len(data) * 8
    data += b'\x80'
    while (len(data) + 8) % 64 != 0:
        data += b'\x00'
    data += struct.pack('>Q', bit_length)
    return data#类型


def P0():
    #0 9 15


def FF(X, Y, Z, j):
    if j >= 0 and j <= 15:
        #X & Y & Z
    else:
        #(X & Y) | (Z & Y) | (Z & X)


def GG(X, Y, Z, j):
    if j >= 0 and j <= 15:
        #X & Y & Z
    else:
        #(X & Y) | (Z & ~X)


def CF(V, Bi):
    A, B, C, D, E, F, G, H = V[0: 8], V[8: 16], V[16: 24], V[24: 32], V[32: 40], V[40: 48], V[48: 56], V[56: 64]
    for j in range(64):#roatate类型转换
        if j >= 0 and j <= 15:
            T = 0x79cc4519
        else:
            T = 0x7a879d8a
        SS1 = rotate_left(rotate_left(A, 12) + E +rotate_left(T, j % 32), 7)
        SS2 = bytes(a ^ b for a, b in zip(SS1, i_pad))
        TT1 = FFj(A, B, C) + D + SS2 + #W?
        D = C
        C = rotate_left(B, 9)
        B = A
        A = TT1
        H = G
        G = rotate_left(F, 19)
        F = E
        E = P0#
    return bytes(a ^ b for a, b in zip(A + B + C + D + E + F + G + H, V))


def SM3(M):
    M = pad_data(M)
    n = len(M) // 64
    V = 0x7380166f4914b2b9172442d7da8a0600a96f30bc163138aae38dee4db0fb0e4e
    V = struct.pack('>Q', )
    for i in range(n):
        V = CF(V, M[64 * i: 64 * i + 64])'''
'''import hashlib


def sm3_msg_expand(Bi):
    W = [int.from_bytes(Bi[i:i+4], 'big') for i in range(0, 64, 4)]
    W_ = W.copy()
    for i in range(16, 68):
        tmp = W_[i-16] ^ W_[i-9] ^ ((W_[i-3] << 15 | W_[i-3] >> 17) & 0xffffffff)
        tmp ^= ((tmp << 1 | tmp >> 31) & 0xffffffff) ^ ((tmp << 8 | tmp >> 24) & 0xffffffff)
        W_.append(tmp ^ W_[i-13] ^ ((W_[i-6] << 7 | W_[i-6] >> 25) & 0xffffffff))
    return W_


def sm3_compress(iv, Bi):
    # Step 1: Initialize working variables
    A, B, C, D, E, F, G, H = iv

    # Step 2: Perform 64 rounds of compression
    W_ = sm3_msg_expand(Bi)
    for i in range(64):
        if i <= 15:
            T = ((A << 12 | A >> 20) & 0xffffffff) + E + 0x79cc4519
        else:
            T = ((A << 12 | A >> 20) & 0xffffffff) + E + 0x7a879d8a
        T += (((B << 27 | B >> 5) & 0xffffffff) ^ ((C << 22 | C >> 10) & 0xffffffff) ^ ((D << 7 | D >> 25)) & 0xffffffff) + W_[i]
        TT = (((F << 12 | F >> 20) & 0xffffffff) + ((T << 7 | T >> 25) & 0xffffffff)) ^ ((F & G) ^ (~F & H))
        EE = D
        DD = C
        CC = (B << 9 | B >> 23) & 0xffffffff
        BB = A
        AA = TT
        E = AA
        F = BB
        G = CC
        H = DD
        D = EE
        A = TT

    # Step 3: Update IV
    new_iv = [(iv[j] + x) & 0xffffffff for j, x in enumerate([A, B, C, D, E, F, G, H])]

    # Step 4: Return new IV
    return new_iv


def sm3(data):
    # Step 1: Initialize IV
    iv = [0x7380166f, 0x4914b2b9, 0x172442d7, 0xda8a0600,
          0xa96f30bc, 0x163138aa, 0xe38dee4d, 0xb0fb0e4e]

    # Step 2: Pad message
    msg = data.encode('utf-8')
    pad_len = (64 - len(msg) % 64) % 64
    padding = b'\x80' + b'\x00' * (pad_len - 1)
    length_bits = (8 * len(msg)).to_bytes(8, 'big')
    padded_msg = msg + padding + length_bits

    # Step 3: Compress message in blocks of 512 bits
    for i in range(0, len(padded_msg), 64):
        block = padded_msg[i:i+64]
        iv = sm3_compress(iv, block)

    # Step 4: Convert IV to bytes and return as hash digest
    digest = b''.join([x.to_bytes(4, 'big') for x in iv])
    return hashlib.new('sm3', digest).hexdigest()'''

'''else:
    print('f4051d239b766c4111e92979aa31af0b35def053646e347bc41e8b73cfd080bc')
'''
#1ab21d8355cfa17f8e61194831e81a8f22bec8c728fefb747ed035eb5082aa2b
#1AB21D8355CFA17F8E61194831E81A8F22BEC8C728FEFB747ED035EB5082AA2B

from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
import struct


def rotate_left(x, n):
    return ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF


def P0(X):
    return (X ^ rotate_left(X, 9) ^ rotate_left(X, 17)) & 0xffffffff


def P1(X):
    return (X ^ rotate_left(X, 15) ^ rotate_left(X, 23)) & 0xffffffff


def FF(X, Y, Z, j):
    if j >= 0 and j <= 15:
        #return X  Y & Z
        return X ^ Y ^ Z
    else:
        return (X & Y) | (X & Z) | (Y & Z)


def GG(X, Y, Z, j):
    if j >= 0 and j <= 15:
        return X ^ Y ^ Z
    else:
        return (X & Y) | (Z & ~X)


def from_bytes(b):
    """将字节数组转换为整数"""
    return int.from_bytes(b, byteorder='big')


def sm3(message):
    # 初始化常量
    IV = [
        0x7380166f,
        0x4914b2b9,
        0x172442d7,
        0xda8a0600,
        0xa96f30bc,
        0x163138aa,
        0xe38dee4d,
        0xb0fb0e4e
    ]
    #print(hex(from_bytes(message)))
    # 填充消息
    msg_len = len(message)
    message += b'\x80'
    while len(message) % 64 != 56:
        message += b'\x00'
    message += struct.pack('>Q', msg_len * 8)
    #print(hex(from_bytes(message)))

    blocks = [message[i:i + 64] for i in range(0, len(message), 64)]

    for block in blocks:
        w = [0] * 68
        v = IV[:]
        for i in range(16):
            w[i] = struct.unpack('>I', block[i * 4:i * 4 + 4])[0]
            #print(hex(from_bytes(w[i])))

            #print(hex(w[i]))
        for i in range(16, 68):#这里错了
            #w[i] = rotate_left(w[i - 16] ^ w[i - 9] ^ rotate_left(w[i - 3], 15), 1) ^ rotate_left(w[i - 13], 7) ^ w[i - 6]
            w[i] = P1(w[i - 16] ^ w[i - 9] ^ rotate_left(w[i - 3], 15)) ^ rotate_left(w[i - 13], 7) ^ w[i - 6]
            #print(hex(w[i]))#改对
        w_ = [0] * 64

        i = 0
        for i in range(64):
            w_[i] = w[i] ^ w[i+4]
        #print(hex(w_[i]))#正确
        A, B, C, D, E, F, G, H = v
        #for i in range(68):
        for i in range(64):
            #第一轮就不一样？ + ^ 错误的a e TT1 TT2
            #print(hex(A), hex(B), hex(C), hex(D), hex(E), hex(F), hex(G), hex(H), sep=' ')
            if i >= 0 and i <= 15:
                #ss1 = rotate_left(rotate_left(A, 12) + E + rotate_left(0x79cc4519, i % 32), 7)
                ss1 = rotate_left((rotate_left(A, 12) + E + rotate_left(0x79cc4519, i % 32)) & 0xffffffff, 7)
            else:
                #ss1 = rotate_left(rotate_left(A, 12) + E + rotate_left(0x7a879d8a, i % 32), 7)
                ss1 = rotate_left((rotate_left(A, 12) + E + rotate_left(0x7a879d8a, i % 32)) & 0xffffffff, 7)
            ss2 = ss1 ^ rotate_left(A, 12)
            '''tt1 = (0x7a879d8a if i < 16 else 0x13198a2e if i < 64 else 0x243185be) + i
            tt2 = (0xaaaaaaaa if i < 16 else 0x55555555 if i < 64 else 0x9b05688c) ^ tt1
            tmp = (rotate_left(a, 12) + ss1 + (tt2 & 0xFFFFFFFF) + (w[i] & 0xFFFFFFFF) & 0xFFFFFFFF)
            tmp = (rotate_left(tmp, 7) + ss2) & 0xFFFFFFFF
            a, b, c, d, e, f, g, h = (tmp ^ rotate_left(b, 9) ^ rotate_left(c, 19), a, rotate_left(b, 10), c, d, e, f, g)
'''
            #TT1 = FF(A, B, C, i) + D + ss2 + w_[i] i = 1时E
            TT1 = (FF(A, B, C, i) + D + ss2 + w_[i]) & 0xffffffff
            #TT2 = GG(E, F, G, i) + H + ss1 + w[i]
            TT2 = (GG(E, F, G, i) + H + ss1 + w[i]) & 0xffffffff
            D = C
            C = (B << 9 | B >> 23) & 0xffffffff
            B = A
            A = TT1
            H = G
            G = rotate_left(F, 19)
            F = E
            E = P0(TT2)
        # 更新中间值
        #都对print(hex(A), hex(B), hex(C), hex(D), hex(E), hex(F), hex(G), hex(H), sep=' ')
        #IV = [(x + y) & 0xFFFFFFFF for x, y in zip(v, [a, b, c, d, e, f, g, h])]
        #IV = [(x + y) & 0xFFFFFFFF for x, y in zip(v, [A, B, C, D, E, F, G, H])]
        IV = [(x ^ y) & 0xFFFFFFFF for x, y in zip(v, [A, B, C, D, E, F, G, H])]
    # 返回摘要结果
    return ''.join(hex(x)[2:].zfill(8) for x in IV)


#M = input().strip()
def main():
    M = input()
    #if M != '':
    M = M.encode('utf-8')
    print(sm3(M))

if __name__ == '__main__':
    with PyCallGraph(output=GraphvizOutput()):
        main()