#加密 解密
#每10个的分析
#要使用字典类型吗？键值交集？
#有限与运算
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput


s_box = [[0x63,0x7c,0x77,0x7b,0xf2,0x6b,0x6f,0xc5,0x30,0x01,0x67,0x2b,0xfe,0xd7,0xab,0x76],
        [0xca,0x82,0xc9,0x7d,0xfa,0x59,0x47,0xf0,0xad,0xd4,0xa2,0xaf,0x9c,0xa4,0x72,0xc0],
        [0xb7,0xfd,0x93,0x26,0x36,0x3f,0xf7,0xcc,0x34,0xa5,0xe5,0xf1,0x71,0xd8,0x31,0x15],
        [0x04,0xc7,0x23,0xc3,0x18,0x96,0x05,0x9a,0x07,0x12,0x80,0xe2,0xeb,0x27,0xb2,0x75],
        [0x09,0x83,0x2c,0x1a,0x1b,0x6e,0x5a,0xa0,0x52,0x3b,0xd6,0xb3,0x29,0xe3,0x2f,0x84],
        [0x53,0xd1,0x00,0xed,0x20,0xfc,0xb1,0x5b,0x6a,0xcb,0xbe,0x39,0x4a,0x4c,0x58,0xcf],
        [0xd0,0xef,0xaa,0xfb,0x43,0x4d,0x33,0x85,0x45,0xf9,0x02,0x7f,0x50,0x3c,0x9f,0xa8],
        [0x51,0xa3,0x40,0x8f,0x92,0x9d,0x38,0xf5,0xbc,0xb6,0xda,0x21,0x10,0xff,0xf3,0xd2],
        [0xcd,0x0c,0x13,0xec,0x5f,0x97,0x44,0x17,0xc4,0xa7,0x7e,0x3d,0x64,0x5d,0x19,0x73],
        [0x60,0x81,0x4f,0xdc,0x22,0x2a,0x90,0x88,0x46,0xee,0xb8,0x14,0xde,0x5e,0x0b,0xdb],
         [0xe0,0x32,0x3a,0x0a,0x49,0x06,0x24,0x5c,0xc2,0xd3,0xac,0x62,0x91,0x95,0xe4,0x79],
        [0xe7,0xc8,0x37,0x6d,0x8d,0xd5,0x4e,0xa9,0x6c,0x56,0xf4,0xea,0x65,0x7a,0xae,0x08],
        [0xba,0x78,0x25,0x2e,0x1c,0xa6,0xb4,0xc6,0xe8,0xdd,0x74,0x1f,0x4b,0xbd,0x8b,0x8a],
        [0x70,0x3e,0xb5,0x66,0x48,0x03,0xf6,0x0e,0x61,0x35,0x57,0xb9,0x86,0xc1,0x1d,0x9e],
        [0xe1,0xf8,0x98,0x11,0x69,0xd9,0x8e,0x94,0x9b,0x1e,0x87,0xe9,0xce,0x55,0x28,0xdf],
        [0x8c,0xa1,0x89,0x0d,0xbf,0xe6,0x42,0x68,0x41,0x99,0x2d,0x0f,0xb0,0x54,0xbb,0x16]]


def gfmutiply(a, b):
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
    #!0
    if a != 0 and b != 0:
        return expTable[(logTable[a] + logTable[b]) % 255]
    else:
        return 0


def n2mat(n):
    mat = []
    pick = 0xff000000000000000000000000000000
    for i in range(4):
        line = []
        for j in range(4):
            line.append((n&pick)>>(120-8*(4*i+j)))
            pick >>= 8
        mat.append(line)
    return mat


def get_known_epsilon(w_cipher, t_cipher):
    ipsilon_list = []  #应该没问题
    #print(w_cipher, t_cipher)居然想等
    '''mat_w_cipher = n2mat(w_cipher)
    mat_t_cipher = n2mat(t_cipher)
    mat_ans = []
    for i in range(4):
        line = []
        for j in range(4):
            line.append(0)
        mat_ans.append(line)
    for i in range(4):
        for j in range(4):
            mat_ans[i][j] = mat_w_cipher[i][j] ^ mat_t_cipher[i][j]
            if mat_ans[i][j] != 0:
                ipsilon_list.append(mat_ans[i][j])'''
    sub = w_cipher ^ t_cipher
    pick = 0xff << 120
    for i in range(16):
        if sub & pick != 0:
            ipsilon_list.append((sub & pick)>>(120-8*i))
        pick >>= 8

    return ipsilon_list


