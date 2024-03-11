'''import string

f = open("singlecipher.txt", "r")
# 加载英文字母频率表
letter_frequency = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99,
                    'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97,
                    'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}

# 加载密文
#ciphertext = input("请输入密文: ").upper()
ciphertext = str(f.readlines()).upper()

# 计算每个字母在密文中出现的次数
#letter_count = {}字典
list_f = list(letter_frequency.keys())
letter_count = {}
for letter in string.ascii_uppercase:
    letter_count[letter] = ciphertext.count(letter)

# 根据字母出现次数排序
letter_count_sorted = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)

# 尝试前10个可能的代换
for i in range(10):
    #mapping = {}
    mapping = [0]*26
    for j in range(len(letter_count_sorted)):
        #mapping[letter_count_sorted[j][0]] = letter_frequency_sorted[j][0]
        #mapping[letter_count_sorted[j][0]] = letter_frequency[j][0]
        #mapping[letter_count_sorted[j][0]] = list_f[j]
        mapping[ord(letter_count_sorted[j][0])-ord('A')] = list_f[j]
    key = ''
    for i in range(0, 26):
        key += mapping[i].lower()


    # 打印可能性排名、密钥、以及解密后的明文
    print("Possible ranking: " + str(i + 1))
    #print("Key: " + str(mapping))
    print(key)
    #print("Plaintext: " + plaintext)
    print()

    # 将字母频率表进行轮换，以尝试下一个可能的代换
    #letter_frequency_sorted = [letter_frequency_sorted[-1]] + letter_frequency_sorted[:-1]
    #letter_frequency = [letter_frequency[-1]] + letter_frequency[:-1]
    list_f = [list_f[-1]] + list_f[:-1]'''

# -*- coding: utf-8 -*-


''' = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
     'X', 'Y', 'Z']
result = []
b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
f1 = open("singlecipher.txt", "r")

message = f1.read()  # 读取文章

sum = 0  # 总数

for i in message:
    if ('A' <= i <= 'Z'):  # 只记录字母
        sum = sum + 1  # 记录字母总数
        for j in range(0, 26):
            if (s[j] == i):
                b[j] = b[j] + 1
print(sum)  # 字母总数
print(b)  # 各个字母总数

for i in range(0, 26):
    result.append((b[i] / sum))
    print(s[i], ":", (b[i] / sum) * 100)
# 打印频率'''
'''import string
import itertools

# 定义字母表和一些常用单词
alphabet = string.ascii_lowercase
common_words = ['the', 'and', 'you', 'that', 'was', 'for', 'are', 'with']

# 统计密文中每个字母出现的频率
def count_frequencies(ciphertext):
    frequencies = dict.fromkeys(alphabet, 0)
    for c in ciphertext:
        if c.lower() in alphabet:
            frequencies[c.lower()] += 1
    return frequencies

# 根据字母频率和常用单词猜测密钥
def guess_key(ciphertext):
    frequencies = count_frequencies(ciphertext)
    # 按照字母出现频率从高到低排序
    sorted_frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
    # 生成所有可能的字母置换
    permutations = itertools.permutations(alphabet)
    # 保存每个置换的还原度
    restoration_rates = {}
    for perm in permutations:
        # 将密文中的每个字母按照置换进行还原
        plaintext = ciphertext.translate(str.maketrans(''.join(perm), alphabet))
        # 计算明文中出现的常用单词数量
        count = 0
        for word in common_words:
            if word in plaintext:
                count += 1
        # 保存还原度
        restoration_rates[''.join(perm)] = count / len(common_words)
    # 按照还原度从高到低排序
    sorted_restoration_rates = sorted(restoration_rates.items(), key=lambda x: x[1], reverse=True)
    # 返回前10个可能的密钥和还原度
    return sorted_restoration_rates[:10]

f = open("singlecipher.txt", "r")
cipher = f.readline()
list = []
list = guess_key(cipher)
for i in range(0, 10):
    print(list[i])'''
import string
from collections import Counter
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
import difflib
import random
#比较字符串相似程度


def appearcount(sub, s):
    ans = 0
    for i in range(0, len(sub)):
        if sub[i] in s:
            ans += 1
    return ans


