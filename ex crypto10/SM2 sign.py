import hashlib
import struct
import math
#import random
import sys


def Egcd(a, b):
    r, s, t = a, 1, 0
    r1, s1, t1 = b, 0, 1
    while r1 != 0:
        q = r//r1
        temp1, temp2, temp3 = r - q * r1, s - q * s1, t - q * t1
        r, s, t = r1, s1, t1
        r1, s1, t1 = temp1, temp2, temp3
    return r, s, t


def gcd(a, b):
    r = a
    r1 = b
    while r1 != 0:
        q = r//r1
        t = r - q*r1
        r = r1
        r1 = t
    return r


def invmod(a, n):
    if gcd(a, n) == 1:#负数？
        _, result, _ = Egcd(a, n)
    return result % n


def int2bytes(n, length):
    """将整数 n 转换为指定长度的字节数组"""
    b = bytearray()
    while n:
        b.append(n & 0xff)
        n >>= 8
    return bytes(bytearray(reversed(b)).rjust(length, b'\x00'))


def bytes2int(b):
    """将字节数组转换为整数"""
    return int.from_bytes(b, byteorder='big')


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


def double(x0, y0, p, a):#zhengquexingjianyan
    if y0 == 0:
        return [0, 0]
    else:
        #lam = ((3 * pow(x0, 2, p) + a) * invmod(2 * y0, p)) %p
        lam = ((3 * pow(x0, 2, p) + a) * pow(2 * y0, p-2, p)) % p
        x = (pow(lam, 2, p) - 2 * x0) % p
        y = (lam * (x0 - x) - y0) % p
        return [x, y]


def add(A_x, A_y, B_x, B_y, p, a):
    if A_x == B_x and (A_y + B_y) % p == 0:
        return [0, 0]
    elif A_x == B_x and (A_y - B_y) % p == 0:
        return double(A_x, A_y, p, a)
    elif A_x == 0 and A_y == 0:
        return [B_x, B_y]
    elif B_x == 0 and B_y == 0:
        return [A_x, A_y]
    else:
        #lam = ((B_y-A_y) % p) * invmod((B_x-A_x) % p, p) % p#域上？
        lam = ((B_y - A_y) % p) * pow((B_x - A_x) % p, p-2, p) % p
        x = (pow(lam, 2, p) - A_x - B_x) % p
        y = (lam * (A_x - x) - A_y) % p
        return [x, y]


def sub(A_x, A_y, B_x, B_y, p, a):
    return add(A_x, A_y, B_x, -B_y, p, a)


def multi(k, x0, y0, p, a):
    if k == 0:
        return [0, 0]
    elif k == 1:
        return [x0, y0]
    else:
        ans = [0, 0]
        k_bin = bin(k)[2:]
        for bit in k_bin:
            ans = double(ans[0], ans[1], p, a)
            if bit == '1':
                ans = add(ans[0], ans[1], x0, y0, p, a)
        return ans


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
    return bytes.fromhex(''.join(hex(x)[2:].zfill(8) for x in IV))


def sign(M, G, dA, n, k, p, a):
    M_bar = ZA + M.encode()
    e = bytes2int(sm3(M_bar))#要转整数 Hv
    r = 0
    s = 0
    #k = 0
    while r == 0 or r + k == n or s == 0:
        #k = random.randint(1, n-1)
        x1, y1 =multi(k, G[0], G[1], p, a)
        r = (e + x1) % n#返回前几步
        s = (invmod(1 + dA, n) * (k - r * dA)) % n#返回前几步
    print(r)
    print(s)

#SM3类型？
def verify(M, G, PA, r, s, n, p, a):
    if not (r >= 1 and r < n):
        sys.exit(0)
    if not (s >= 1 and s < n):
        sys.exit(0)
    #M_bar = ZA + M
    M_bar = ZA + M.encode()
    e = bytes2int(sm3(M_bar))
    t = (r + s) % n
    if t == 0:
        sys.exit(0)
    tem_point1 = multi(s, G[0], G[1], p, a)
    tem_point2 = multi(t, PA[0], PA[1], p, a)
    x1, y1 = add(tem_point1[0], tem_point1[1], tem_point2[0], tem_point2[1], p, a)
    R = (e + x1) % n
    if R == r:
        print("True")
    else:
        print("False")


p = eval(input().strip())
a = eval(input().strip())
b = eval(input().strip())
G = list(map(int, input().split(" ")))
n = eval(input().strip())
#IDA = eval('0x' + input().strip())
IDA = input().strip()
IDA = bytes2int(IDA.encode())
PA = list(map(int, input().split(" ")))
M = input().strip()
Mode = input().strip()
ENTLA = int2bytes((len(hex(IDA))-2) * 4, 2)
ZA = sm3(ENTLA + int2bytes(IDA, math.ceil(IDA.bit_length()/8)) + int2bytes(a, math.ceil(a.bit_length()/8)) + int2bytes(b, math.ceil(b.bit_length()/8)) + int2bytes(G[0], math.ceil(G[0].bit_length()/8)) + int2bytes(G[1], math.ceil(G[1].bit_length()/8)) + int2bytes(PA[0], math.ceil(PA[0].bit_length()/8)) + int2bytes(PA[1], math.ceil(PA[1].bit_length()/8)))

if Mode == 'Sign':
    dA = eval(input().strip())
    k = eval(input().strip())
    sign(M, G, dA, n, k, p, a)
elif Mode == 'Vrfy':
    r = eval(input().strip())
    s = eval(input().strip())
    verify(M, G, PA, r, s, n, p, a)