def get_ep(wr, t_cipher, kind):
#intersection
#kind?

    wr_mat = n2mat(wr)
    #print(wr, t_cipher)输入为什么会
    known_epsilon_list = get_known_epsilon(wr, t_cipher)#到这没错了
    #print(known_epsilon_list)
    #for ele in known_epsilon_list:
        #print("%2x"%ele, end=' ')
    ep = []
    x_list = []
#以列为标准
    #cm_mat = [[2, 1, 1, 3], [3, 2, 1, 1], [1, 3, 2, 1], [1, 1, 3, 2]]
    #cm_mat = [[2, 1, 1, 3], [1, 1, 3, 2], [1, 3, 2, 1], [3, 2, 1, 1]]
    #00 10 20 30
    #cm_mat = [[2, 1, 1, 3], [1, 1, 3, 2], [1, 3, 2, 1], [3, 2, 1, 1]]
    cm_mat = [[2, 1, 1, 3], [2, 1, 1, 3], [2, 1, 1, 3], [2, 1, 1, 3]]
    '''iep = 0
    j = 0
    for row in range(4):
        iep = 0
        j = 0
        unitx = []
        unitep = []
        for iep in range(256):
            for j in range(256):
                #if s_box(j ^ gfmutiply(cm_mat[kind][row], iep)) == s_box(j) ^ known_epsilon_list[row]:
                print(iep, j)
                print(kind, end = '')
                print("kind")
                print(row)
                print(cm_mat[kind][row])
                if len(known_epsilon_list) != 0 and s_box[(j ^ gfmutiply(cm_mat[kind][row], iep))>>4][(j ^ gfmutiply(cm_mat[kind][row], iep))&0x0f] == s_box[j>>4][j&0x0f] ^ known_epsilon_list[row]:
                #报错最后一次变成【】
                    print(known_epsilon_list)
                    unitx.append(j)
                    unitep.append(iep)
        x_list.append(unitx)
        ep.append(unitep)'''
    known_ind = [[0, 3, 2, 1], [1, 0, 3, 2], [2, 1, 0, 3], [3, 2, 1, 0]]

    iep = 0
    j = 0
    unitx = []
    unitep = []
    for iep in range(256):
        for j in range(256):
            #if len(known_epsilon_list) != 0 and s_box[(j ^ gfmutiply(cm_mat[kind][0], iep))>>4][(j ^ gfmutiply(cm_mat[kind][0], iep))&0xf] == s_box[(j)>>4][(j)&0xf] ^ known_epsilon_list[known_ind[kind][0]]:
            if len(known_epsilon_list) != 0 and s_box[(j ^ gfmutiply(2, iep)) >> 4][
                (j ^ gfmutiply(2, iep)) & 0xf] == s_box[(j) >> 4][(j) & 0xf] ^ known_epsilon_list[
                known_ind[kind][0]]:
                unitx.append(j)
                unitep.append(iep)
    x_list.append(unitx)
    ep.append(unitep)

    iep = 0
    j = 0
    unitx = []
    unitep = []
    for iep in ep[0]:
        for j in range(256):#1怎么会没解呢？
            if len(known_epsilon_list) != 0 and s_box[(j ^ iep)>>4][(j ^ iep)&0xf] == s_box[(j)>>4][(j)&0xf] ^ known_epsilon_list[known_ind[kind][1]]:
                unitx.append(j)
                unitep.append(iep)
    x_list.append(unitx)
    ep.append(unitep)

    iep = 0
    j = 0
    unitx = []
    unitep = []
    for iep in ep[1]:
        for j in range(256):
            if len(known_epsilon_list) != 0 and s_box[(j ^ iep)>>4][(j ^ iep)&0xf] == s_box[(j)>>4][(j)&0xf] ^ known_epsilon_list[known_ind[kind][2]]:
                unitx.append(j)
                unitep.append(iep)
    x_list.append(unitx)
    ep.append(unitep)

