#def mersenne_twister(seed, n):
seed = eval(input().strip())
n = 634
w, n, m, r = 32, n, 31, 0x9908B0DF
a, u, d = 0x9D2C5680, 11, 0xFFFFFFFF
s, b, t, c = 7, 0x9D2C5680, 15, 0xEFC60000
l = 18
f = 1812433253

MT = [0] * n
MT[0] = seed
for i in range(1, n):
    MT[i] = (f * (MT[i-1] ^ (MT[i-1] >> (w-2))) + i) & d#初始化

index = n
#while True:
for i in range(n):
    y = (MT[i] & 0x80000000) | (MT[(i+1) % 624] & 0x7FFFFFFF)
    MT[i] = MT[(i + 397) % 624] ^ (y >> 1) ^ ((y & 1) * r)

    '''if index == n - 1:
        y = (MT[0] & 0x80000000) | (MT[1] & 0x7FFFFFFF)
        MT[n] = MT[m-1] ^ (y >> 1) ^ ((y & 1) * r)'''

    y = MT[i]
    y ^= (y >> u) & d
    y ^= (y << s) & b
    y ^= (y << t) & c
    y ^= y >> l

    index += 1
    #yield y & d
    print(y)

