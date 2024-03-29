from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput


logTable = [
		0x00, 0xff, 0xc8, 0x08, 0x91, 0x10, 0xd0, 0x36,
		0x5a, 0x3e, 0xd8, 0x43, 0x99, 0x77, 0xfe, 0x18,
		0x23, 0x20, 0x07, 0x70, 0xa1, 0x6c, 0x0c, 0x7f,
		0x62, 0x8b, 0x40, 0x46, 0xc7, 0x4b, 0xe0, 0x0e,
		0xeb, 0x16, 0xe8, 0xad, 0xcf, 0xcd, 0x39, 0x53,
		0x6a, 0x27, 0x35, 0x93, 0xd4, 0x4e, 0x48, 0xc3,
		0x2b, 0x79, 0x54, 0x28, 0x09, 0x78, 0x0f, 0x21,
		0x90, 0x87, 0x14, 0x2a, 0xa9, 0x9c, 0xd6, 0x74,
		0xb4, 0x7c, 0xde, 0xed, 0xb1, 0x86, 0x76, 0xa4,
		0x98, 0xe2, 0x96, 0x8f, 0x02, 0x32, 0x1c, 0xc1,
		0x33, 0xee, 0xef, 0x81, 0xfd, 0x30, 0x5c, 0x13,
		0x9d, 0x29, 0x17, 0xc4, 0x11, 0x44, 0x8c, 0x80,
		0xf3, 0x73, 0x42, 0x1e, 0x1d, 0xb5, 0xf0, 0x12,
		0xd1, 0x5b, 0x41, 0xa2, 0xd7, 0x2c, 0xe9, 0xd5,
		0x59, 0xcb, 0x50, 0xa8, 0xdc, 0xfc, 0xf2, 0x56,
		0x72, 0xa6, 0x65, 0x2f, 0x9f, 0x9b, 0x3d, 0xba,
		0x7d, 0xc2, 0x45, 0x82, 0xa7, 0x57, 0xb6, 0xa3,
		0x7a, 0x75, 0x4f, 0xae, 0x3f, 0x37, 0x6d, 0x47,
		0x61, 0xbe, 0xab, 0xd3, 0x5f, 0xb0, 0x58, 0xaf,
		0xca, 0x5e, 0xfa, 0x85, 0xe4, 0x4d, 0x8a, 0x05,
		0xfb, 0x60, 0xb7, 0x7b, 0xb8, 0x26, 0x4a, 0x67,
		0xc6, 0x1a, 0xf8, 0x69, 0x25, 0xb3, 0xdb, 0xbd,
		0x66, 0xdd, 0xf1, 0xd2, 0xdf, 0x03, 0x8d, 0x34,
		0xd9, 0x92, 0x0d, 0x63, 0x55, 0xaa, 0x49, 0xec,
		0xbc, 0x95, 0x3c, 0x84, 0x0b, 0xf5, 0xe6, 0xe7,
		0xe5, 0xac, 0x7e, 0x6e, 0xb9, 0xf9, 0xda, 0x8e,
		0x9a, 0xc9, 0x24, 0xe1, 0x0a, 0x15, 0x6b, 0x3a,
		0xa0, 0x51, 0xf4, 0xea, 0xb2, 0x97, 0x9e, 0x5d,
		0x22, 0x88, 0x94, 0xce, 0x19, 0x01, 0x71, 0x4c,
		0xa5, 0xe3, 0xc5, 0x31, 0xbb, 0xcc, 0x1f, 0x2d,
		0x3b, 0x52, 0x6f, 0xf6, 0x2e, 0x89, 0xf7, 0xc0,
		0x68, 0x1b, 0x64, 0x04, 0x06, 0xbf, 0x83, 0x38,
	]
