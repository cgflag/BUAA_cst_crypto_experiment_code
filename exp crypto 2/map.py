from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput


def exgcd(a, b):
    r, s, t = a, 1, 0
    r1, s1, t1 = b, 0, 1
    while r1 != 0:
        q = r // r1
        temp1, temp2, temp3 = r - q * r1, s - q * s1, t - q * t1
        r, s, t = r1, s1, t1
        r1, s1, t1 = temp1, temp2, temp3
    if b < 0:
        r, s, t = -r, -s, -t
    return r, s, t


def invmod(a, n):
    g, _, _ = exgcd(a, n)
    if g == 1:
        _, x, _ = exgcd(a, n)
    return x%n

def map_encrypt(m, k, b):
    ans = ''
    for i in range(0, len(m)):
        t = (k*(ord(m[i])-ord('a'))+b)%26
        ans += chr(t+ord('a'))
    return ans


def map_decrypt(c, k, b):
    ans = ''
    k1 = invmod(k, 26)
    for i in range(0, len(c)):
        t = ((ord(c[i])-ord('a')-b)*k1) % 26
        ans += chr(t+ord('a'))
    return ans


def main():
    s_num = input().strip()
    massage = input().strip()
    mode = eval(input().strip())
    s_n1, s_n2 = s_num.split(' ')
    k = eval(s_n1)
    b = eval(s_n2)

    if k == 2 or k == 13:
        print("invalid key")
    else:
        if mode == 0:
            print(map_decrypt(massage, k, b))
        elif mode == 1:
            print(map_encrypt(massage, k, b))
if __name__ == '__main__':
    with PyCallGraph(output=GraphvizOutput()):
        main()