from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput


def encrypt(s, k):
    ans = ''
    for j in range(0, k):
        for i in range(0, len(s)):
            if i % k == j:
                ans += s[i]
    return ans


def decrypt(s, k):
    ans = ''
    line_len = [0]*k
    l_s = len(s)
    #line_length = 0
    for i in range(0, len(s)):
        for j in range(0, k):
            if i % k == j:
                line_len[j] += 1
    mat = []
    for i in range(0, k):
        line = []
        for j in range(0, line_len[0]):
            line.append(0)
        mat.append(line)
    sum_big = line_len[0]
    sum_small = 0
    r = 0
    for t in range(0, l_s):

        if t >= sum_big:
            sum_small += line_len[r]
            r += 1
            sum_big += line_len[r]
        mat[r][t-sum_small] = ord(s[t])-ord('a')
    i = 0
    for j in range(0, line_len[0]):
        for i in range(0, k):
            if k * j + i < l_s:  # !
                ans += chr(mat[i][j] + ord('a'))
    '''for j in range(0, line_length):
        for i in range(0, len(s)):
            if i % line_length == j:
                ans += s[i]
    '''
    return ans

'''def decrypt(s, k):
    l_s = len(s)
    mat = []
    #注意分类讨论
    if l_s % k == 0:
        n_col = l_s // k
    else:
        n_col = l_s // k+1
    for i in range(0, k):
        line = []
        for j in range(0, n_col):
            line.append(0)
        mat.append(line)
    for i in range(0, l_s):
        mat[i//n_col][i%n_col] = ord(s[i])-ord('a')
    ans = ''
    for i in range(0, k):
        for j in range(0, n_col):
            print(chr(mat[i][j]+ord('a')), end = '')
        print()
    for j in range(0, n_col):
        for i in range(0, k):
            if i*n_col+j < l_s:#!
                ans += chr(mat[i][j]+ord('a'))
    return ans'''


def main():
    k = eval(input().strip())
    s = input().strip()
    mode = eval(input().strip())

    if mode == 1:
        print(encrypt(s, k))
    else:
        print(decrypt(s, k))


if __name__ == '__main__':
    with PyCallGraph(output=GraphvizOutput()):
        main()
#解密 数组记录每行长度
#错误原因 算法写错了 毕竟是对角线
#11 10 10