expTable = [
		0x01, 0xe5, 0x4c, 0xb5, 0xfb, 0x9f, 0xfc, 0x12,
		0x03, 0x34, 0xd4, 0xc4, 0x16, 0xba, 0x1f, 0x36,
		0x05, 0x5c, 0x67, 0x57, 0x3a, 0xd5, 0x21, 0x5a,
		0x0f, 0xe4, 0xa9, 0xf9, 0x4e, 0x64, 0x63, 0xee,
		0x11, 0x37, 0xe0, 0x10, 0xd2, 0xac, 0xa5, 0x29,
		0x33, 0x59, 0x3b, 0x30, 0x6d, 0xef, 0xf4, 0x7b,
		0x55, 0xeb, 0x4d, 0x50, 0xb7, 0x2a, 0x07, 0x8d,
		0xff, 0x26, 0xd7, 0xf0, 0xc2, 0x7e, 0x09, 0x8c,
		0x1a, 0x6a, 0x62, 0x0b, 0x5d, 0x82, 0x1b, 0x8f,
		0x2e, 0xbe, 0xa6, 0x1d, 0xe7, 0x9d, 0x2d, 0x8a,
		0x72, 0xd9, 0xf1, 0x27, 0x32, 0xbc, 0x77, 0x85,
		0x96, 0x70, 0x08, 0x69, 0x56, 0xdf, 0x99, 0x94,
		0xa1, 0x90, 0x18, 0xbb, 0xfa, 0x7a, 0xb0, 0xa7,
		0xf8, 0xab, 0x28, 0xd6, 0x15, 0x8e, 0xcb, 0xf2,
		0x13, 0xe6, 0x78, 0x61, 0x3f, 0x89, 0x46, 0x0d,
		0x35, 0x31, 0x88, 0xa3, 0x41, 0x80, 0xca, 0x17,
		0x5f, 0x53, 0x83, 0xfe, 0xc3, 0x9b, 0x45, 0x39,
		0xe1, 0xf5, 0x9e, 0x19, 0x5e, 0xb6, 0xcf, 0x4b,
		0x38, 0x04, 0xb9, 0x2b, 0xe2, 0xc1, 0x4a, 0xdd,
		0x48, 0x0c, 0xd0, 0x7d, 0x3d, 0x58, 0xde, 0x7c,
		0xd8, 0x14, 0x6b, 0x87, 0x47, 0xe8, 0x79, 0x84,
		0x73, 0x3c, 0xbd, 0x92, 0xc9, 0x23, 0x8b, 0x97,
		0x95, 0x44, 0xdc, 0xad, 0x40, 0x65, 0x86, 0xa2,
		0xa4, 0xcc, 0x7f, 0xec, 0xc0, 0xaf, 0x91, 0xfd,
		0xf7, 0x4f, 0x81, 0x2f, 0x5b, 0xea, 0xa8, 0x1c,
		0x02, 0xd1, 0x98, 0x71, 0xed, 0x25, 0xe3, 0x24,
		0x06, 0x68, 0xb3, 0x93, 0x2c, 0x6f, 0x3e, 0x6c,
		0x0a, 0xb8, 0xce, 0xae, 0x74, 0xb1, 0x42, 0xb4,
		0x1e, 0xd3, 0x49, 0xe9, 0x9c, 0xc8, 0xc6, 0xc7,
		0x22, 0x6e, 0xdb, 0x20, 0xbf, 0x43, 0x51, 0x52,
		0x66, 0xb2, 0x76, 0x60, 0xda, 0xc5, 0xf3, 0xf6,
		0xaa, 0xcd, 0x9a, 0xa0, 0x75, 0x54, 0x0e, 0x01,
	]


def mutiply(a, b):
	#ans = 0
	#p = 0xe5
	#digit_1 = p.bit_length()-1
	#while b > 0:
		#if b & 1 == 1:
			#ans = ans ^ a
		#a, b = a << 1, b >> 1
		#if a >> digit_1:  # 取出 a 的最高位
			#a = a ^ p
	#return ans%256'
	ans = 0
	poly = 0xe5
	digit_1 = poly.bit_length() - 1
	while b:
		if b & 1:
			ans = ans ^ a
		a, b = a << 1, b >> 1
		if a >> digit_1:  # 取出 a 的最高位
			a = a ^ poly
	return ans


def gfdiv(a, b):
    if b == 0:
        return
    ans = 0
    bl_a = a.bit_length()
    bl_b = b.bit_length()
    while bl_a >= bl_b:
        sub = bl_a-bl_b
        a ^= (b <<sub)
        ans |= (1 <<sub)
        bl_a = a.bit_length()
    return ans


def gfmod(a, b):
    if b == 0:
        return
    ans = 0
    bl_a = a.bit_length()
    bl_b = b.bit_length()
    while bl_a >= bl_b:
        sub = bl_a-bl_b
        a ^= (b <<sub)
        ans |= (1 <<sub)
        bl_a = a.bit_length()
    return  a

