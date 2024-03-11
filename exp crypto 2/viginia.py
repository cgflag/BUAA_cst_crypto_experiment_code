from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput


def encrypt(k, s):
    ans = ''
    l_k = len(k)
    for i in range(0, len(s)):
        t = chr((ord(s[i])-ord('a')+ord(k[i%l_k])-ord('a'))%26+ord('a'))
        ans += t
    return ans


def decrypt(k, s):
    ans = ''
    l_k = len(k)
    for i in range(0, len(s)):
        #t = chr(ord(s[i]) - ord('a') - (ord(k[i % l_k]) - ord('a')) + ord('a'))
        t = chr((ord(s[i]) - ord('a') - (ord(k[i % l_k]) - ord('a'))) % 26 + ord('a'))
        ans += t
    return ans


def main():
    k = input().strip()
    s = input().strip()
    mode = eval(input().strip())

    if mode == 1:
        print(encrypt(k, s))
    else:
        print(decrypt(k, s))


if __name__ == '__main__':
    with PyCallGraph(output=GraphvizOutput()):
        main()