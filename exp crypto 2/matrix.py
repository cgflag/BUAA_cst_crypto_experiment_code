from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput


def encrypt(s, k):
    n = len(k)
    l_s = len(s)
    ans = ''
    for j in range(1, n+1):
        for i in range(0, l_s):
            if eval(k[i%n]) == j:
                ans += s[i]
    return ans


def decrypt(s, k):
    n = len(k)
    l_s = len(s)
    ans = ''
    mat = []
    n_line = l_s//n
    for i in range(0, n_line):
        line = []
        for j in range(0, n):
            line.append(0)
        mat.append(line)
    for t in range(0, l_s):
        for j in range(0, n):
            if eval(k[j]) == (t//n_line)+1:
                mat[t%n_line][j] = ord(s[t])-ord('a')
    '''mat1 = []
    for i in range(0, n_line):
        line = []
        for j in range(0, n):
            line.append(chr(mat[i][j]+ord('a')))
        mat1.append(line)
    print(mat1)'''
    for i in range(0, n_line):
        for j in range(0, n):
            ans += chr(mat[i][j]+ord('a'))
    return ans


def main():
    n = eval(input().strip())
    k = input().strip()
    massage = input().strip()
    mode = eval(input().strip())

    if mode == 0:
        print(decrypt(massage, k))
    elif mode == 1:
        print(encrypt(massage, k))
#把消息一行一行读成矩阵块，按列读出，但是打乱列的次序
if __name__ == '__main__':
    with PyCallGraph(output=GraphvizOutput()):
        main()