def str2hex(s):
    odata = 0;
    su =s.upper()
    for c in su:
        tmp=ord(c)
        if tmp <= ord('9') :
            odata = odata << 4
            odata += tmp - ord('0')
        elif ord('A') <= tmp <= ord('F'):
            odata = odata << 4
            odata += tmp - ord('A') + 10
    return odata


def gfExgcd(a, b):
    r, x, y = a, 1, 0
    r1, x1, y1 = b, 0, 1
    while r1 != 0:
        #q = gfdiv(r, r1)
        q = gfdiv(r, r1)
        #temp1, temp2, temp3 = gfmod(r, r1), x - q * x1, y - q * y1
        #temp1, temp2, temp3 = gfmod(r, r1), x ^ (q * x1), y ^ (q * y1)
        temp1, temp2, temp3 = gfmod(r, r1), x ^ mutiply(q, x1), y ^ mutiply(q, y1)
        #temp1, temp2, temp3 = r - q * r1, x - q * x1, y - q * y1
        r, x, y = r1, x1, y1
        r1, x1, y1 = temp1, temp2, temp3
    #return r, x % 255, y % 255
    #return r, x , y
    return abs(r)%255, abs(x)%255, abs(y)%255


def initiate():
    ans = []
    for i in range(0, 16):
        line = []
        for j in range(0, 16):
            line.append(i*16+j)
        ans.append(line)
    return ans


def gfinvmod(a, m):
    k, c, _ = gfExgcd(a, m)
    if k == 1:
        return c%m
    else:
        return


def inverse(mat):
    ans = []
    for i in range(len(mat)):
        line = []
        for j in range(len(mat[i])):
            if mat[i][j] != 0:
                #line.append(gfinvmod(mat[i][j], 0xe5))
                #line.append(gfinvmod(mat[i][j], 0x11d))
                #line.append(gfinvmod(mat[i][j], 0x11b))
                line.append(expTable[255-logTable[mat[i][j]]])
            else:
                line.append(0)
        ans.append(line)
    return ans


def bytemap(n):
    s_c = '01100011'
    b = 0
    s_b = ''
    li_b = [0]*8
    s_n = ''

    s_n = str(bin(n))[2:]
    while len(s_n) < 8:
        s_n = '0'+s_n
    for i in range(8):
        li_b[i] = eval(s_n[i])^eval(s_n[(i-4)%8])^eval(s_n[(i-5)%8])^eval(s_n[(i-6)%8])^eval(s_n[(i-7)%8])^eval(s_c[i])
    s_n = ''
    #for i in range(7, -1, -1):
    for i in range(8):
        s_n += str(li_b[i])
    return eval('0b'+s_n)


#?二维列表 一维下标？
def reverse(mat):
    t = []
    for i in range(16):
        line = []
        for j in range(16):
            line.append(0)
        t.append(line)

    for i in range(256):
        t[mat[i//16][i % 16]//16][mat[i//16][i % 16]%16] = i
    return t


def main():
    ori = initiate()
    for i in range(len(ori)):
        for j in range(len(ori[i])):
            print('0x', end='')
            print("{:02x}".format(ori[i][j]), end = ' ')
        print()

    print()
    mat = inverse(ori)
    for i in range(16):
        for j in range(16):
            print('0x', end='')
            print("{:02x}".format(mat[i][j]), end = ' ')
        print()
    #print(len(mat))

    print()
    s_box = []
    for i in range(len(mat)):
        line = []
        for j in range(len(mat[i])):
            line.append(bytemap(mat[i][j]))
        s_box.append(line)
    for i in range(16):
        for j in range(16):
            print('0x', end='')
            #print("{:02x}".format(s_box[i][j]), end = ' ')
            print("{:02x}".format(s_box[i][j]), end = ',')
        print()

    print()
    #print(s_box)
    r_s_box = reverse(s_box)
    for i in range(16):
        for j in range(16):
            print('0x', end='')
            #print("{:02x}".format(r_s_box[i][j]), end = ' ')
            print("{:02x}".format(r_s_box[i][j]), end=', ')
        print()
#求逆元错了


if __name__ == '__main__':
    with PyCallGraph(output=GraphvizOutput()):
        main()