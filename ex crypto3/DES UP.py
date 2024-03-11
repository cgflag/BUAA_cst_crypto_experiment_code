def ip(s):
    mask = []
    mask0 = 0x8000000000000000
    for i in range(0, 64):
        mask.append(mask0>>i)
    subtable = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
                62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
                57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
                61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]
    ans = 0
    for i in range(64):
        #b[subtable[i-1]] = (s&mask[i])>>(63-subtable[i-1])
        ans |= ((s&mask[subtable[i]-1])>>(64-subtable[i]))<<(63-i)
    return ans



def ipreverse(s):
    mask = []
    mask0 = 0x8000000000000000
    for i in range(0, 64):
        mask.append(mask0 >> i)
    rsubtable = [40,  8, 48, 16, 56, 24, 64, 32, 39,  7, 47, 15, 55, 23, 63, 31,
38,  6, 46, 14, 54, 22, 62, 30, 37,  5, 45, 13, 53, 21, 61, 29,
36,  4, 44, 12, 52, 20, 60, 28, 35,  3, 43, 11, 51, 19, 59, 27,
34,  2, 42, 10, 50, 18, 58, 26, 33,  1, 41,  9, 49, 17, 57, 25]
    ans = 0
    for i in range(64):
        # b[subtable[i-1]] = (s&mask[i])>>(63-subtable[i-1])
        ans |= ((s&mask[rsubtable[i]-1])>>(64-rsubtable[i]))<<(63-i)
    return ans#正确
#！左右交换实现


#def E(r):
    #return eval(rbin[31]+rbin[0:4]+rbin[4]+rbin[3]+rbin[4:8]+rbin[8]+rbin[7]+rbin[8:12]+rbin[12]+rbin[11]+rbin[12:16]+rbin[16]+rbin[15]+rbin[16:20]+rbin[20]+rbin[19]+rbin[20:24]+rbin[24]+rbin[23]+rbin[24:28]+rbin[28]+rbin[27]+rbin[28:32]+rbin[0])

    #return eval('0b'+rbin[31]+rbin[0:4]+rbin[4]+rbin[3]+rbin[4:8]+rbin[8]+rbin[7]+rbin[8:12]+rbin[12]+rbin[11]+rbin[12:16]+rbin[16]+rbin[15]+rbin[16:20]+rbin[20]+rbin[19]+rbin[20:24]+rbin[24]+rbin[23]+rbin[24:28]+rbin[28]+rbin[27]+rbin[28:32]+rbin[0])
#    return ((r&1)<<47)|((r&0xf0000000)<<15)|((r&0x08000000)<<15) |(((r&0x10000000)|(r&0x0f000000)|(r&0x00800000))<<13) |(((r&0x01000000)|(r&0x00f00000)|(r&0x00080000))<<11) |(((r&0x00100000)|(r&0x000f0000)|(r&0x000080000))<<9) |(((r&0x00010000)|(r&0x0000f000)|(r&0x00000800))<<7) |(((r&0x00001000)|(r&0x00000f00)|(r&0x00000080))<<5) |(((r&0x00000100)|(r&0x000000f0)|(r&0x00000008))<<3) |(((r&0x00000010)|(r&0x0000000f))<<1)|((r&0x80000000)>>31)
def E(r):
    rbin = str(bin(r))[2:]
    while len(rbin) < 32:
        rbin = '0'+rbin
    #return eval(rbin[31]+rbin[0:4]+rbin[4]+rbin[3]+rbin[4:8]+rbin[8]+rbin[7]+rbin[8:12]+rbin[12]+rbin[11]+rbin[12:16]+rbin[16]+rbin[15]+rbin[16:20]+rbin[20]+rbin[19]+rbin[20:24]+rbin[24]+rbin[23]+rbin[24:28]+rbin[28]+rbin[27]+rbin[28:32]+rbin[0])
    return eval('0b'+rbin[31]+rbin[0:4]+rbin[4]+rbin[3]+rbin[4:8]+rbin[8]+rbin[7]+rbin[8:12]+rbin[12]+rbin[11]+rbin[12:16]+rbin[16]+rbin[15]+rbin[16:20]+rbin[20]+rbin[19]+rbin[20:24]+rbin[24]+rbin[23]+rbin[24:28]+rbin[28]+rbin[27]+rbin[28:32]+rbin[0])


