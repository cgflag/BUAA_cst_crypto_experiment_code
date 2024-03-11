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


def main():
    p = eval(input().strip())
    a = eval(input().strip())
    b = eval(input().strip())
    A_x, A_y = map(int, input().split(" "))
    B_x, B_y =map(int, input().split(" "))
    k = eval(input().strip())

    sum = add(A_x, A_y, B_x, B_y, p, a)
    diff = sub(A_x, A_y, B_x, B_y, p, a)
    mul_result = multi(k, A_x, A_y, p, a)#慢

    print(sum[0], end=' ')
    print(sum[1])
    print(diff[0], end=' ')
    print(diff[1])
    print(mul_result[0], end=' ')
    print(mul_result[1])#倍点哪里错了？


if __name__ == '__main__':
    with PyCallGraph(output=GraphvizOutput()):
        main()
#t12637770518718272361069030959675909011950070361104001676990341902418348821166
#w86375030786635094404384804603083222796334328654542125546726580606530221105506

#t8782182299491035655407366522213245608339654612217932552302421142270846681994
#w82537453111862378017531365428025545403473629699965547851282003923889747350878 da
#debug
#sum = add(A_x, A_y, B_x, B_y, p, a)
#diff = sub(A_x, A_y, B_x, B_y, p, a)
#mul_result1 = add(multi(2, A_x, A_y, p, a)[0], multi(2, A_x, A_y, p, a)[1], A_x, A_y, p, a)#慢
#mul_result2 = add(double(A_x, A_y, p, a)[0], double(A_x, A_y, p, a)[1], A_x, A_y, p, a)
#mul_result3 = multi(3, A_x, A_y, p, a)

#mul_result1 = multi(2, A_x, A_y, p, a)#慢
#mul_result2 = double(A_x, A_y, p, a)不一样
#64901889550129866513443884082574452575157116031103742365434905633820925813192 84553412528427919723206133858954594911213526647800598970633596412071681640913
#46265008535339128785615121705652515610876129255117925363495168987013185179160 81035072460156187231565236226739487574245648226168407152527165957566304548283]