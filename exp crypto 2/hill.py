#def matrix_reverse(mat):
'''def Exgcd(a, b):
    r, s, t = a, 1, 0
    r1, s1, t1 = b, 0, 1
    while r1 != 0:
        q = r//r1
        temp1, temp2, temp3 = r - q * r1, s - q * s1, t - q * t1
        r, s, t = r1, s1, t1
        r1, s1, t1 = temp1, temp2, temp3
    if b < 0 :
        r, s, t = -r, -s, -t
    return r, s, t


def invmod(a, n):
    g, _, _ = Exgcd(a, n)
    if g == 1:
        _, ans, _ = Exgcd(a, n)
    return ans%n

def mat_mutiply(targ, mat):
    dim = len(mat)
    ans = [[]*dim]
    for i in range(0, len(targ)):
        for j in range(0, dim):
            sum = 0
            for k in range(0, dim):
                sum += (targ[i][k] * mat[k][j]) % 26
                sum %= 26
            ans[i].append(sum)
    return ans
    '''
'''


def permute(nums):  # dao
    # 生成n个元素的全排列
    length = len(nums)

    permutations = []

    def _permute(index=0):

        if index == length:
            permutations.append(nums[0:length])

        for i in range(index, length):
            nums[i], nums[index] = nums[index], nums[i]
            _permute(index + 1)
            nums[i], nums[index] = nums[index], nums[i]

    _permute()

    return permutations


def inversion_number(nums):  # dao
    # 计算排列的逆序数
    count = 0
    for i in range(len(nums)):

        for j in range(i):

            if nums[j] > nums[i]:
                count += 1

    return count


def calculate(det):  # dao
    # 计算n阶行列式的值

    if not det:  # 没有元素
        return 0

    if len(det) == 1:  # 一阶行列式直接返回值
        return det[0]

    # 生成 1,..., n的全排列
    permutations = permute([i for i in range(1, len(det) + 1)])

    result = 0

    for p in permutations:
        # t为逆序数
        t = inversion_number(p)
        #product = (-1) ** t
        product = pow(-1, t%2)
        i = 0
        for pn in p:
            #product *= det[i][pn - 1]  # 连乘
            #
            product *= det[i][pn - 1]%26
            product %= 26
            i += 1

        #result += product  # 连加
        result %= 26

    return result


def rmdet(m, i1, j1):  # dao
    det = calculate(m)
    size = len(m)
    t = [[0] * (size - 1) for _ in range(size - 1)]
    row = 0
    col = 0
    for i in range(size):
        if i != i1:
            row += 1
            col = 0
            for j in range(size):
                if j != j1:
                    col += 1
                    t[row - 1][col - 1] = m[i][j]

    result = calculate(t) * pow(-1, (i1 + j1) % 2)
    result *= invmod(det, 26)
    result %= 26
    return result


def matrix_inv(m):  # dao
    det = calculate(m)
    size = len(m)
    inv = [[int(0)] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            #inv[i][j] = rmdet(m, j, i)
            inv[i][j] = rmdet(m, j, i)%26
    return inv

#高斯消元
#def matrix_inv(m):
    m1 = m
    n = len(m)
    unit = []
    for i in range(0, n):
        line = []
        for j in range(0, n):
            line.append(0)
        unit.append(line)
    for i in range(0, n):
        unit[i][i] = 1
    for i in range(0, n):
        m1[i] += unit[i]
    for i in range(0, n):
        if m1[i][j] == 0:
            for j in range(i+1, n):
                if m1[i][j] != 0:
                    break
            if j == n:
                return
            for r in range(i, 2*n):
                m1[i][r] += m1[j][r]
                m1[j][r] %= 26
        ep = m1[i][i]%26
        for r in range(i, 2*n):
            m1[i][r] *= invmod(ep, 26)
            m1[i][r] %= 26
        for j in range(i+1, n):
            e = 26-(m1[j][i]*invmod(m1[i][i]))%26
            for r in range(i, 2*n):
                m1[j][r] += e*m1[i][r]
                m1[j][r] %= 26
    for i in range(n-1, -1, -1):
        for j in range(i - 1, -1, -1):
            e = 26 - (m1[j][i] * invmod(m1[i][i])) % 26
            for r in range(i, 2 * n):
                m1[j][r] += e * m1[i][r]
                m1[j][r] %= 26
    result = []
    for i in range(0, n):
        line = []
        for j in range(0, n):
            line.append(0)
        result.append(line)
    for i in range(0, n):
        for r in range(n, 2*n):
            result[i][r-n] = m1[i][r]
    return result#


def mat_mutiply(M, N):
    c = []
    for i in range(0, len(M)):
        temp = []
        for j in range(0, len(N[0])):
            s = 0
            for k in range(0, len(M[0])):
                s += M[i][k] * N[k][j]
            temp.append(s)
        c.append(temp)
    #return c
    return list(c)


def encrypt(s, k):
    dim = len(k)
    s1 = []
    n_line = len(s) // dim
    #s1 = [[]*(len(s)//dim)]
    for i in range(0, n_line):
        line = []
        for j in range(0, dim):
            #s1[i][j] = ord(s[i*dim+j])-ord('a')
            line.append(ord(s[i*dim+j])-ord('a'))
        s1.append(line)
    ans = mat_mutiply(s1, k)
    cipher = ''
    for i in range(0, len(s)//dim):
        for j in range(0, dim):
            cipher += chr((ans[i][j])%26+ord('a'))
    return cipher
#为什么同步变化

def decrypt(s, k):
    k1 = matrix_inv(k)
    dim = len(k)
    s1 = []
    n_line = len(s) // dim
    # s1 = [[]*(len(s)//dim)]
    for i in range(0, n_line):
        line = []
        for j in range(0, dim):
            # s1[i][j] = ord(s[i*dim+j])-ord('a')
            line.append(ord(s[i * dim + j]) - ord('a'))
        s1.append(line)
    ans = mat_mutiply(s1, k1)
    message = ''
    for i in range(0, n_line):
        for j in range(0, dim):
            message += chr((ans[i][j]) % 26 + ord('a'))
    return message


n = eval(input().strip())
key = []
for i in range(0, n):
    #line = list(map(int, input().split(" ")))
    line = list(map(int, input().strip().split(" ")))
    key.append(line)
s = input().strip()
mode = eval(input().strip())

if mode == 1:
    print(encrypt(s, key))
else:
    print(decrypt(s, key))
#难道要三个三个乘
print(matrix_inv(key))'''
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