def main():
    # 加载常用词
    with open("common_words.txt", "r") as f:
        common_words = set(f.read().splitlines())

    # 密文和字母频率
    #ciphertext = "VGhpcyBpcyBhIHRlc3Q="
    f1 = open("singlecipher.txt", "r")
    f2 = open("madeup.txt", "r")
    ciphertext = f1.readline()
    mas = f2.readline()
    freqs = Counter(ciphertext)

    print(freqs)
    # 根据字母频率对字母表排序
    alphabet = string.ascii_lowercase
    alphabet1 = alphabet
    sorted_alphabet = [a for a, _ in freqs.most_common()]
    std_suphigh = ['e']
    std_high = ['t', 'a', 'o', 'i', 'n', 's', 'r']
    std_hmid = ['h', 'l', 'd', 'c']
    std_mmid = ['u', 'm', 'f', 'p']
    std_dmid = ['g','w', 'y', 'b', 'v']
    std_low = ['k', 'x', 'j', 'q', 'z']
    # 枚举所有可能的密钥
    suphigh = sorted_alphabet[0:1]
    high = sorted_alphabet[1:8]
    umid = sorted_alphabet[8:12]
    mmid = sorted_alphabet[12:16]
    dmid = sorted_alphabet[16:21]
    low = sorted_alphabet[21:]
    nature = ['e', 't', 'a', 'o', 'i', 'n', 's', 'r', 'h', 'l', 'd', 'c', 'u', 'm', 'f', 'p', 'g','w', 'y', 'b', 'v', 'k', 'x', 'j', 'q', 'z']
    possible_keys = []
    '''for i in range(len(alphabet)):
        key = dict(zip(sorted_alphabet, alphabet[i:] + alphabet[:i]))
        possible_keys.append(key)'''
    #print(list(alphabet))
    for ihigh in range(0, len(high)):
        high = list(high)
        random.shuffle(high)
        for ihmid in range(0, len(umid)):
            umid = list(umid)
            random.shuffle(umid)
            for immid in range(0, len(mmid)):
                mmid = list(mmid)
                random.shuffle(mmid)
                for idmid in range(0, len(dmid)):
                    dmid = list(dmid)
                    random.shuffle(dmid)
                    for ilow in range(0, len(low)):
                        #key = dict(zip(sorted_alphabet, std_suphigh[0:]+std_high[ihigh:]+std_high[:ihigh]+std_mid[imid:]+std_mid[:imid]+std_low[ilow:]+std_low[:ilow]))

                        low = list(low)
                        random.shuffle(low)
                        #key = dict(zip(suphigh+high+umid+mmid+dmid+low, sorted_alphabet))
                        #key = dict(zip(suphigh + high + umid + mmid + dmid + low, nature))
                        key = dict(zip(nature, suphigh + high + umid + mmid + dmid + low))
                        if ihigh+ihmid+immid+idmid+ilow == 0:
                            print(key)
                            print(suphigh + high + umid + mmid + dmid + low)
                        possible_keys.append(key)
    #for i in range(0, len(possible_keys)):
    #    print(possible_keys[i])
    # 对每个密钥进行解密，并计算还原度
    print(possible_keys[0])
    probabilities = []
    for key in possible_keys:
        plaintext = "".join([key.get(c, c) for c in ciphertext])
        words = plaintext.split()
        #common_word_count = len(common_words.intersection(words))
        common_word_count = appearcount(list(common_words), words[0])
        #换成这个跑不出来了 跑太就不能调试
        #common_word_count = difflib.SequenceMatcher(None, mas, words[0]).quick_ratio()
        #probability = common_word_count / len(words[0])
        probability = common_word_count
        probabilities.append((key, probability))

    # 按还原度排序并输出前10个
    probabilities = sorted(probabilities, key=lambda x: x[1], reverse=True)
    for i in range(min(10, len(probabilities))):
        key, probability = probabilities[i]
        print(f"Rank {i+1}: Probability {probability:.3f}")
        ans = ''

        for a in alphabet:
            #print(f"{a} -> {key.get(a, a)}")
            ans += key.get(a, a)
        print(ans)
        print()
        #听说是频率相近的字母放在同一集合里代替


if __name__ == '__main__':
    with PyCallGraph(output=GraphvizOutput()):
        main()
#怎么遍历密钥