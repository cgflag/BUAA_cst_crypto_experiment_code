from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput


def odd_back(t):
    l = len(t)
    temp = ''
    ans = []
    for i in range(0, l):
        temp = ''
        #只想着改一个函数
        s = bin(t[i])[2:]
        #print(s)
        while len(s) < 56:
            s = '0'+s
        for j in range(0, len(s)//7):
            check = 0
            for k in range(7):
                temp += s[7*j+k]
                check ^= eval(s[7*j+k])
            temp += chr(check+ord('0'))
        #print(temp)
        #print(hex(eval('0b' + temp)))
        s = str(hex(eval('0b' + temp)))[2:]
        while len(s) < 16:
            s = '0' + s

        ans.append(s)
    return ans

def even_back(t):
    l = len(t)
    temp = ''
    ans = []
    for i in range(0, l):
        #!temp清空
        temp = ''
        s = ''
        s = bin(int(t[i]))[2:]
        while len(s) < 56:
            s = '0'+s
        for j in range(0, len(s) // 7):
            check = 0
            for k in range(7):
                temp += s[7 * j + k]
                check ^= eval(s[7 * j + k])
            check ^= 1
            temp += chr(check+ord('0'))
        s = str(hex(eval('0b'+temp)))[2:]
        while len(s) < 16:
            s = '0'+s
        ans.append(s)
    return ans


def substitute(list_):
    #key_subtitution1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
    #                    10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
    #                    63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
    #                    14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]
    key_subtitution1 = [50, 43, 36, 29, 22, 15, 8, 1, 51, 44, 37, 30, 23, 16,
                        9, 2, 52, 45, 38, 31, 24, 17, 10, 3, 53, 46, 39, 32,
                        56, 49, 42, 35, 28, 21, 14, 7, 55, 48, 41, 34, 27, 20,
                        13, 6, 54, 47, 40, 33, 26, 19, 12, 5, 25, 18, 11, 4]
    #先补全到64位
    mid = []
    '''for i in range(0, len(list_)):
        t_s = ''
        s_b = str(bin(list_[i]))[2:]
        while len(s_b) < 56:
            s_b = '0'+ s_b
        for j in range(56):
            t_s += s_b[j]
            if j%7 == 6:
                t_s += '0'
        mid.append(eval('0b'+t_s))'''
    ans = []
    t = [0]*64
    t_s = ''
    for i in range(0, len(list_)):
        t_s = ''
        #s_b = str(bin(mid[i]))[2:]
        s_b = str(bin(list_[i]))[2:]
        #while len(s_b) < 64:
        while len(s_b) < 56:
            s_b = '0' + s_b
        #for j in range(56):
            #t += str(s_b)[key_subtitution1[j]-1]应该逆过来
            #t[key_subtitution1[j]-1] = str(s_b)[j]
        for j in range(56):
            #t += str(s_b)[key_subtitution1[j]-1]应该逆过来
            t[key_subtitution1[j]-1] = str(s_b)[j]
            #t[j] = str(s_b)[key_substitution2[j] - 1]
        for j in range(56):
            t_s += str(t[j])
            #if j%7 == 6:
            #    t_s += '0'
        ans.append(eval('0b'+t_s))
    return ans


def main():
    t_weak = [0x00000000000000, 0x0000000FFFFFFF, 0xFFFFFFF0000000, 0xFFFFFFFFFFFFFF]
    key_weak = even_back(t_weak)+odd_back(t_weak)

    pre_semi_weak = [0xaaaaaaa, 0x00000005555555,
                     0xaaaaaaa0000000, 0x55555550000000,
                     0xaaaaaaaaaaaaaa, 0x55555555555555,
                     0xaaaaaaa5555555, 0x5555555aaaaaaa,
                     0xaaaaaaafffffff, 0x5555555fffffff,
                     0xfffffffaaaaaaa, 0xfffffff5555555]

    t_semi_weak = substitute(pre_semi_weak)
    #for n in t_semi_weak:
    #    print("{:16x}".format(n))
    #还要代换
    key_semiweak = even_back(t_semi_weak)+odd_back(t_semi_weak)
    print(key_weak)
    print(key_semiweak)


if __name__ == '__main__':
    with PyCallGraph(output=GraphvizOutput()):
        main()



