from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput


def encrypt(t1, t2, m):
    ans = ''
    for i in range(0, len(m)):
        ans += t2[t1.index(m[i])]
    return ans


def decrypt(t1, t2, m):
    ans = ''
    for i in range(0, len(m)):
        ans += t1[t2.index(m[i])]
    return ans


def main():
    t1 = input().strip()
    t2 = input().strip()
    massage = input().strip()
    mode = eval(input().strip())

    if mode == 0:
        print(decrypt(t1, t2, massage))
    else:
        print(encrypt(t1, t2, massage))
if __name__ == '__main__':
    with PyCallGraph(output=GraphvizOutput()):
        main()