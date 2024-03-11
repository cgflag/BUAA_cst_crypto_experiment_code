'''import hashlib
import random
import time


def BirthdayAttack(n):
    while 1:
        x = random.random()
        y = random.random()
        h1 = hashlib.sha1(str(x).encode())
        h2 = hashlib.sha1(str(y).encode())
        if h1[:n] == h2[:n]:
            break
    return (h1[:n], h2[:n])


while 1:
    n = int(input("规模（单位：Byte）："))
    #start = time.time()
    for i in range(10):
        BirthdayAttack(n)
    #end = time.time()
    #runtime = (end - start) / 10
    #print("用时：", runtime, "s")
    if n == 0:
        break'''
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
import hashlib
import re
import random


def bytes2int(b):
    return int.from_bytes(b, byteorder='big')


def sha1(m):#sha1 #L不是空时怎么处理？
    return hashlib.sha1(m).digest()


'''def extract_numbers(text):
    # 使用正则表达式查找所有数字
    numbers = re.findall(r'\d+', text)
    return numbers


def find_matching_sentence(sentence):
    # 提取数字并用占位符替换它们
    n = 32
    numbers = extract_numbers(sentence)
    placeholder_sentence = re.sub(r'\d+', '%d', sentence)

    # 计算原句子的哈希值并提取前 32 位
    original_hash = sha1(sentence.encode())
    original_hash_32bit = bytes2int(original_hash) & 0xffffffff
    print(hex(bytes2int(sha1(original_hash))))

    # 循环更改数字并计算新句子的哈希值，直到找到匹配的句子
    #for i in range(1, 10):
    while True:
        #new_numbers = [eval(number) + i for number in numbers]
        new_numbers = [eval(number) + random.randint(pow(2, 37), pow(2, 40)) for number in numbers]
        new_sentence = placeholder_sentence % tuple(new_numbers)
        new_hash = sha1(new_sentence.encode())
        #new_hash_32bit = bytes2int(new_hash) & 0xffffffff
        if bin(bytes2int(sha1(original_hash)))[2:n + 2] == bin(bytes2int(new_hash))[2:n + 2] and len(bin(bytes2int(sha1(original_hash)))) == len(bin(bytes2int(new_hash))):
            return new_sentence

    #return ''


sentence = 'please vme 50 dollars to enjoy KFC on this crazy Thursday'
print(find_matching_sentence(sentence))#一对句子找 存字典'''
def main():
    hash_dict = {}
    hash_set = set()
    sentence = input("请输入含有阿拉伯数字的句子：")#句子数字不能连在一起
    num_list = [int(s) for s in sentence.split() if s.isdigit()]
    if not num_list:
        print("句子中没有阿拉伯数字，请重新输入！")
    else:
        while True:
            new_sentence = sentence
            for i in range(len(num_list)):
                new_sentence = new_sentence.replace(str(num_list[i]), str(random.randint(3550000, 10000000)))

            sha1_hash = hashlib.sha1(new_sentence.encode()).hexdigest()[:8]
            if sha1_hash in hash_set and hash_dict[sha1_hash] != new_sentence:
                print(f"找到了两个不同句子的sha1哈希值的前32bit：{hash_dict[sha1_hash]} 和 {new_sentence}")
                print(hex(bytes2int(sha1(hash_dict[sha1_hash].encode())))[2:])
                print(hex(bytes2int(sha1(new_sentence.encode())))[2:])
                break
            else:
                hash_dict[sha1_hash] = new_sentence
                hash_set.add(sha1_hash)


if __name__ == '__main__':
    with PyCallGraph(output=GraphvizOutput()):
        main()