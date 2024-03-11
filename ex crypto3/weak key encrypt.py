def ip(s):
    #st = str(bin(s))[2:]
    st = str(bin(s))[2:]
    while len(st) < 64:
        st = '0'+st
    anst = [0]*64
    subtable = [58, 50, 42, 34, 26, 18, 10,  2, 60, 52, 44, 36, 28, 20, 12,  4,
62, 54, 46, 38, 30, 22, 14,  6, 64, 56, 48, 40, 32, 24, 16,  8,
57, 49, 41, 33, 25, 17,  9,  1, 59, 51, 43, 35, 27, 19, 11,  3,
61, 53, 45, 37, 29, 21, 13,  5, 63, 55, 47, 39, 31, 23, 15,  7]
    ans = ''
    for i in range(0, 64):
        #anst[i] = st[subtable[i]-1]
        anst[i] = st[subtable[i] - 1]
    for i in range(0, 64):
        ans += anst[i]
    ans = '0b'+ans
    #return int(ans)注意进制转换
    return eval(ans)#已验证正确


def ipreverse(s):
    st = str(bin(s))[2:]
    while len(st) < 64:
        st = '0'+st
    anst = [0]*64
    rsubtable = [40,  8, 48, 16, 56, 24, 64, 32, 39,  7, 47, 15, 55, 23, 63, 31,
38,  6, 46, 14, 54, 22, 62, 30, 37,  5, 45, 13, 53, 21, 61, 29,
36,  4, 44, 12, 52, 20, 60, 28, 35,  3, 43, 11, 51, 19, 59, 27,
34,  2, 42, 10, 50, 18, 58, 26, 33,  1, 41,  9, 49, 17, 57, 25]
    ans = ''
    for i in range(0, 64):
        #anst[i] = st[rsubtable[i]]
        anst[i] = st[rsubtable[i]-1]
    for i in range(0, 64):
        ans += anst[i]
    ans = '0b' + ans
    return eval(ans)#正确
#！左右交换实现


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
    #print("{:#x}".format(k^r))
    ans = s_map(k^r)
    ans = p(ans)
    return ans#正确


def encrypt(s, k):
    x = ip(s)
    l0 = x>>32
    #print("%32x"%l0)
    r0 = x%int(pow(2,32))
    #print("%32x" % r0)
    #print("%32x" % p(s_map((E(r0)^key_generating(k, 1)))))
    for i in range(1, 17):
        l = x%int(pow(2,32))
        #r = (x>>8)^func(x%256,k[i])
        #r = (x >> 8) ^ func(x % 256, key_generating(k, i))
        r = (x >> 32) ^ func(x % int(pow(2,32)), key_generating(k, i))
        #print("%32x"%r)
        #print("{:#x}".format(key_generating(k, i)))
        x = (l<<32)+r
        #print("{:#x}".format(x))
    #ans = (x<<8)+(x>>8)#注意移位
    #ans = (x << 32) + (x >> 32)  # 注意移位 不等同于交换
    ans = ((x << 32) + (x >> 32))%int(pow(2, 64))
    #print("{:#x}".format(ans))
    ans = ipreverse(ans)
    return ans


#def decrypt(s, k, t):
def decrypt(s, k):
    #x = ip(s)
    x = ip(s)#正确
    l0 = x % int(pow(2, 32))
    r0 = x >> 32
    for i in range(1, 17):
        #l = x % 256
        #r = (x >> 8) ^ func(x % 256, k[17 - i])
        #r = (x >> 8) ^ func(x % 256, key_generating(k, 17-i))
        r = l0
        l = r0 ^ func(r, key_generating(k, 17-i))
        #x = (l << 8) + r
        l0 = l
        r0 = r
        #print('{:#x}'.format((l<<32)+r))
    #ans = ((x << 32) + (x >> 32)) % int(pow(2, 64))
    #ans = ipreverse(ans)
    #ans = ((x << 32) + (x >> 32)) % int(pow(2, 64))
    #ans = ((r<<32)+l)%int(pow(2, 64))
    ans = ((l<<32)+r)%int(pow(2, 64))
    ans = ipreverse(ans)
    return ans


weak_key = ['0101010101010101', '01010101fefefefe', 'fefefefe01010101', 'fefefefefefefefe', '0000000000000000', '00000000ffffffff', 'ffffffff00000000', 'ffffffffffffffff']
semi_key = ['011f011f010e010e', '1f011f010e010e01', '01e001e001f101f1', 'e001e001f101f101', '01fe01fe01fe01fe', 'fe01fe01fe01fe01', '1fe01fe00ef10ef1', 'e01fe01ff10ef10e', '1ffe1ffe0efe0efe', 'fe1ffe1ffe0efe0e', 'e0fee0fef1fef1fe', 'fee0fee0fef1fef1', '001e001e000f000f', '1e001e000f000f00', '00e100e100f000f0', 'e100e100f000f000', '00ff00ff00ff00ff', 'ff00ff00ff00ff00', '1ee11ee10ff00ff0', 'e11ee11ef00ff00f', '1eff1eff0fff0fff', 'ff1eff1eff0fff0f', 'e1ffe1fff0fff0ff', 'ffe1ffe1fff0fff0']
s = 0x02468aceeca86420
key1 = eval('0x'+semi_key[0])
key2 = eval('0x'+semi_key[1])
print('0x', end='')
print("%016x"%encrypt(encrypt(s, key1), key2))
