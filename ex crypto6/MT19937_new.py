'''# coefficients for MT19937
#(w, n, m, r) = (32, 624, 397, 31)
(w, n, m, r) = (32, 634, 397, 31)
a = 0x9908B0DF
(u, d) = (11, 0xFFFFFFFF)
(s, b) = (7, 0x9D2C5680)
(t, c) = (15, 0xEFC60000)
l = 18
f = 1812433253


# make a arry to store the state of the generator
MT = [0 for i in range(n)]
index = n+1
lower_mask = 0x7FFFFFFF #(1 << r) - 1 // That is, the binary number of r 1's
upper_mask = 0x80000000 #lowest w bits of (not lower_mask)


# initialize the generator from a seed
def MT_seed(seed):
    # global index
    # index = n
    MT[0] = seed
    for i in range(1, n):
        temp = f * (MT[i-1] ^ (MT[i-1] >> (w-2))) + i
        MT[i] = temp & 0xffffffff


# Extract a tempered value based on MT[index]
# calling twist() every n numbers
def extract_number():
    global index
    if index >= n:
        twist()
        index = 0

    y = MT[index]
    y = y ^ ((y >> u) & d)
    y = y ^ ((y << s) & b)
    y = y ^ ((y << t) & c)
    y = y ^ (y >> l)

    index += 1
    return y & 0xffffffff


# Generate the next n values from the series x_i
def twist():
    for i in range(0, n):
        x = (MT[i] & upper_mask) + (MT[(i+1) % n] & lower_mask)
        xA = x >> 1
        if (x % 2) != 0:
            xA = xA ^ a
        MT[i] = MT[(i + m) % n] ^ xA


seed = eval(input().strip())
MT_seed(seed)
for index in range(0, 20):
    print(extract_number())'''
MT = [0] * 640
index = 634
(u, d) = (11, 0xFFFFFFFF)
(s, b) = (7, 0x9D2C5680)
(t, c) = (15, 0xEFC60000)


def _int32(x):
    return int(0xFFFFFFFF & x)


def seedInit(seed):
    index = 634
    MT[0] = seed
    for i in range(1, 634):
        MT[i] = _int32(1812433253 * (MT[i - 1] ^ MT[i - 1] >> 30) + i)#初始化


def twist(index):
    for i in range(0, 634):
        y = _int32((MT[i] & 0x80000000) + (MT[(i + 1) % 624] & 0x7fffffff))
        yA = y >> 1
        if y % 2 == 1:
            yA ^= 0x9908b0df
        MT[i] = yA ^ MT[(i + 397) % 634]
    index = 0


def extract(index):
    if index >= 634:
        if index > 634:
            print(end='')
        twist(index)

    x = MT[index]
    y = x ^ ((x >> u) & d)
    y = y ^ ((y << s) & b)
    y = y ^ ((y << t) & c)
    z = y ^ (y >> 1)
    index += 1
    print(z & 0xffffffff)
    

seed = eval(input().strip())
seedInit(seed)
for index in range(0, 20):
    twist(index)
    extract(index)