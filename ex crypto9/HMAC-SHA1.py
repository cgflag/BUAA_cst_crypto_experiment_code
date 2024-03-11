import struct
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

INITIAL_H = (0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0)
K = [
    0x5A827999,
    0x6ED9EBA1,
    0x8F1BBCDC,
    0xCA62C1D6,
]


def int2bytes(n, length):
    """将整数 n 转换为指定长度的字节数组"""
    b = bytearray()
    while n:
        b.append(n & 0xff)
        n >>= 8
    return bytes(bytearray(reversed(b)).rjust(length, b'\x00'))


def bytes2int(b):
    """将字节数组转换为整数"""
    return int.from_bytes(b, byteorder='big')


def rotate_left(x, n):
    return ((x << n) & 0xffffffff) | (x >> (32 - n))


def pad_data(data):
    bit_length = len(data) * 8
    data += b'\x80'
    while (len(data) + 8) % 64 != 0:
        data += b'\x00'
    data += struct.pack('>Q', bit_length)
    return data


def sha1(data):#没有问题
    data = pad_data(data)# 数据填充

    h = list(INITIAL_H)

    for i in range(0, len(data), 64):
        block = data[i:i+64]
        w = list(struct.unpack('>16L', block))

        for j in range(16, 80):
            temp = w[j-3] ^ w[j-8] ^ w[j-14] ^ w[j-16]
            w.append(rotate_left(temp, 1))

        a, b, c, d, e = h

        for j in range(80):
            if 0 <= j <= 19:
                f = (b & c) | ((~b) & d)
                k = K[0]
            elif 20 <= j <= 39:
                f = b ^ c ^ d
                k = K[1]
            elif 40 <= j <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = K[2]
            elif 60 <= j <= 79:
                f = b ^ c ^ d
                k = K[3]

            temp = (rotate_left(a, 5) + f + e + k + w[j]) % (2 ** 32)
            e = d
            d = c
            c = rotate_left(b, 30)
            b = a
            a = temp

        h[0] = (h[0] + a) % (2 ** 32)# 更新哈希值
        h[1] = (h[1] + b) % (2 ** 32)
        h[2] = (h[2] + c) % (2 ** 32)
        h[3] = (h[3] + d) % (2 ** 32)
        h[4] = (h[4] + e) % (2 ** 32)

    # 将哈希值转为十六进制字符串
    ans_ = ''.join([hex(i)[2:].zfill(8) for i in h])
    ans = bytes.fromhex(ans_)
    return ans


def HMAC(key, mes):
    #key类型
    mes = mes.encode('utf-8')
    l = len(key) // 2
    bytes_key = int2bytes(eval('0x'+key), l)
    #block_size = 20
    block_size = 64
    if len(bytes_key) > block_size:
        bytes_key = sha1(bytes_key)
        #bytes_key = int2bytes(eval('0x' + sha1(bytes_key)), l)
    elif len(key) < block_size:
        #bytes_key += b'\x00' * (block_size - len(key))
        bytes_key += b'\x00' * (block_size - len(bytes_key))

    #异或
    #o_pad = (block_size//8) * b'\x00\x11\x01\x10'
    #i_pad = (block_size//8) * b'\x01\x01\x11\x00'
    '''o_pad = (block_size) * b'\x36'
    i_pad = (block_size) * b'\x5c'

    i = bytes(a ^ b for a, b in zip(bytes_key, i_pad))
    o = bytes(a ^ b for a, b in zip(bytes_key, o_pad))'''
    o = bytes([x ^ 0x5c for x in bytes_key])#换这个居然变了
    i = bytes([x ^ 0x36 for x in bytes_key])

    h = sha1(i + mes)
    ans = sha1(o + h)

    return ans


def main():
    k = input().strip()
    mes = input().strip()
    #print(HMAC(k, mes).decode('utf-8'))
    #print(HMAC(k, mes).decode())
    print(HMAC(k, mes).hex())
if __name__ == '__main__':
    with PyCallGraph(output=GraphvizOutput()):
        main()