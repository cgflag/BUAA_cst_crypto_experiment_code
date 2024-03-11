import hashlib
import math


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


def Sign(s, r):
    R = pow(alp, r, p)
    #e = sha1(int2bytes(R, math.ceil(R.bit_length()/8)) + M.encode())
    #e = sha1((str(R) + M).encode())
    e = sha1((M + str(R)).encode())
    #规定？
    y = (r + s * bytes2int(e)) % q
    print(bytes2int(e), y, sep=' ')


def Verify(v, e, y):
    R_prime = (pow(alp, y, p) * pow(v, e, p)) % p
    #if e == bytes2int(sha1((str(R_prime) + M).encode())):
    if e == bytes2int(sha1((M + str(R_prime)).encode())):
        print("True")
    else:
        print("False")



p = eval(input().strip())
q = eval(input().strip())
alp = eval(input().strip())
M = input().strip()
Mode = input().strip()
if Mode == 'Sign':
    s = eval(input().strip())
    r = eval(input().strip())
    Sign(s, r)
elif Mode == 'Vrfy':
    v = eval(input().strip())
    e, y = map(int, input().split(" "))
    Verify(v, e, y)

#计算很混乱