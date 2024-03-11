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
    if gcd(a, n) == 1:
        _, result, _ = Egcd(a, n)
    return result % n

def encrypt(N, e, m):
    c = pow(m, e, N)
    return c

def decrypt(p, q, e, c, N):
    '''phi = (p - 1) * (q - 1)
    d = invmod(e, phi)
    return pow(c, d, N)
    '''
    #CRT加速后
    g, _, _ = Egcd(p-1, q-1)
    phi = (p - 1) * (q - 1)//g
    d = invmod(e, phi)
    m1 = pow(c % p, d % (p-1), p)
    m2 = pow(c % q, d % (q-1), q)
    a = invmod(q, p)
    b = invmod(p, q)
    m = (m1*a*q+m2*b*p) % N
    return m


def main():
    p = eval(input().strip())
    q = eval(input().strip())
    e = eval(input().strip())
    m = eval(input().strip())
    op = eval(input().strip())

    n = p * q

    if op == 1:
        print(encrypt(n, e, m))

    else:
        print(decrypt(p, q, e, m, n))


if __name__ == '__main__':
    with PyCallGraph(output=GraphvizOutput()):
        main()