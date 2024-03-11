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


def encrypt(Pm_x, Pm_y, k, Pb_x, Pb_y, G_x, G_y, p, a):
    C1 = multi(k, G_x, G_y, p, a)
    temp = multi(k, Pb_x, Pb_y, p, a)
    C2 = add(Pm_x, Pm_y, temp[0], temp[1], p, a)
    return C1, C2


def decrypt(C1_x, C1_y, C2_x, C2_y, n_B, p, a):
    temp = multi(n_B, C1_x, C1_y, p, a)
    Pm = sub(C2_x, C2_y, temp[0], temp[1], p, a)
    return Pm


def main():
    p = eval(input().strip())
    a = eval(input().strip())
    b = eval(input().strip())
    G_x, G_y = map(int, input().split(" "))
    op = eval(input().strip())
    if op == 1:
        Pm_x, Pm_y = map(int, input().split(" "))
        k = eval(input().strip())
        Pb_x, Pb_y = map(int, input().split(" "))
        C1, C2 = encrypt(Pm_x, Pm_y, k, Pb_x, Pb_y, G_x, G_y, p, a)
        print(C1[0], end=' ')
        print(C1[1])
        print(C2[0], end=' ')
        print(C2[1])
    else:
        C1_x, C1_y = map(int, input().split(" "))
        C2_x, C2_y = map(int, input().split(" "))
        n_B = eval(input().strip())
        Pm = decrypt(C1_x, C1_y, C2_x, C2_y, n_B, p, a)
        print(Pm[0], end=' ')
        print(Pm[1])


if __name__ == '__main__':
    with PyCallGraph(output=GraphvizOutput()):
        main()