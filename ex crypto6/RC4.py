#如何读入 字节为单位？ 还有 k比明文长的情形？
import sys
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

'''def RC4(k, e_s):
    j = 0
    li_k = []
    pick = 0xff << (8 * (n - 1))
    for i in range(n):
        li_k.append((k & pick) >> (8 * (n - 1 - i)))
        pick >>= 8
    for i in range(n):
        j = (j + s[i]+ li_k[i])
        #到底模几？
        t = s[i]
        s[i] = s[j]
        s[j] = t

    i = 0
    j = 0
    while n1 > 0:
        n1 -= 1
        i = (i + 1) %
        j = (j + s[i]) %
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        t = (s[i] + s[j]) %
        sub_k = s[t]#类型 最终异或得'''


'''def RC4(key, e_s):
    key = key[2:]
    if len(key) % 2 == 1:
        key = '0' + key
    #print(key, end=' ')对
    n = len(key)//2
    key = eval('0x' + key)
    li_k = []
    pick = 0xff << (8 * (n - 1))
    for i in range(n):
        li_k.append((key & pick) >> (8 * (n - 1 - i)))
        pick >>= 8
    #print(li_k)
    s_box = list(range(256))
    j = 0
    for i in range(256):
        #j = (j + s_box[i] + key[i % len(key)]) % 256
        j = (j + s_box[i] + li_k[i % len(li_k)]) % 256
        s_box[i], s_box[j] = s_box[j], s_box[i]
    i = 0
    j = 0
    keystream = []
    for _ in range(len(e_s)):
        i = (i + 1) % 256
        j = (j + s_box[i]) % 256
        s_box[i], s_box[j] = s_box[j], s_box[i]
        k = s_box[(s_box[i] + s_box[j]) % 256]
        keystream.append(k)

    #ciphertext = []
    ciphertext = ''
    #for i in range(len(e_s)):
        #c = ord(e_s[i]) ^ keystream[i]
        ##ciphertext += chr(c)
        ##ciphertext += str(c)
        #ciphertext += hex(c)[2:]
        ##ciphertext.append(c)
    c = eval('0x'+e_s) ^ keystream[i]
    c = hex(c)[2:]
    while len(c) < 2:
        c = '0' + c
    ciphertext += c

    #return bytes(ciphertext)
    return ciphertext'''


#k = eval(input().strip())
def main():
    key = input().strip()

    sys.stdin.read(2)
    print()
    print("0x", end='')
    key = key[2:]
    if len(key) % 2 == 1:
        key = '0' + key
    # print(key, end=' ')对
    n = len(key) // 2
    key = eval('0x' + key)
    li_k = []
    pick = 0xff << (8 * (n - 1))
    for i in range(n):
        li_k.append((key & pick) >> (8 * (n - 1 - i)))
        pick >>= 8
    # print(li_k)
    s_box = list(range(256))#初始化
    j = 0
    for i in range(256):
        # j = (j + s_box[i] + key[i % len(key)]) % 256
        j = (j + s_box[i] + li_k[i % len(li_k)]) % 256
        s_box[i], s_box[j] = s_box[j], s_box[i]#初始置换

    i = 0
    j = 0

    while True:
        s = sys.stdin.read(2)
        if not s:
            break
        #s_n = eval('0x' + s)
        #逐字节操作
        i = (i + 1) % 256
        j = (j + s_box[i]) % 256
        s_box[i], s_box[j] = s_box[j], s_box[i]
        k = s_box[(s_box[i] + s_box[j]) % 256]

        ciphertext = ''
        c = eval('0x' + s) ^ k
        c = hex(c)[2:]
        while len(c) < 2:
            c = '0' + c
        ciphertext += c

        print(ciphertext, end='')

if __name__ == '__main__':
    with PyCallGraph(output=GraphvizOutput()):
        main()