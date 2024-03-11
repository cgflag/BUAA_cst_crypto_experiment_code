from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput


def _int32(x):
    return int(0xFFFFFFFF & x)


def twist(mt):#旋转
    #for i in range(0, 624):
    for i in range(0, 634):
        y = _int32((mt[i] & 0x80000000 ) + (mt[(i + 1) % 624] & 0x7fffffff))
        #mt[i] = (y >> 1) ^ mt[(i + 397) % 624]
        mt[i] = (y >> 1) ^ mt[(i + 397) % 634]

        if y % 2 != 0:
            mt[i] = mt[i] ^ 0x9908b0df


def main():
    seed = eval(input().strip())
    mt = [0] * 1268
    mt[0] = seed
    mti = 0
    #for i in range(1, 624):
    for i in range(1, 634):
        mt[i] = _int32(1812433253 * (mt[i - 1] ^ mt[i - 1] >> 30) + i)#初始化
    '''if mti == 0:
        twist(mt)
    
        y = mt[mti]
        y = y ^ y >> 11
        y = y ^ y << 7 & 2636928640
        y = y ^ y << 15 & 4022730752
        y = y ^ y >> 18
        mti = (mti + 1) % 624
    '''
    #while mti < 624:#一轮以上
    while mti < 634:
        if mti == 0:
            twist(mt)
        #if mti >= 624:
            #twist(mt)

        y = mt[mti]#处理
        y = y ^ y >> 11
        y = y ^ y << 7 & 2636928640
        y = y ^ y << 15 & 4022730752
        y = y ^ y >> 18
        mti = (mti + 1) % 635
        print(y)#只有第一个一样



if __name__ == '__main__':
    with PyCallGraph(output=GraphvizOutput()):
        main()
'''def mersenne_twister(seed, n):
    w, n, m, r = 32, n, 31, 0x9908B0DF
    a, u, d = 0x9D2C5680, 11, 0xFFFFFFFF
    s, b, t, c = 7, 0x9D2C5680, 15, 0xEFC60000
    l = 18
    f = 1812433253

    MT = [0] * n
    MT[0] = seed
    for i in range(1, n):
        MT[i] = (f * (MT[i-1] ^ (MT[i-1] >> (w-2))) + i) & d

    index = n
    while True:
        y = (MT[index-n] & 0x80000000) | (MT[(index-n)+1] & 0x7FFFFFFF)
        MT[index] = MT[(index-m)] ^ (y >> 1) ^ ((y & 1) * r)

        if index == n - 1:
            y = (MT[0] & 0x80000000) | (MT[1] & 0x7FFFFFFF)
            MT[n] = MT[m-1] ^ (y >> 1) ^ ((y & 1) * r)

        y = MT[index]
        y ^= (y >> u) & d
        y ^= (y << s) & b
        y ^= (y << t) & c
        y ^= y >> l

        index += 1
        yield y & d'''
#参数含义
#加法链 快速幂 进制表示
#大于一轮？
#生成列表 初始值？