#提供的有用思路
    iep = 0
    j = 0
    unitx = []
    unitep = []
    for iep in ep[2]:
        for j in range(256):
            if len(known_epsilon_list) != 0 and s_box[(j ^ gfmutiply(3, iep))>>4][(j ^ gfmutiply(3, iep))&0xf] == s_box[(j)>>4][(j)&0xf] ^ known_epsilon_list[known_ind[kind][3]]:
                unitx.append(j)
                unitep.append(iep)#怎么一个下表重复这么多遍
    x_list.append(unitx)
    ep.append(unitep)

    #ep_intersection = list(set(ep[0])&set(ep[1])&set(ep[2])&set(ep[3]))
    ep_intersection = ep[3]
    #求x
    '''x_list1 = []
    for k in range(4):
        unitx = []
        for iep in ep_intersection:
            for j in range(256):
                if len(known_epsilon_list) != 0 and s_box[(j ^ gfmutiply(cm_mat[kind][k], iep)) >> 4][(j ^ gfmutiply(cm_mat[kind][k], iep)) & 0xf] == s_box[(j) >> 4][(j) & 0xf] ^ known_epsilon_list[known_ind[kind][k]]:
                      unitx.append(j)
        x_list1.append(unitx)'''

    inde = []
    for i in range(4):
        unitind = []
        for j in range(len(ep[i])):
            if ep[i][j] in ep_intersection:
                unitind.append(j)
        inde.append(unitind)
    #列表赋值都变成0
    x_list1 = []
    x_list1.append([])
    x_list1.append([])
    x_list1.append([])
    x_list1.append([])

    for i in range(4):
        for j in range(len(inde[i])):
            x_list1[i].append(x_list[i][inde[i][j]])
    #print(x_list1)
    #return ep_intersection
    return x_list1


def get_common_x(mat_10_, t_cipher, kind):
    #print(mat_10_)
    old_x = get_ep(mat_10_[0], t_cipher, kind)
    #得到的x没有交集？
    #for i in range(1, 2):
    for i in range(1, 10):
        new_x = get_ep(mat_10_[i], t_cipher, kind)
        #for i in range(4):
        for j in range(4):
            old_x[j] = list(set(old_x[j])&set(new_x[j]))
        if len(old_x[0]) == 1 and len(old_x[1]) == 1 and len(old_x[2]) == 1 and len(old_x[3]) == 1:
            break
    return old_x


def get_keyseg(x_l, t_cipher, posi):
    #for ele in x_l:
        #print("%2x"%ele[0])得到公共x就不对
    if posi == 0:#x_l空集？类型也不对
        ans = 0#列排序
        ans |= ((((t_cipher >> 120)&0xff)^s_box[x_l[0][0]>>4][x_l[0][0]&0xf])<<120)|((((t_cipher >> 16)&0xff)^s_box[x_l[1][0]>>4][x_l[1][0]&0x0f])<<16)|((((t_cipher >> 40)&0xff)^s_box[x_l[2][0]>>4][x_l[2][0]&0x0f])<<40)|((((t_cipher >> 64)&0xff)^s_box[x_l[3][0]>>4][x_l[3][0]&0x0f])<<64)
    elif posi == 1:
        ans = 0
        '''ans |= ((((t_cipher >> 112) & 0xff) ^ s_box[x_l[0][0]>>4][x_l[0][0]&0x0f]) << 112) | (
                    (((t_cipher >> 88) & 0xff) ^ s_box[x_l[1][0]>>4][x_l[1][0]&0x0f]) << 88) | (
                           (((t_cipher >> 32) & 0xff) ^ s_box[x_l[2][0]>>4][x_l[2][0]&0x0f]) << 32) | (
                           (((t_cipher >> 8) & 0xff) ^ s_box[x_l[3][0]>>4][x_l[3][0]&0x0f]) << 8)'''
        ans |= ((((t_cipher >> 88) & 0xff) ^ s_box[x_l[0][0] >> 4][x_l[0][0] & 0x0f]) << 88) | (
                (((t_cipher >> 112) & 0xff) ^ s_box[x_l[1][0] >> 4][x_l[1][0] & 0x0f]) << 112) | (
                       (((t_cipher >> 32) & 0xff) ^ s_box[x_l[3][0] >> 4][x_l[3][0] & 0x0f]) << 32) | (
                       (((t_cipher >> 8) & 0xff) ^ s_box[x_l[2][0] >> 4][x_l[2][0] & 0x0f]) << 8)
    elif posi == 2:
        ans = 0
        '''ans |= ((((t_cipher >> 104) & 0xff) ^ s_box[x_l[2][0]>>4][x_l[2][0]&0x0f]) << 104) | (
                (((t_cipher >> 80) & 0xff) ^ s_box[x_l[1][0]>>4][x_l[1][0]&0x0f]) << 80) | (
                       (((t_cipher >> 28) & 0xff) ^ s_box[x_l[0][0]>>4][x_l[0][0]&0x0f]) << 28) | (
                       (((t_cipher >> 0) & 0xff) ^ s_box[x_l[3][0]>>4][x_l[3][0]&0x0f]) << 0)'''
        ans |= ((((t_cipher >> 104) & 0xff) ^ s_box[x_l[2][0] >> 4][x_l[2][0] & 0x0f]) << 104) | (
                (((t_cipher >> 80) & 0xff) ^ s_box[x_l[1][0] >> 4][x_l[1][0] & 0x0f]) << 80) | (
                       (((t_cipher >> 56) & 0xff) ^ s_box[x_l[0][0] >> 4][x_l[0][0] & 0x0f]) << 56) | (
                       (((t_cipher >> 0) & 0xff) ^ s_box[x_l[3][0] >> 4][x_l[3][0] & 0x0f]) << 0)
    else:
        ans = 0
        ans |= ((((t_cipher >> 96) & 0xff) ^ s_box[x_l[3][0]>>4][x_l[3][0]&0x0f]) << 96) | (
                (((t_cipher >> 72) & 0xff) ^ s_box[x_l[2][0]>>4][x_l[2][0]&0x0f]) << 72) | (
                       (((t_cipher >> 48) & 0xff) ^ s_box[x_l[1][0]>>4][x_l[1][0]&0x0f]) << 48) | (
                       (((t_cipher >> 24) & 0xff) ^ s_box[x_l[0][0]>>4][x_l[0][0]&0x0f]) << 24)
    return ans


