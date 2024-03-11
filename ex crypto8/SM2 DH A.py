import hashlib
import math
import sys


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


def sha256(m):#sha1 #L不是空时怎么处理？ 输出32个字节
    """sha1 哈希函数"""
    return hashlib.sha256(m).digest()


def point2bytes(P, p):#q是什么 l
    l = math.ceil(math.log(p, 2)/8)
    X1 = int2bytes(P[0], l)
    Y1 = int2bytes(P[1], l)
    PC = b'\x04'
    S = PC + X1 + Y1
    return S


def bytes2point(S, p):
    l = math.ceil(math.log(p, 2) / 8)
    yP = bytes2int(S[l + 1: 2 * l + 1])
    xP = bytes2int(S[1:l + 1])
    return [xP, yP]


def KDF(Z, klen):
    ct = 0x00000001
    v = b''
    klen_byte = (klen + 7) // 8
    for i in range((klen + 255) // 256):
        md = hashlib.sha256()
        md.update(Z)
        md.update(ct.to_bytes(length=4, byteorder='big'))
        v += md.digest()
        ct += 1
    return v[:klen_byte]


p = eval(input().strip())
a = eval(input().strip())
b = eval(input().strip())
G = list(map(int, input().split(" ")))
n = eval(input().strip())
IDA = eval('0x' + input().strip())
IDB = eval('0x' + input().strip())
d = eval(input().strip())
PA = list(map(int, input().split(" ")))
PB = list(map(int, input().split(" ")))
r = eval(input().strip())
#R = list(map(int, input().split(" ")))
#R = list(map(int, input().split(" ")))
#Z
h = 1
klen = 128
#ENTLA = int2bytes(IDA.bit_length(), 2)
ENTLA = int2bytes((len(hex(IDA))-2) * 4, 2)
#print(hex(bytes2int(ENTLA)))

#ENTLB = int2bytes(IDB.bit_length(), 2)
ENTLB = int2bytes((len(hex(IDB))-2) * 4, 2)
#print(hex(bytes2int(ENTLB)))
ZA = sha256(ENTLA + int2bytes(IDA, math.ceil(IDA.bit_length()/8)) + int2bytes(a, math.ceil(a.bit_length()/8)) + int2bytes(b, math.ceil(b.bit_length()/8)) + int2bytes(G[0], math.ceil(G[0].bit_length()/8)) + int2bytes(G[1], math.ceil(G[1].bit_length()/8)) + int2bytes(PA[0], math.ceil(PA[0].bit_length()/8)) + int2bytes(PA[1], math.ceil(PA[1].bit_length()/8)))
ZB = sha256(ENTLB + int2bytes(IDB, math.ceil(IDB.bit_length()/8)) + int2bytes(a, math.ceil(a.bit_length()/8)) + int2bytes(b, math.ceil(b.bit_length()/8)) + int2bytes(G[0], math.ceil(G[0].bit_length()/8)) + int2bytes(G[1], math.ceil(G[1].bit_length()/8)) + int2bytes(PB[0], math.ceil(PB[0].bit_length()/8)) + int2bytes(PB[1], math.ceil(PB[1].bit_length()/8)))
w = math.ceil(math.ceil(math.log(n, 2))/2)-1
l = math.ceil(n.bit_length()/8)
RA = multi(r, G[0], G[1], p, a)
with open('shared.txt', 'w') as file:
    file.write(str(RA))#A写 B读 不读自己写的
x1 = RA[0]
y1 = RA[1]
x1_bar = pow(2, w) + (x1 & ((1 << w) - 1))
tA = (d + x1_bar * r) % n
#验证rB
with open('shared.txt', 'r+') as file:
    while True:
        '''R = file.readline()#']\n'什么情况
        print(R)
        if len(R) != 0 and R != '' and '[' in R and ']' in R:
            T = file.readline()
            if len(T) == 0:
                continue
            R = eval(R)
            #SB = eval(file.readline())
            SB = eval(T)
            file.truncate(0)
            break'''
        file.seek(0)
        R = file.readlines()
        if len(R) == 2:
            SB = eval(R[1])
            R = eval(R[0])
            #print(SB, R, sep=' ')
            file.truncate(0)
            break
        '''line_count = 0
        R = []
        for line in file:
            R.append(line)
            line_count += 1

        if line_count == 2:
            #R = file.readline().strip()
            #SB = file.readline().strip()
            print(R[0], R[1], sep=' ')
            #R = eval(R)
            SB = eval(R[1])#见鬼 就读进一个中括号
            R = eval(R[0])
            break'''


if pow(R[1], 2, p) != (pow(R[0], 3, p) + (a * R[0]) % p + b) % p:
    print("RA error")
    sys.exit(1)

x2 = R[0]
y2 = R[1]
x2_bar = pow(2, w) + (x2 & ((1 << w) - 1))
factor = add(PB[0], PB[1], multi(x2_bar, R[0], R[1], p, a)[0], multi(x2_bar, R[0], R[1], p, a)[1], p, a)
U = multi(h * tA, factor[0], factor[1], p, a)
#bytes_xU = int2bytes(U[0], l)
#bytes_yU = int2bytes(U[1], l)
bytes_xU = int2bytes(U[0], math.ceil(U[0].bit_length()/8))
bytes_yU = int2bytes(U[1], math.ceil(U[1].bit_length()/8))

if U == [0, 0]:
    print("U == O, consult failed")
    sys.exit(1)

KA = KDF(bytes_xU + bytes_yU + ZA + ZB, klen)
#S1 = sha256(b'\x02' + bytes_yU + sha256(bytes_xU + ZA + ZB + int2bytes(x1, math.ceil(x1.bit_length()/8)) + int2bytes(y1, math.ceil(y1.bit_length()/8)) + int2bytes(x2, math.ceil(x1.bit_length()/8)) + int2bytes(y1, math.ceil(y2.bit_length()/8))))
#SA = sha256(b'\x03' + bytes_yU + sha256(bytes_xU + ZA + ZB + int2bytes(x1, math.ceil(x1.bit_length()/8)) + int2bytes(y1, math.ceil(y1.bit_length()/8)) + int2bytes(x2, math.ceil(x1.bit_length()/8)) + int2bytes(y1, math.ceil(y2.bit_length()/8))))
S1 = sha256(b'\x02' + bytes_yU + sha256(bytes_xU + ZA + ZB + int2bytes(x1, math.ceil(x1.bit_length()/8)) + int2bytes(y1, math.ceil(y1.bit_length()/8)) + int2bytes(x2, math.ceil(x2.bit_length()/8)) + int2bytes(y2, math.ceil(y2.bit_length()/8))))

#if bytes2int(S1) != SB:
if S1 != int2bytes(SB, 32):
    print(bytes2int(S1))
    print(SB)
    print("S1 != SB, confirm failed")
    sys.exit(1)

SA = sha256(b'\x03' + bytes_yU + sha256(bytes_xU + ZA + ZB + int2bytes(x1, math.ceil(x1.bit_length()/8)) + int2bytes(y1, math.ceil(y1.bit_length()/8)) + int2bytes(x2, math.ceil(x2.bit_length()/8)) + int2bytes(y2, math.ceil(y2.bit_length()/8))))
print(bytes2int(KA))
print(bytes2int(S1), bytes2int(SA), sep=' ')#zhengque
with open('shared.txt', 'r+') as file:
    while True:
        content = file.readline()
        if len(content) == 0:
            break
    file.write(str(bytes2int(SA)) + '\n')