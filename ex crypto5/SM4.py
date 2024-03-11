from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput


SboxTable = [
    [0xd6, 0x90, 0xe9, 0xfe, 0xcc, 0xe1, 0x3d, 0xb7, 0x16, 0xb6, 0x14, 0xc2, 0x28, 0xfb, 0x2c, 0x05],
    [0x2b, 0x67, 0x9a, 0x76, 0x2a, 0xbe, 0x04, 0xc3, 0xaa, 0x44, 0x13, 0x26, 0x49, 0x86, 0x06, 0x99],
    [0x9c, 0x42, 0x50, 0xf4, 0x91, 0xef, 0x98, 0x7a, 0x33, 0x54, 0x0b, 0x43, 0xed, 0xcf, 0xac, 0x62],
    [0xe4, 0xb3, 0x1c, 0xa9, 0xc9, 0x08, 0xe8, 0x95, 0x80, 0xdf, 0x94, 0xfa, 0x75, 0x8f, 0x3f, 0xa6],
    [0x47, 0x07, 0xa7, 0xfc, 0xf3, 0x73, 0x17, 0xba, 0x83, 0x59, 0x3c, 0x19, 0xe6, 0x85, 0x4f, 0xa8],
    [0x68, 0x6b, 0x81, 0xb2, 0x71, 0x64, 0xda, 0x8b, 0xf8, 0xeb, 0x0f, 0x4b, 0x70, 0x56, 0x9d, 0x35],
    [0x1e, 0x24, 0x0e, 0x5e, 0x63, 0x58, 0xd1, 0xa2, 0x25, 0x22, 0x7c, 0x3b, 0x01, 0x21, 0x78, 0x87],
    [0xd4, 0x00, 0x46, 0x57, 0x9f, 0xd3, 0x27, 0x52, 0x4c, 0x36, 0x02, 0xe7, 0xa0, 0xc4, 0xc8, 0x9e],
    [0xea, 0xbf, 0x8a, 0xd2, 0x40, 0xc7, 0x38, 0xb5, 0xa3, 0xf7, 0xf2, 0xce, 0xf9, 0x61, 0x15, 0xa1],
    [0xe0, 0xae, 0x5d, 0xa4, 0x9b, 0x34, 0x1a, 0x55, 0xad, 0x93, 0x32, 0x30, 0xf5, 0x8c, 0xb1, 0xe3],
    [0x1d, 0xf6, 0xe2, 0x2e, 0x82, 0x66, 0xca, 0x60, 0xc0, 0x29, 0x23, 0xab, 0x0d, 0x53, 0x4e, 0x6f],
    [0xd5, 0xdb, 0x37, 0x45, 0xde, 0xfd, 0x8e, 0x2f, 0x03, 0xff, 0x6a, 0x72, 0x6d, 0x6c, 0x5b, 0x51],
    [0x8d, 0x1b, 0xaf, 0x92, 0xbb, 0xdd, 0xbc, 0x7f, 0x11, 0xd9, 0x5c, 0x41, 0x1f, 0x10, 0x5a, 0xd8],
    [0x0a, 0xc1, 0x31, 0x88, 0xa5, 0xcd, 0x7b, 0xbd, 0x2d, 0x74, 0xd0, 0x12, 0xb8, 0xe5, 0xb4, 0xb0],
    [0x89, 0x69, 0x97, 0x4a, 0x0c, 0x96, 0x77, 0x7e, 0x65, 0xb9, 0xf1, 0x09, 0xc5, 0x6e, 0xc6, 0x84],
    [0x18, 0xf0, 0x7d, 0xec, 0x3a, 0xdc, 0x4d, 0x20, 0x79, 0xee, 0x5f, 0x3e, 0xd7, 0xcb, 0x39, 0x48]
]

FK = [0xa3b1bac6, 0x56AA3350, 0x677d9197, 0xb27022dc]

CK = [
    0x00070e15, 0x1c232a31, 0x383f464d, 0x545b6269,
    0x70777e85, 0x8c939aa1, 0xa8afb6bd, 0xc4cbd2d9,
    0xe0e7eef5, 0xfc030a11, 0x181f262d, 0x343b4249,
    0x50575e65, 0x6c737a81, 0x888f969d, 0xa4abb2b9,
    0xc0c7ced5, 0xdce3eaf1, 0xf8ff060d, 0x141b2229,
    0x30373e45, 0x4c535a61, 0x686f767d, 0x848b9299,
    0xa0a7aeb5, 0xbcc3cad1, 0xd8dfe6ed, 0xf4fb0209,
    0x10171e25, 0x2c333a41, 0x484f565d, 0x646b7279
]


# def leftshift(a, n, size=32):
# 	a = list(bin(a)[2:])
# 	a = ["0"]*(size - len(a)) + a
# 	b = ['0']*32
# 	for i,x in enumerate(a):
# 		b[(i-n)%32] = a[i]
# 	return int("".join(b), 2)

def leftshift(a, n, size=32):
    n = n % size
    #return (a << n) | (a >> (size - n))
    return (((a << n) | (a >> (size - n)))&0xffffffff)


def PUT_ULONG_BE(b):
    b = sm4Sbox(b)
    return b ^ (leftshift(b, 13)) ^ (leftshift(b, 23))#线性变换


