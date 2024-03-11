from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

def attack(cipher,hasher):
    for i in range(0, len(cipher)):
        hasher[ord(cipher[i])-ord('a')] += 1

    #hasher1 = hasher
    hasher1 = []
    hasher1 += hasher
    hasher.sort(reverse = True)
    k = (hasher1.index(hasher[0])-4)%26
    return k

def main():
    cipher = input().strip()
    hasher = [0]*26
    print(attack(cipher, hasher))


if __name__ == '__main__':
    with PyCallGraph(output=GraphvizOutput()):
        main()
