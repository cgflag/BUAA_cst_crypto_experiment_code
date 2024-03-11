from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
import hashlib
import hmac
import math
import time

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


'''def KDF(Z, klen):
    # 将klen转换为字节数
    klen_byte = (klen + 7) // 8

    # 根据SM2标准构造常量字符串
    ct = b""
    #for i in range(1, (klen_byte // 32) + 1):
    #for i in range(1, klen_byte + 1):
    #for i in range(1, (klen // 32) + 1):
    for i in range(1, klen_byte + 2):
        ct += hashlib.sha256(Z + int2bytes(i, 4)).digest()

    # 如果klen不能被32整除，则再执行一次hash #不要补全
    #if klen % 32 != 0:
        #ct += hashlib.sha256(Z + bytes([(klen_byte // 32) + 1])).digest()
        ##ct += hashlib.sha256(Z + int2bytes((klen // 32) + 1, 8)).digest()

    # 返回长度为klen_byte的密钥K #取bit
    return ct[:klen_byte]'''
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
    return v[:klen_byte]#这个解密对了



def SM2_encrypt(M, klen, k, G, p, a, PB):#h余因子
    #C1 G倍点 类型转换字节转比特串
    l = math.ceil(math.ceil(math.log(p, 2)) / 8)#还得求集合大小和阶？
    #h =
    while True:
        C1 = multi(k, G[0], G[1], p, a)
        #print(hex(C1[0]), end=' ')
        #print(hex(C1[1]))
        bytes_C1 = point2bytes(C1, p)

        #S Pb
        #S = multi(h, PB[0], PB[1], p, a)
        #bytes_S = point2bytes(S, p)
        #hPb 坐标 域元素转比特串 ?h
        x2, y2 = multi(k, PB[0], PB[1], p, a)
        #print(hex(x2), end=' ')
        #print(hex(y2))
        bytes_x2, bytes_y2 = int2bytes(x2, l), int2bytes(y2, l)#l
        t = KDF(bytes_x2 + bytes_y2, klen)
        #print(hex(bytes2int(t)))
        if bytes2int(t) == 0:
            continue
        #C2 = bytes([x ^ y for x, y in zip(int2bytes(M, math.ceil(p.bit_length() / 8)), t)])#M ^ t#?字节串能否异或
        C2 = bytes([x ^ y for x, y in zip(int2bytes(M, math.ceil(M.bit_length() / 8)), t)])
        #print(hex(bytes2int(C2)))
        #C3 = sha256(bytes_x2 + int2bytes(M, math.ceil(p.bit_length() / 8)) + bytes_y2)
        C3 = sha256(bytes_x2 + int2bytes(M, math.ceil(M.bit_length() / 8)) + bytes_y2)
        C =  bytes_C1 + C2 + C3
        return C


def SM2_decrypt(C, klen, dB, p, a):
    #取出C1 C1长度是固定的吗
    #C转字节串 之后划分
    C = int2bytes(C, math.ceil(C.bit_length() / 8))
    l = math.ceil(math.ceil(math.log(p, 2)) / 8)  # 还得求集合大小和阶？
    C1 = C[0: 2 * l + 1]
    C2 = C[2 * l + 1: 2 * l + 1 + math.ceil(klen/8)]
    C3 = C[2 * l + 1 + math.ceil(klen/8):]
    p_C1 = bytes2point(C1, p)
    x2, y2 = multi(dB, p_C1[0], p_C1[1], p, a)
    #S = multi(h, C1[0], C1[1], p, a)

    bytes_x2, bytes_y2 = int2bytes(x2, l), int2bytes(y2, l)
    t = KDF(bytes_x2 + bytes_y2, klen)
    #M = bytes([x ^ y for x, y in zip(int2bytes(C2, math.ceil(p.bit_length() / 8)), t)])
    M = bytes([x ^ y for x, y in zip(C2, t)])
    #u = sha256()
    return M


def main():
    p = eval(input().strip())
    a = eval(input().strip())
    b = eval(input().strip())
    G = list(map(int, input().split(" ")))
    Par = eval(input().strip())
    op = eval(input().strip())
    mes = eval(input().strip())
    l = math.ceil(math.log(p, 2) / 8)
    if op == 1:
        PB = list(map(int, input().split(" ")))
        klen = mes.bit_length()
        k = eval(input().strip())
        #别忘了补0
        ans = SM2_encrypt(mes, klen, k, G, p, a, PB)
        ans = bytes2int(ans)

        ans = '0x0' + hex(ans)[2:]
        print(ans)
    else:
        dB = eval(input().strip())
        #？klen
        klen = mes.bit_length() - 8 * (2 * l + 1) - 256
        ans = SM2_decrypt(mes, klen, dB, p, a)
        ans = bytes2int(ans)

        print("0x", end='')
        print("%x" % ans)


if __name__ == '__main__':
    start_time = time.time()
    with PyCallGraph(output=GraphvizOutput()):
        main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Elapsed time: {:.6f} seconds".format(elapsed_time))
#RSA强素数
#预结算
#剪枝
#加密只有前几位对
#不对解密
#0x04245c26fb68b1ddddb12c4b6bf9f2b6d5fe60a383b0d18d1c4144abf17f6252e776cb9264c2a7e88e52b19903fdc47378f605e36811f5c07423a24b84400f01b8 6f081f231e38bcfdb9d7e4862c61999d5cbee9f638494d6d27b17885c800d754d465c455968634d04ea494616ba817 c229e8b6
#0x04245c26fb68b1ddddb12c4b6bf9f2b6d5fe60a383b0d18d1c4144abf17f6252e776cb9264c2a7e88e52b19903fdc47378f605e36811f5c07423a24b84400f01b8 229e6c9aee2bb92cad649fe2c035689785da33be89139d07853100efa763f60cbe30099ea3df7f8f364f9d10a5e988 e3c5aafc
#0x1145141919810ab19260817cd947866efedcba
#0x48248b16d62f58aa6daaecf176634960b9e0ee
#0x04245c26fb68b1ddddb12c4b6bf9f2b6d5fe60a383b0d18d1c4144abf17f6252e776cb9264c2a7e88e52b19903fdc47378f605e36811f5c07423a24b84400f01b847f00fe8975bcd45c20abf91b431689096d127f638494d6d27b17885c800d754d465c455968634d04ea494616ba817c229e8b6
#0x04245c26fb68b1ddddb12c4b6bf9f2b6d5fe60a383b0d18d1c4144abf17f6252e776cb9264c2a7e88e52b19903fdc47378f605e36811f5c07423a24b84400f01b8229e6c9aee2bb92cad649fe2c035689785da33 be89139d07853100efa763f60cbe30099ea3df7f8f364f9d10a5e988e3c5aafc
#0x04245c26fb68b1ddddb12c4b6bf9f2b6d5fe60a383b0d18d1c4144abf17f6252e776cb9264c2a7e88e52b19903fdc47378f605e36811f5c07423a24b84400f01b8229e6c9aee2bb92cad649fe2c035689785da33 be89139d07853100efa763f60cbe30099ea3df7f8f364f9d10a5e988e3c5aafc
#0x04245c26fb68b1ddddb12c4b6bf9f2b6d5fe60a383b0d18d1c4144abf17f6252e776cb9264c2a7e88e52b19903fdc47378f605e36811f5c07423a24b84400f01b8229e6c9aee2bb92cad649fe2c035689785da33 f638494d6d27b17885c800d754d465c455968634d04ea494616ba817c229e8b6