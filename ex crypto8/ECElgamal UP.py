from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput


def Egcd(a, b):#结果对 加法链还变慢
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


'''def multi(k, x0, y0, p, a):
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
        return ans'''
'''def multi(k, x0, y0, p, a):
    n_bit = "{0:b}".format(k)[::-1]  # 将倍数转换为二进制，并反转位序
    #Q = "O"  # 初始化中间变量Q为无穷远点
    Q = [0, 0]
    R = [x0, y0]  # 初始化中间变量R为点P
    for i in range(len(n_bit)):
        if n_bit[i] == "1":
            Q = add(Q[0], Q[1], R[0], R[1], p, a)  # 如果当前位为1，则计算Q+R
            R = add(R[0], R[1], R[0], R[1], p, a)  # 计算R的下一个倍数，即点加运算R+R
        else:
            R = add(R[0], R[1], Q[0], Q[1], p, a)  # 如果当前位为0，则计算R+Q
            Q = add(Q[0], Q[1], Q[0], Q[1], p, a)  # 计算Q的下一个倍数，即点加运算Q+Q
    return R'''
'''def multi(k, x0, y0, p, a):
    
    #Computes the scalar multiplication k*P using an addition chain
    
    P = [x0, y0]
    bin_k = bin(k)[2:]  # Convert k to binary
    n = len(bin_k)
    Q = [x0, y0]
    R = [0, 0]
    for i in range(0, n):
        if bin_k[i] == '1':
            # If bit i is 1, add P to Q
            Q = add(Q[0], Q[1], P[0], P[1], p, a)
            if R is [0, 0]:
                R = [x0, y0]
            else:
                # Double R and add P
                R = add(R[0], R[1], R[0], R[1], p, a)
                R = add(R[0], R[1], P[0], P[1], p, a)
        else:
            # If bit i is 0, double Q and R
            Q = add(Q[0], Q[1], Q[0], Q[1], p, a)
            if R is [0, 0]:
                R = Q
            else:
                R = add(R[0], R[1], R[0], R[1], p, a)
    return R'''
def base_mult(k, x0, y0, p, a):
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


def generate_naf(num):
    bin_num = bin(num)[2:]
    naf = []
    i = 0
    while i < len(bin_num):
        if bin_num[i] == '0':
            naf.append(0)
            i += 1
        else:
            if i == len(bin_num) - 1:
                naf.append(int(bin_num[i]))
                break
            if bin_num[i+1] == '0':
                naf.append(int(bin_num[i]))
                i += 2
            else:
                naf.append(int(bin_num[i:i+2])-2)
                i += 2
    return naf


def multi(k, x0, y0, p, a):
    k = k
    p0 = [x0, y0]
    p1 = double(x0, y0, p, a)
    neg = [x0, -y0]
    # length = len(bin(k))-2
    length = 0
    #w = k.bit_length() - 1  # 13有问题 没有-1问题更多
    #w = 4
    w = 2
    NAF = []
    while k > 0:  # 7不对
        if k % 2 == 1:#速度反而减了
            remainder = k % (1 << w)
            if remainder > (1 << (w - 1)):
                NAF.append(remainder - (1 << w))
                k = k - (remainder - (1 << w))
            else:
                NAF.append(remainder)
                k = k - remainder
        else:
            NAF.append(0)
        k = k // 2
        length += 1
    #NAF = generate_naf(k)
    #length = len(NAF)
    # Q = ec.EllipticCurvePublicNumbers(0, 0, curve).public_key(default_backend())
    Q = [0, 0]
    # NAF = NAF[::-1]
    i = length - 1
    while i >= 0:
        Q = double(Q[0], Q[1], p, a)
        j = NAF[i]
        if j > 0:
            # Q = Q.add(p0)
            if abs(NAF[i]) != 1:
                t = base_mult(abs(NAF[i]), p0[0], p0[1], p, a)#为什么跳回去？ 递归了
                Q = add(Q[0], Q[1], t[0], t[1], p, a)
            else:
                Q = add(Q[0], Q[1], p0[0], p0[1], p, a)
        elif j < 0:
            if abs(NAF[i]) != 1:
                t = base_mult(abs(NAF[i]), p0[0], p0[1], p, a)
                Q = add(Q[0], Q[1], t[0], -t[1], p, a)
            else:
                Q = add(Q[0], Q[1], p0[0], -p0[1], p, a)
        i = i - 1
    return Q


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
        N = eval(input().strip())
        C1, C2 = encrypt(Pm_x, Pm_y, k, Pb_x, Pb_y, G_x, G_y, p, a)
        #print(C1[0], end=' ')
        #print(C1[1])
        #print(C2[0], end=' ')
        #print(C2[1])
        ans = C2
        for _ in range(N):
            C1, ans = encrypt(ans[0], ans[1], k, Pb_x, Pb_y, G_x, G_y, p, a)
        print(C1[0], C1[1], sep=' ')#C1对· C2不对·
        print(ans[0], ans[1], sep=' ')
    else:
        C1_x, C1_y = map(int, input().split(" "))
        C2_x, C2_y = map(int, input().split(" "))
        n_B = eval(input().strip())
        N = eval(input().strip())
        Pm = decrypt(C1_x, C1_y, C2_x, C2_y, n_B, p, a)
        #print(Pm[0], end=' ')
        #print(Pm[1])
        ans = Pm
        for i in range(N):
            ans = decrypt(C1_x, C1_y, ans[0], ans[1], n_B, p, a)
        print(ans[0], ans[1], sep=' ')
        #加法链


