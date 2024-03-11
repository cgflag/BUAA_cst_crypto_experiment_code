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


def qpow(a, m, n):
    result = 1
    while m > 0:
        if m % 2 == 1:
            result = (result * a) % n
        a = (a * a) % n
        m //= 2
    return result


def main():
    e1 = eval(input().strip())
    e2 = eval(input().strip())
    c1 = eval(input().strip())
    c2 = eval(input().strip())
    N = eval(input().strip())

    g, u, v = Egcd(e1, e2)
    c2v = invmod(c2, N)
    if u < 0:
        c1 = invmod(c1, N)
    if v < 0:
        c2 = invmod(c2, N)
    #msg = (pow(c1, e1, N) % N*pow(c2v, -e2, N) % N) % N
    #msg = (pow(c1, u, N) % N*pow(c2v, -v, N) % N) % N
    #msg = (qpow(c1, u, N) % N*qpow(c2v, -v, N) % N) % N
    #msg = (qpow(c1, u, N) % N*qpow(c2, v, N) % N) % N
    msg = (qpow(c1, abs(u), N) % N*qpow(c2, abs(v), N) % N) % N
    print(msg)


if __name__ == '__main__':
    with PyCallGraph(output=GraphvizOutput()):
        main()