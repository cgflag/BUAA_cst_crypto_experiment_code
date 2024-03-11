import hashlib
import math
import sys


hlen = 20
slen = 20


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


def sha1(m):#sha1 #L不是空时怎么处理？
    return hashlib.sha1(m).digest()


def MGF(X, maskLen):
    T = b''
    k = math.ceil(maskLen / hlen) - 1
    for i in range(0, k + 1):
        C = int2bytes(i, 4)
        T += sha1(X + C)
    return T[:maskLen]


def sign(M, emBits, d, n, salt):
    padding1 = b'\x00' * 8
    mhash = sha1(M.encode())
    #print(bytes2int(mhash))
    emlen = math.ceil(emBits / 8)
    padding2 = b'\x00' * (emlen - slen - hlen - 2) + b'\x01'
    #M_prime = padding1 + mhash + salt#!(整数转字节)
    M_prime = padding1 + mhash + int2bytes(salt, math.ceil(salt.bit_length() / 8))
    #M_prime = padding1 + mhash + int2bytes(salt, slen)
    #print(M_prime)
    #print('M_prime:' + (hex(bytes2int(M_prime))))#对
    H = sha1(M_prime)
    #print('H:' + (hex(bytes2int(H))))#不一样？
    DB = padding2 + int2bytes(salt, math.ceil(salt.bit_length() / 8))
    #DB = padding2 + int2bytes(salt, slen)
    dbmask = MGF(H, emlen-hlen-1)
    maskedDB = bytes(a ^ b for a, b in zip(DB, dbmask))#异或
    #左面_字节设为0
    maskedDB = b'\x00' * math.ceil((emlen - emBits / 8)) + maskedDB[math.ceil(emlen - emBits / 8):]
    EM = maskedDB + H + b'\xbc'
    s = hex(pow(bytes2int(EM), d, n))[2:]
    '''while len(s) <= 2 * 128:
        s = '0' + s'''
    print(s)#k字节长


def Verify(M, emBits, e, n,  S):
    #还要先解密
    padding1 = b'\x00' * 8
    emlen = math.ceil(emBits / 8)
    padding2 = b'\x00' * (emlen - slen - hlen - 2) + b'\x01'

    m = pow(S, e, n)
    #EM = int2bytes(m, math.ceil(1023 / 8))
    EM = int2bytes(m, math.ceil(emBits / 8))
    mhash = sha1(M.encode())
    if emlen - slen - hlen - 2 < 0:
        print("False")
        sys.exit(0)
    if EM[-1] != 0xbc:
        print("False")
        sys.exit(0)
    maskedDB = EM[0: emlen - hlen - 1]
    H = EM[emlen - hlen - 1: emlen - 1]
    if maskedDB[0: (8 * emlen - emBits) // 8] != b'\x00' * ((8 * emlen - emBits) // 8):#不全0
        print("False")
        sys.exit(0)
    dbmask = MGF(H, emlen - hlen - 1)
    DB = bytes(a ^ b for a, b in zip(maskedDB, dbmask))
    #设置左为0
    DB = b'\x00' * math.ceil((emlen - emBits / 8)) + DB[math.ceil((emlen - emBits / 8)):]
    #最左填充2比较
    if DB[: emlen - hlen - slen - 1] != padding2:
        print("False")
        sys.exit(0)
    #salt = DB[-1-slen: -1]
    salt = DB[-slen:]
    M_prime = padding1 + mhash + salt
    H_prime = sha1(M_prime)
    if H == H_prime:
        print("True")
    else:
        print("False")#此处有问题



M = input().strip()
n = eval(input().strip())
emBits = eval(input().strip())
Mode = input().strip()
emlen = math.ceil(emBits / 8)
if Mode == 'Sign':
    d = eval(input().strip())
    salt = eval('0x' + input().strip())
    sign(M, emBits, d, n, salt)
elif Mode == 'Vrfy':
    e = eval(input().strip())
    S = eval('0x' + input().strip())
    Verify(M, emBits, e, n, S)




'''
本题所用哈希函数固定为 SHA1，即 hLen=20hLen=20；
本题所有盐值固定为 2020 字节，即 sLen=20sLen=20；
本题采用模数的比特长度固定为 10241024。
'''
'''original_bytes = b'\x12\x34\x56\x78\x90'  # 原始字节串
zero_bytes = b'\x00\x00'                  # 要替换成全0的字节串

modified_bytes = zero_bytes + original_bytes[len(zero_bytes):]'''#例子