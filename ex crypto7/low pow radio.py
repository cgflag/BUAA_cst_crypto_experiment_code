from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
import gmpy2
from functools import reduce


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


def crt(cpr_lst, n_lst):
    """
    中国剩余定理求解: x == c (mod n)
    params:
        cpr-lst 余数c列表
        n_lst 模数n列表
    return: x
    """
    # 累积 m = n1*n2*...*nk
    m = reduce(lambda x, y: x * y, (ni for ni in n_lst))
    result = 0
    data = zip(cpr_lst, n_lst)
    for ci, ni in data:
        mi = m // ni
        di = invmod(mi, ni)
        result += (ci * mi * di) % m
    return result % m, m


def main():
    n = eval(input().strip())
    e = eval(input().strip())
    c_list = []
    N_list = []
    for i in range(n):
        c_list.append(eval(input().strip()))
        N_list.append(eval(input().strip()))

    C, N = crt(c_list, N_list)
    res = gmpy2.iroot(C, e)
    if res[1]:
        print(res[0])


if __name__ == '__main__':
    with PyCallGraph(output=GraphvizOutput()):
        main()