def GET_ULONG_BE(b):
    b = sm4Sbox(b)
    return b ^ (leftshift(b, 2)) ^ (leftshift(b, 10)) ^ (leftshift(b, 18)) ^ (leftshift(b, 24))#线性变换L


# def sm4Sbox(a):
# 	a1 = ("%08x"%a)[0:2]
# 	a2 = ("%08x"%a)[2:4]
# 	a3 = ("%08x"%a)[4:6]
# 	a4 = ("%08x"%a)[6:8]
# 	b1 = SboxTable[int(a1[0], 16)][int(a1[1], 16)]
# 	b2 = SboxTable[int(a2[0], 16)][int(a2[1], 16)]
# 	b3 = SboxTable[int(a3[0], 16)][int(a3[1], 16)]
# 	b4 = SboxTable[int(a4[0], 16)][int(a4[1], 16)]
# 	return int("%02x%02x%02x%02x"%(b1,b2,b3,b4), 16)

def sm4Sbox(a):
    b1 = SboxTable[(a & 0xf0000000) >> 28][(a & 0x0f000000) >> 24]
    b2 = SboxTable[(a & 0x00f00000) >> 20][(a & 0x000f0000) >> 16]
    b3 = SboxTable[(a & 0x0000f000) >> 12][(a & 0x00000f00) >> 8]
    b4 = SboxTable[(a & 0x000000f0) >> 4][(a & 0x0000000f) >> 0]
    return (b1 << 24) | (b2 << 16) | (b3 << 8) | (b4 << 0)


def generate_key(MK):
    K = [0] * 36#FK系统参数 CK固定参数
    rk = [0] * 32

    K[0] = MK[0] ^ FK[0]
    K[1] = MK[1] ^ FK[1]
    K[2] = MK[2] ^ FK[2]
    K[3] = MK[3] ^ FK[3]

    for i in range(32):
        K[i + 4] = K[i] ^ PUT_ULONG_BE(K[i + 1] ^ K[i + 2] ^ K[i + 3] ^ CK[i])#T'
        rk[i] = K[i + 4]
        #print("%8x"%rk[i])
    return rk


def Word2hex(Word_list):
    #print("%8x"%Word_list[0])
    return (Word_list[0] << 96)|(Word_list[1] << 64)|(Word_list[2] << 32)|(Word_list[3] << 0)


def sm4_encrypt(message, key, method='cbc'):
    MK = key
    X = message + [0] * 32
    rk = generate_key(MK)
    #rk 14字节
    '''print("%8x" % X[0])
    print("%8x" % X[1])
    print("%8x" % X[2])
    print("%8x" % X[3])'''

    for i in range(32):
        X[i + 4] = X[i] ^ GET_ULONG_BE(X[i + 1] ^ X[i + 2] ^ X[i + 3] ^ rk[i])
        #print("%8x" % X[i+4])
    # Y = [hex(X[35]), hex(X[34]), hex(X[33]), hex(X[32])]
    Y = [X[35], X[34], X[33], X[32]]
    #print(Y)
    return Y
    #32次迭代，一次反序


def sm4_decrypt(crphertext, key, method='cbc'):
    MK = key
    X = crphertext + [0] * 32
    rk = generate_key(MK)

    rk.reverse()

    for i in range(32):
        X[i + 4] = X[i] ^ GET_ULONG_BE(X[i + 1] ^ X[i + 2] ^ X[i + 3] ^ rk[i])

    # Y = [hex(X[35]), hex(X[34]), hex(X[33]), hex(X[32])]

    Y = [X[35], X[34], X[33], X[32]]#数组
    return Y


#if __name__ == '__main__':
    #time.clock() message k都是4*32数组
def main():
    T = eval(input().strip())
    s = eval(input().strip())
    k = eval(input().strip())
    op = eval(input().strip())

    if op == 1:
        ans = []
        s_li = []
        k_li = []
        pick = 0xffffffff000000000000000000000000
        for i in range(4):
            s_li.append((s&pick)>>(96-32*i))
            k_li.append((k & pick) >> (96 - 32 * i))
            pick >>= 32
        ans = s_li
        for x in range(T):
            #ciphertext = sm4_encrypt(s, k)
            ans = sm4_encrypt(ans, k_li)
    # message = map(lambda x:int(x[:-1], 16), ciphertext)
    # print ciphertext
        print("0x", end='')
        print("%032x" % Word2hex(ans))
        #time.clock()
        # ciphertext = [0x681edf34, 0xd206965e, 0x86b3e94f, 0x536e4246]
    else:
        s_li = []
        k_li = []
        pick = 0xffffffff000000000000000000000000
        for i in range(4):
            s_li.append((s & pick) >> (96 - 32 * i))
            k_li.append((k & pick) >> (96 - 32 * i))
            pick >>= 32
            ans = s_li
        for x in range(T):
            #ciphertext = sm4_encrypt(s, k)
            #ciphertext = sm4_decrypt(s_li, k_li)
            ans = sm4_decrypt(ans, k_li)
        print("0x", end='')
        #print("%032x" % Word2hex(ciphertext))
        print("%032x" % Word2hex(ans))

if __name__ == '__main__':
    with PyCallGraph(output=GraphvizOutput()):
        main()
