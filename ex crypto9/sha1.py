'''a, b, c, d, e = 0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0


def sha1_padding(message):
    binary_message = ''.join(format(ord(c), '08b') for c in message)
    binary_message += '1'
    message_length = len(binary_message)
    zeros_needed = (448 - message_length) % 512

    # Append the necessary number of '0' bits
    binary_message += '0' * zeros_needed
    binary_message += format(message_length - 1, '064b')
    return binary_message


def sha1(m):
    m = sha1_padding(m)


mes = input().strip()
print()
'''
import struct
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

# 常量定义
BLOCK_SIZE = 64  # 512位
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
    while (len(data) + 8) % BLOCK_SIZE != 0:
        data += b'\x00'
    data += struct.pack('>Q', bit_length)
    return data


def sha1(data):
    data = pad_data(data)# 数据填充

    h = list(INITIAL_H)

    for i in range(0, len(data), BLOCK_SIZE):
        block = data[i:i+BLOCK_SIZE]
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
    return ''.join([hex(i)[2:].zfill(8) for i in h])


def main():
    mes = input().strip()
    t = sha1(mes.encode('utf-8'))
    print(t)
#ans = hex(bytes2int(sha1(mes.encode('utf-8'))))[2:]
#print(ans)


if __name__ == '__main__':
    with PyCallGraph(output=GraphvizOutput()):
        main()