from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput


def gcd(a, b):
    r, s, t = a, 1, 0
    r1, s1, t1 = b, 0, 1
    while r1 != 0:
        q = r//r1
        temp1, temp2, temp3 = r - q * r1, s - q * s1, t - q * t1
        r, s, t = r1, s1, t1
        r1, s1, t1 = temp1, temp2, temp3
    if b < 0 :
        r, s, t = -r, -s, -t
    return r


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


'''

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
            inv[i][j] = rmdet(m, j, i)
    return inv'''
'''def permute(nums):  # dao
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
        product = (-1) ** t
        i = 0
        for pn in p:
            product *= det[i][pn - 1]  # 连乘
            i += 1

        result += product  # 连加

    return result'''
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
            #C[i][j] = C[i][j] * invmod(d, 26)
            C[i][j] = (C[i][j] * invmod(d, 26))%26
    #return C
    return C


def mat_mutiply(M, N):
    c = []
    for i in range(0, len(M)):
        temp = []
        for j in range(0, len(N[0])):
            s = 0
            for k in range(0, len(M[0])):
                s += M[i][k] * N[k][j]
            temp.append(s%26)
        c.append(temp)
    #return c
    return list(c)


def attack2(cipher, m):
    m1 = inverseofmatrix(m)
    ans = mat_mutiply(m1, cipher)
    n = len(m)
    ans_s = ''
    #ans_s = []
    #for i in range(0, n):
    #    for j in range(0, n):
            #ans_s += chr((ans[i][j])%26+ord('a'))
    #        ans_s.append()
    #return ans_s
    '''for i in range(0, n):
        for j in range(0, n):
            ans[i][j] %= 26
    '''
    return ans


def main():
    n = eval(input().strip())
    message = input().strip()
    cipher = input().strip()

    message_mat = []
    det = 2

    cip_mat = []
    k = 0
    while gcd(det, 26) != 1 and k < len(message)-n*n:
        message_mat = []
        cip_mat = []
        if len(message) >= n*n:
            for i in range(0, n):
                line = []
                for j in range(0, n):
                    line.append(ord(message[i*n+j+k]) - ord('a'))
                message_mat.append(line)
            for i in range(0, n):
                line = []
                for j in range(0, n):
                    line.append(ord(cipher[i * n + j+k]) - ord('a'))
                cip_mat.append(line)
        #k += 1
        k += n
        det = detofmatrix(message_mat)



    #print(calculate(message_mat)%26)
    ans = attack2(cip_mat, message_mat)

    #print(ans)
    for i in range(0, n):
        for j in range(0, n):
            print(ans[i][j], end=' ')
        print()
if __name__ == '__main__':
    with PyCallGraph(output=GraphvizOutput()):
        main()

'''for i in range(0, len(message)//3):
    line = []
    for j in range(0, 3):
        line.append(ord(message[i][j])-ord('a'))
    messge_mat.append(line)
for i in range(0, len(cipher)//n):
    line = []
    for j in range(0, n):
        line.append(ord(cipher[i][j])-ord('a'))
    cip_mat.append(line)
#平方
截取一部分不可行 hishishis'''
#一组一组加