def Exgcd(a, b):
    r, s, t = a, 1, 0
    r1, s1, t1 = b, 0, 1
    while r1 != 0:
        q = r//r1
        temp1, temp2, temp3 = r - q * r1, s - q * s1, t - q * t1
        r, s, t = r1, s1, t1
        r1, s1, t1 = temp1, temp2, temp3
    if b < 0 :
        r, s, t = -r, -s, -t
    return r, s, t


def invmod(a, n):
    g, _, _ = Exgcd(a, n)
    if g == 1:
        _, ans, _ = Exgcd(a, n)
    return ans%n


def multiplyofmatrix(A, f):
    """
    Compute matrix A * matrix f.
    For example:
    Input:
    A: [[1, 2], [3, 4]]    Row of A: 2 Col of A: 2
    f: [[1, 2], [3, 4]]    Row of f: 2 Col of f: 2
    Output:
    ans: [[7, 10], [15, 22]]

    s.t. A.col == f.col
    """
    Arow, Acol = len(A), len(A[0])
    frow, fcol = len(f), len(f[0])
    if Acol != frow:
        return 'False!'
    ans = [[0] * fcol for _ in range(Arow)]
    for i in range(fcol):
        for j in range(Arow):
            for k in range(frow):
                ans[j][i] += A[j][k]*f[k][i]
    return ans


def submatrix(A, i, j):
    # 矩阵A第i行第j列元素的余矩阵
    m, n = len(A), len(A[0])
    C = [[A[x][y] for y in range(n) if y != j] for x in range(m) if x != i]  # 列表推导式
    return C


def detofmatrix(A):
    m = len(A)  # 矩阵的行数
    n = len(A[0])  # 矩阵的列数
    if m == 1 and n == 1:
        return A[0][0]
    else:
        value = 0
        for j in range(n):
            value += ((-1) ** (j + 2)) * A[0][j] * detofmatrix(submatrix(A, 0, j))
        return value


def inverseofmatrix(A):
    #注意逆元
    m = len(A)  # 矩阵的行数
    n = len(A[0])  # 矩阵的列数
    C = [[0] * n for _ in range(m)]
    d = detofmatrix(A)
    for i in range(m):
        for j in range(n):
            C[i][j] = ((-1) ** (i + j + 2)) * detofmatrix(submatrix(A, j, i))
            #C[i][j] = C[i][j] / d
            C[i][j] = C[i][j] * invmod(d, 26)
    return C


def encrypt(s, k):
    dim = len(k)
    s1 = []
    n_line = len(s) // dim
    # s1 = [[]*(len(s)//dim)]
    for i in range(0, n_line):
        line = []
        for j in range(0, dim):
            # s1[i][j] = ord(s[i*dim+j])-ord('a')
            line.append(ord(s[i * dim + j]) - ord('a'))
        s1.append(line)
    ans = multiplyofmatrix(s1, k)
    cipher = ''
    for i in range(0, len(s) // dim):
        for j in range(0, dim):
            cipher += chr((ans[i][j]) % 26 + ord('a'))
    return cipher


def decrypt(s, k):
    k1 = inverseofmatrix(k)
    dim = len(k)
    s1 = []
    n_line = len(s) // dim
    # s1 = [[]*(len(s)//dim)]
    for i in range(0, n_line):
        line = []
        for j in range(0, dim):
            # s1[i][j] = ord(s[i*dim+j])-ord('a')
            line.append(ord(s[i * dim + j]) - ord('a'))
        s1.append(line)
    ans = multiplyofmatrix(s1, k1)
    message = ''
    for i in range(0, n_line):
        for j in range(0, dim):
            message += chr((ans[i][j]) % 26 + ord('a'))
    return message


def main():
    n = eval(input().strip())
    key = []
    for i in range(0, n):
        #line = list(map(int, input().split(" ")))
        line = list(map(int, input().strip().split(" ")))
        key.append(line)
    s = input().strip()
    mode = eval(input().strip())

    if mode == 1:
        print(encrypt(s, key))
    else:
        print(decrypt(s, key))

if __name__ == '__main__':
    with PyCallGraph(output=GraphvizOutput()):
        main()
