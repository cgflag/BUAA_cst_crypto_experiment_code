'''import collections

def count_frequency(text):
    # 统计字符串中每个字符出现的次数，并返回一个字典
    freq = collections.defaultdict(int)
    for c in text:
        freq[c] += 1
    return freq

std_freq_table = {
    'a': 0.0817,
    'b': 0.0150,
    'c': 0.0278,
    'd': 0.0425,
    'e': 0.1270,
    'f': 0.0223,
    'g': 0.0202,
    'h': 0.0609,
    'i': 0.0697,
    'j': 0.0015,
    'k': 0.0077,
    'l': 0.0403,
    'm': 0.0241,
    'n': 0.0675,
    'o': 0.0751,
    'p': 0.0193,
    'q': 0.0010,
    'r': 0.0599,
    's': 0.0633,
    't': 0.0906,
    'u': 0.0276,
    'v': 0.0098,
    'w': 0.0236,
    'x': 0.0015,
    'y': 0.0197,
    'z': 0.0007,
}


def substitute(text, key):
    # 对输入文本进行单表代替，返回代替后的文本
    res = []
    for c in text:
        if c in key:
            res.append(key[c])
        else:
            res.append(c)
    return ''.join(res)

def score(text):
    # 计算输入文本的还原度，返回一个得分
    freq = count_frequency(text)
    score = 0
    for c in freq:
        if c in std_freq_table:
            score += std_freq_table[c] * freq[c]
    return score

def find_best_key(ciphertext):
    # 对输入密文进行频率分析，返回可能的前10个密钥
    freq = count_frequency(ciphertext)
    key_list = list(freq.keys())
    key_score = []
    for i in range(26):
        key = {}
        for j in range(26):
            key[key_list[j]] = key_list[(j+i)%26]
        plain = substitute(ciphertext, key)
        key_score.append((key, score(plain)))
    key_score.sort(key=lambda x: x[1], reverse=True)
    return key_score[:10]


f = open("singlecipher.txt", "r")
cipher = f.readline()
list_ = []
list_ = find_best_key(cipher)
#print(list_)
for i in range(0, len(list_)):
    ans = [0]*26
    anss = ''
    for k, v in list_[i][0].items():
        ans[ord(k)-ord('a')] = v
    for i in range(0, 26):
        anss += ans[i]
    print(anss)'''
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
import string
from collections import Counter

# 加载常用词
with open("common_words.txt", "r") as f:
    common_words = set(f.read().splitlines())

# 密文和字母频率
ciphertext = "VGhpcyBpcyBhIHRlc3Q="
freqs = Counter(ciphertext)

# 根据字母频率对字母表排序
alphabet = string.ascii_uppercase
sorted_alphabet = [a for a, _ in freqs.most_common()]

# 枚举所有可能的密钥
possible_keys = []
for i in range(len(alphabet)):
    key = dict(zip(sorted_alphabet, alphabet[i:] + alphabet[:i]))
    possible_keys.append(key)

# 对每个密钥进行解密，并计算还原度
probabilities = []
for key in possible_keys:
    plaintext = "".join([key.get(c, c) for c in ciphertext])
    words = plaintext.split()
    common_word_count = len(common_words.intersection(words))
    probability = common_word_count / len(words)
    probabilities.append((key, probability))

# 按还原度排序并输出前10个
probabilities = sorted(probabilities, key=lambda x: x[1], reverse=True)
for i in range(min(10, len(probabilities))):
    key, probability = probabilities[i]
    print(f"Rank {i+1}: Probability {probability:.3f}")
    for a in alphabet:
        print(f"{a} -> {key.get(a, a)}")
    print()