import hashlib
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

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


def sha256(m):#sha1 #L不是空时怎么处理？
    return hashlib.sha256(m).digest()


def Sign(q, alp, M, XA, K):
    m = bytes2int(sha256(M.encode()))
    s1 = pow(alp, K, q)
    k_r = invmod(K, q-1)
    s2 = (k_r * (m - XA * s1)) % (q-1)
    print(s1, s2, sep=' ')


def Verify(q, alp, M, YA, S1, S2):
    m = bytes2int(sha256(M.encode()))
    v1 = pow(alp, m, q)
    v2 = (pow(YA, S1, q) * pow(S1, S2, q)) % q
    if v1 == v2:
        print("True")
    else:
        print("False")


def main():
    q = eval(input().strip())
    alp = eval(input().strip())
    M = input().strip()
    Mode = input().strip()
    if Mode == 'Sign':
        XA = eval(input().strip())
        K = eval(input().strip())
        Sign(q, alp, M, XA, K)
    elif Mode == 'Vrfy':
        YA = eval(input().strip())
        S1, S2 = map(int, input().split(" "))
        Verify(q, alp, M, YA, S1, S2)


if __name__ == '__main__':
    with PyCallGraph(output=GraphvizOutput()):
        main()
#标准梅森素数