def g(li, round):
    R_con = [0x01000000, 0x02000000, 0x04000000, 0x08000000, 0x10000000,
            0x20000000, 0x40000000, 0x80000000, 0x1b000000, 0x36000000]
    li = li[1:]+li[:1]
    in_ = (li[0]<<24)|(li[1]<<16)|(li[2]<<8)|li[3]
    ans = []
    #轮常量异或
    #s_map更改后有潜在错误输入输出位数
    n = (((s_box[li[0] >> 4][li[0] & 0xf])<<24)|((s_box[li[1] >> 4][li[1] & 0xf])<<16)|((s_box[li[2] >> 4][li[2] & 0xf])<<8)|((s_box[li[3] >> 4][li[3] & 0xf])<<0)) ^ R_con[round]
    #n = s_box[in_>>4][in_&0xf]^R_con[round]
    pick = 0xff
    move = 24
    for i in range(4):
        ans.append((n>>move)&pick)
        move -= 8
    return ans


def r_key_expand(key):#验证正确
    mat = []  # 第一轮没问题
    move = 120
    pick = 0xff
    for i in range(0, 4):
        line = []
        for j in range(4):
            line.append((key >> move) & pick)
            move -= 8
        mat.append(line)
    W = []
    for i in range(0, 44):
        word = []
        for j in range(0, 4):
            #word.append(mat[j][i])
            word.append(0)
        W.append(word)
    for i in range(43, 39, -1):
        for j in range(4):
            #W[i][j] = key[i-40][j]
            W[i][j] = mat[i - 40][j]
    for i in range(39, -1, -1):
        if i % 4 != 0:
            for j in range(4):
                W[i][j] = W[i+4][j]^W[i+3][j]
        else:
            for j in range(4):
                #W[i][j] = W[i+4][j] ^ g(W[i+3][j], i//4)[j]
                W[i][j] = W[i + 4][j] ^ g(W[i + 3], i // 4)[j]
    return W


def mat2n(mat):
    ans = 0
    move = 120
    for i in range(4):
        for j in range(4):
            #ans |= mat[j][i]<<move
            ans |= mat[i][j] << move
            move -= 8
    return ans


def main():
    mes = eval(input().strip())
    cipher = eval(input().strip())
    wrong_mat = []
    for i in range(16):
        wrong_line = []
        for j in range(10):
            wrong_line.append(eval(input().strip()))
        wrong_mat.append(wrong_line)


    #遍历 X0 e得到适应集合
    #错误密文异或正确密文
    #for i in range(16):
    #    for j in range(10):
    #输入返回类型确定 收敛速度
    #0 4 8 12 分别还原4个
    #每个4个方程解出
    #for i in range(4):
    #每次还原四个字节
    #get_key

    #print(get_common_x(wrong_mat[0], cipher))
    key = 0
    #print(wrong_mat)又一个与密文一样
    for i in range(4):
        x_l = get_common_x(wrong_mat[i], cipher, i)
        key |= get_keyseg(x_l, cipher, i)#多个key也行吗
    #print("%32x"%key)
    print('0x', end='')
    print("%032x"%mat2n(r_key_expand(key)[0:4]))
if __name__ == '__main__':
    with PyCallGraph(output=GraphvizOutput()):
        main()
'''


x_list = []
eps_list = []
for eps in range(256):
    for x in range(256):
        if s_box(x^gfmutiply(2, eps)) == s_box(x)^[0]:
            x_list.append(x)
            eps_list.append(eps)'''
