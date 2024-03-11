import random
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput


def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a


def getpq(n, e, d):
    p = 1
    q = 1
    while p == 1 and q == 1:
        k = d * e - 1
        g = random.randint(0, n)
        while p == 1 and q == 1 and k % 2 == 0:
            k //= 2
            y = pow(g, k, n)
            if y != 1 and gcd(y - 1, n) > 1:
                p = gcd(y - 1, n)
                q = n // p
    return p, q


def main():
    e = eval(input().strip())
    d = eval(input().strip())
    N = eval(input().strip())

    p, q = getpq(N, e, d)
    print(min(p, q))
    print(max(p,q))


if __name__ == '__main__':
    with PyCallGraph(output=GraphvizOutput()):
        main()