if __name__ == '__main__':
    with PyCallGraph(output=GraphvizOutput()):
        main()
        '''def add_chain_exponentiation(base, exponent, chain_length):
            # 加法链指数幂算法
            chains = [0] * chain_length
            k = exponent // chain_length
            r = exponent % chain_length
            chains[0] = base
            for i in range(1, chain_length):
                chains[i] = (chains[i-1] ** k) % p
            result = 1
            for i in reversed(range(chain_length)):
                result = (result ** chain_length) * chains[i]
            if r != 0:
                result *= base ** r
            return result'''
        '''def ecc_point_addition(P, Q):
        """计算两个点P、Q的和"""
        if P == "O":  # 如果其中一个点为无穷远点，返回另一个点
            return Q
        if Q == "O":
            return P
        if P[0] == Q[0] and P[1] == -Q[1]:  # 如果两个点在x轴对称，则返回无穷远点
            return "O"
        if P != Q:  # 如果不是同一个点，则进行点加运算
            k = (P[1] - Q[1]) / (P[0] - Q[0])
            x = k ** 2 - P[0] - Q[0]
            y = k * (P[0] - x) - P[1]
        else:  # 否则进行点倍运算
            k = (3 * P[0] ** 2 + a) / (2 * P[1])
            x = k ** 2 - 2 * P[0]
            y = k * (P[0] - x) - P[1]
        return (x, y)
    
    def ecc_point_multiplication(P, n):
        """使用加法链算法计算点P的n倍"""
        n_bit = "{0:b}".format(n)[::-1]  # 将倍数转换为二进制，并反转位序
        Q = "O"  # 初始化中间变量Q为无穷远点
        R = P  # 初始化中间变量R为点P
        for i in range(len(n_bit)):
            if n_bit[i] == "1":
                Q = ecc_point_addition(Q, R)  # 如果当前位为1，则计算Q+R
                R = ecc_point_addition(R, R)  # 计算R的下一个倍数，即点加运算R+R
            else:
                R = ecc_point_addition(R, Q)  # 如果当前位为0，则计算R+Q
                Q = ecc_point_addition(Q, Q)  # 计算Q的下一个倍数，即点加运算Q+Q
        return Q
        
        
        
        def ecc_addition_chain(k, P):
        """
        Computes the scalar multiplication k*P using an addition chain
        """
        bin_k = bin(k)[2:]  # Convert k to binary
        n = len(bin_k)
        Q = P
        R = None
        for i in range(1, n):
            if bin_k[i] == '1':
                # If bit i is 1, add P to Q
                Q = point_addition(Q, P)
                if R is None:
                    R = P
                else:
                    # Double R and add P
                    R = point_addition(R, R)
                    R = point_addition(R, P)
            else:
                # If bit i is 0, double Q and R
                Q = point_addition(Q, Q)
                if R is None:
                    R = Q
                else:
                    R = point_addition(R, R)
        return Q
'''
#wNAF
