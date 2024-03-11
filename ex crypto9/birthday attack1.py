'''n = int(input()) // 4  # 转换为字节长度
target_hash = bytes.fromhex(input())

while True:
    message = bytearray(random.getrandbits(8) for _ in range(64))
    hash1 = hashlib.sha1(message).digest()
    if hash1[:n] != target_hash[:n]:
        continue
    message[-4:] = bytearray(random.getrandbits(8) for _ in range(4))
    hash2 = hashlib.sha1(message).digest()
    if hash2[:n] == target_hash[:n]:
        break
    while True:
        message[-4:] = bytearray(random.getrandbits(8) for _ in range(4))
        hash2 = hashlib.sha1(message).digest()
        if hash2[:n] == target_hash[:n]:
            break

#print(message.hex())
print(message.decode())'''
#怎么生成 生成一个大集合 设初值 构造？ 2^80 调整初值
import hashlib
import struct
import random
import string
import unicodedata

#length = 10


# 获取十六进制数的二进制表示，并填充到指定长度
'''def hex_to_bin(s, length):
    return bin(int(str(s), 16))[2:].zfill(length)

# 获取二进制字符串的十六进制表示
def bin_to_hex(s):
    return hex(int(s, 2))[2:]

# SHA-1散列函数
def sha1(message):
    m = hashlib.sha1()
    m.update(message)
    return m.digest()

# 循环左移函数
def rol(n, r):
    return ((n << r) & 0xFFFFFFFF) | (n >> (32 - r))


def generate_random_unicode_string(length):
    # 生成可打印的unicode字符范围为U+0021到U+007E
    printable_range = range(0x0021, 0x007F)
    # 生成指定长度的unicode字符列表
    unicode_list = [chr(random.choice(printable_range)) for _ in range(length)]
    # 将unicode字符列表合并成一个字符串
    unicode_string = ''.join(unicode_list)
    # 将unicode字符串编码为utf-8字节串
    utf8_bytes = unicode_string.encode('utf-8')
    return utf8_bytes

# 对给定的哈希值s进行SHA-1的第一类生日攻击
def sha1_birthday_attack(n, s):
    # 将十六进制哈希值转换为二进制形式，并截取前n比特
    s_bin = hex_to_bin(s, 160)[:n]

    # 随机生成两个消息块，并计算它们的哈希值
    while True:
        # 随机生成两个消息块，并将它们拼接成一个长消息
        #m1 = bytearray(random.getrandbits(8) for _ in range(64))
        #m2 = bytearray(random.getrandbits(8) for _ in range(64))
        #message = m1 + m2
        #m1 =  ''.join(random.choice(string.printable) for _ in range(length)).encode('utf-8')
        #unicode_string = ''.join(chr(random.randint(0, 0x10FFFF)) for _ in range(10))
        #m1 = ''.join(chr(random.randint(0, 0x10FFFF)) for _ in range(10))
        #m1 = unicodedata.normalize('NFC', m1)
        #m1 = m1.encode()
        #m1 = unicodedata.normalize('NFC', unicode_string)
        m1 = generate_random_unicode_string(10)

        # 计算消息的哈希值，并截取前n比特
        h = sha1(m1)
        h_bin = hex_to_bin(h.hex(), 160)[:n]

        # 如果匹配成功，则输出构造的消息
        if h_bin == s_bin:
            #return bin_to_hex(m1.hex() + m2.hex())
            return m1.decode()

#n = int(input()) // 4  # 转换为字节长度
n = eval(input().strip())
#s = bytes.fromhex(input())
s = eval('0x' + input().strip())
#s = input().strip()
print(sha1_birthday_attack(n, s))'''
'''import hashlib
import random


def generate_random_string(n):
    # 生成一个长度为n的随机UTF-8字符串
    s = ''.join([chr(random.randint(0x4E00, 0x9FA5)) for i in range(n)])
    return s


def find_hash_collision(target_hash, n):
    while True:
        # 生成一个随机UTF-8字符串
        random_string = generate_random_string(n)

        # 计算哈希值并提取前n位
        h = hashlib.sha1(random_string.encode('utf-8')).hexdigest()
        check_code = int(h[:n // 4], 16)

        # 如果校验码匹配，则返回字符串和哈希值
        if check_code == int(target_hash[:n // 4], 16):
            return random_string, h


n = eval(input().strip())
target_hash = input().strip()
ans, _ = find_hash_collision(target_hash, n)
print(ans)'''
'''import random
import hashlib


targ = hashlib.sha1()
#input_size = 10
input_size = eval(input().strip()) // 4
number_of_trys = 40


def generateRandomString(d):
    charString = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join([random.choice(charString) for i in range(d)])


def getDbitHAsh(string, d):
    global targ
    targ.update(bytes(string, encoding='utf8'))
    hexHash=targ.hexdigest()
    return bin(int(hexHash, 16))[2:][:d]


def fun(d):
    global input_size
    totalBits = 0
    data = {}
    first = generateRandomString(input_size)
    hashCode = getDbitHAsh(first, d)
    data[hashCode] = first
    totalBits += d
    counter = 1
    while True:
        totalBits += d
        counter += 1
        first = generateRandomString(input_size)
        hashCode = getDbitHAsh(first, d)
        if hashCode in data.keys() and data[hashCode] != first:
            return data[hashCode], first, hashCode,totalBits, counter*(counter-1)
        data[hashCode] = first

print("Hash Bits, string1, string2, hashCode, Largest Memory in Bits, comparission")
for d in range(1, 25):
    print(d, "     ", fun(d))'''
#random.choice生成随记utf
'''import random
import unicodedata

length = 10
unicode_string = ''.join(chr(random.randint(0, 0x10FFFF)) for _ in range(length))
normalized_unicode_string = unicodedata.normalize('NFC', unicode_string)'''
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
import hashlib
import random


#不会有其他情况相等吗？ 生日攻击怎么使用
def sha1(m):#sha1 #L不是空时怎么处理？
    return hashlib.sha1(m).digest()


def bytes2int(b):
    return int.from_bytes(b, byteorder='big')


def main():
    n = eval(input().strip())
    #target_hash = input().strip()
    target_hash = eval('0x'+input().strip())
    while True:
        if n <= 16:
            rand = random.randint(10, pow(2, 20))
        #if bin(bytes2int(sha1(rand)))[2:n+2] == bin(target_hash)[2:n+2]:
        elif n <= 20:
            rand = random.randint(pow(2, 24), 0b10101111101100001110011111)#估计得hex
        else:
            rand = random.randint(0b11011100011101011011000000000, 0b100000010011001100010111111111)
        if bin(bytes2int(sha1(bytes(str(rand), 'utf-8'))))[2:n + 2] == bin(target_hash)[2:n + 2] and len(bin(bytes2int(sha1(bytes(str(rand), 'utf-8'))))) == len(bin(target_hash)):#粗心
        #if hex(bytes2int(sha1(bytes(str(rand), 'utf-8'))))[2:n // 4 + 2] == hex(target_hash)[2:n // 4 + 2] and len(hex(bytes2int(sha1(bytes(str(rand), 'utf-8'))))) == 42:
            #print(bin(bytes2int(sha1(bytes(str(rand), 'utf-8'))))[2:n + 2])
            #print(bin(target_hash)[2:n + 2])
        #if bin(bytes2int(sha1(str(rand).encode())))[2:n + 2] == bin(target_hash)[2:n + 2]:
            print(rand)
            break
#范围内根本没有？


if __name__ == '__main__':
    with PyCallGraph(output=GraphvizOutput()):
        main()