from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput


def encrypt(s, k):
    ans = ''
    l_k = len(k)
    for i in range(0, len(s)):
        #ans += chr((ord(s[i])-33)^(ord(k[i%l_k])-33)+33)
        #ans += chr(((ord(s[i]) - 33) ^ (ord(k[i % l_k]) - 33))%94 + 33)
        #ans += chr(((ord(s[i])) ^ (ord(k[i % l_k]))) % 94 + 33)
        ans += chr(((ord(s[i])) ^ (ord(k[i % l_k]))))
    return ans


def decrypt(s, k):
    ans = ''
    l_k = len(k)
    for i in range(0, len(s)):
        ans += chr(((ord(s[i])) ^ (ord(k[i % l_k]))))
    return ans


def main():
    k = input().strip()
    s = input().strip()
    mode = eval(input().strip())

    if mode == 1:
        print(encrypt(s, k))
    else:
        print(decrypt(s, k))
if __name__ == '__main__':
    with PyCallGraph(output=GraphvizOutput()):
        main()