def key_generating(k, round):
    key_shift = [0, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    key_subtitution1 = [57, 49, 41, 33, 25, 17,  9,  1, 58, 50, 42, 34, 26, 18,
10,  2, 59, 51, 43, 35, 27, 19, 11,  3, 60, 52, 44, 36,
63, 55, 47, 39, 31, 23, 15,  7, 62, 54, 46, 38, 30, 22,
14,  6, 61, 53, 45, 37, 29, 21, 13,  5, 28, 20, 12,  4]
    key_subtitution2 = [14, 17, 11, 24,  1,  5,  3, 28, 15,  6, 21, 10,
23, 19, 12,  4, 26,  8, 16,  7, 27, 20, 13,  2,
41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
    kt = str(bin(k))[2:]

    while len(kt) < 64:
        kt = '0'+kt

    #changed_pt = [0]*64
    changed_p = ''
    #for i in range(0, 64):
    #for i in range(0, 56):
        #changed_pt[i] = kt[key_subtitution1[i]]
        #changed_pt[i] = kt[key_subtitution1[i]-1]
    for i in key_subtitution1:
        changed_p += kt[i-1]
    #for i in range(0, 64):
        #if changed_pt[i] != 0:
         #   changed_p += changed_pt[i]
    l = changed_p[0:28]
    r = changed_p[28:]
    for i in range(1, round+1):#!1开头
        #l = l[key_shift[i]:]+l[:key_shift[i]]
        l = l[key_shift[i]:28] + l[0:key_shift[i]]
        #r = r[key_shift[i]:]+r[:key_shift[i]]
        r = r[key_shift[i]:28] + r[0:key_shift[i]]
    changed_p = l+r
    ans = ''
    k = [0]*56
    #for i in range(48):
        #k[i] = changed_p[key_subtitution2[i]]
    #    k[i] = changed_p[key_subtitution2[i]-1]
    #changed_p = ''
    #for i in range(0, 56):
    #    if k[i] != 0:
    #        changed_p += k[i]
    for i in key_subtitution2:
        ans += changed_p[i-1]
    return eval('0b'+ans)


def s_map(n):
    s_n = str(bin(n))[2:]
    while len(s_n) < 48:
        s_n = '0'+s_n
    sbox = []
    sbox1 = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    sbox2 = [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    sbox3 = [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    sbox4 = [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    sbox5 = [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    sbox6 = [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    sbox7 = [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    sbox8 = [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    sbox.append(sbox1)
    sbox.append(sbox2)
    sbox.append(sbox3)
    sbox.append(sbox4)
    sbox.append(sbox5)
    sbox.append(sbox6)
    sbox.append(sbox7)
    sbox.append(sbox8)
    #?高低位
    list_ = ''
    for i in range(0, 8):
        line = 2*eval(s_n[6*i])+eval(s_n[6*i+5])
        col = 8*eval(s_n[6*i+1])+4*eval(s_n[6*i+2])+2*eval(s_n[6*i+3])+eval(s_n[6*i+4])
        #list_ += str(bin(sbox[i][line][col]))[2:]
        temp = str(bin(sbox[i][line*16+col]))[2:]
        while len(temp) < 4:
            temp = '0'+temp
        list_ += temp#!长度可能不够
    #return eval(list_)
    return eval('0b'+list_)#正确


def p(s):
    pbox = [16,  7, 20, 21, 29, 12, 28, 17,  1, 15, 23, 26,  5, 18, 31, 10,
 2,  8, 24, 14, 32, 27,  3,  9, 19, 13, 30,  6, 22, 11,  4, 25]
    st = str(bin(s))[2:]
    while len(st) < 32:
        st = '0'+st
    anst = [0] * 32
    ans = ''
    for i in range(0, 32):
        anst[i] = st[pbox[i]-1]
    for i in range(0, 32):
        ans += anst[i]
    return eval('0b'+ans)#正确


def func(r, k):
    r = E(r)
    ans = s_map(k^r)
    ans = p(ans)
    return ans#正确


def encrypt(s, k):
    x = ip(s)
    l0 = x>>32
    r0 = x&0x00000000ffffffff
    for i in range(1, 17):
        #l = x&0x00000000ffffffff
        l = x%(int(pow(2, 32)))
        #r = (x>>8)^func(x%256,k[i])
        #r = (x >> 8) ^ func(x % 256, key_generating(k, i))
        #r = (x >> 32) ^ func(x & 0x00000000ffffffff, key_generating(k, i))
        r = (x >> 32) ^ func(x%(int(pow(2, 32))), key_generating(k, i))
        #print("%#x"%key_generating(k, i))
        #if i == 3:
        #    print("%#x"%key_generating(k, i))
        #    print(hex(x & 0x00000000ffffffff))
        #    print(hex(x >> 32))
        #    print(func(x & 0x00000000ffffffff, key_generating(k, i)))
        #    print(r)
        #print(str(hex(l))+' '+str(hex(r)))
        x = (l<<32)+r
        #print("%x"%x)
    #ans = (x<<8)+(x>>8)#注意移位
    #ans = (x << 32) + (x >> 32)  # 注意移位 不等同于交换
    ans = ((x << 32) + (x >> 32))&0x00000000ffffffffffffffff
    ans = ipreverse(ans)
    return ans


t = eval(input().strip())
#s_s = input.strip()
s = eval(input().strip())
#s_k = input.strip()
k = eval(input().strip())
op = eval(input().strip())

if op == 1:
    ans = s
    for i in range(t):
        ans = encrypt(ans, k)
    #print('{:#016x}'.format(ans))?补0
    result = str(hex(ans))[2:]
    while len(result) < 16:
        result = '0'+result
    print('0x'+result)