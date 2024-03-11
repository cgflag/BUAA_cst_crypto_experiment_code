def gcd(a, b):
    r = a
    r1 = b
    while r1 != 0:
        q = r // r1
        temp1, temp2, temp3 = r - q * r1, s - q * s1, t - q * t1
        r, s, t = r1, s1, t1
        r1, s1, t1 = temp1, temp2, temp3
    if b < 0:
        r = -r
    return r


def Exgcd(a, b):
    r, s, t = a, 1, 0
    r1, s1, t1 = b, 0, 1
    while r1 != 0:
        q = r//r1
        temp1, temp2, temp3 = r - q * r1, s - q * s1, t - q * t1
        r, s, t = r1, s1, t1
        r1, s1, t1 = temp1, temp2, temp3
    if b < 0 :
        r, s, t = -r, -s, -t
    return r, s, t



s = input()
s1, s2 = s.split(' ')
a = eval(s1)
b = eval(s2)
g, x, y = Exgcd(a, b)
if g == 1:
    while x <= 0:
        if b > 0:
            x += b
            y -= a
        elif b < 0:
            x += -b
            y -= -a
    print(x, y, g, end=' ')
else:
    a1 = a//g
    b1 = b//g
    g1, x1, y1 = Exgcd(a1, b1)
    while x1 <= 0:
        if b1 > 0:
            x1 += b1
            y1 -= a1
        elif b1 < 0:
            x1 += -b1
            y1 -= -a1
    print(x1, y1, g, end=' ')
'''if a != 0:
    if abs(b) % abs(a) != 0 and b != 0 and abs(a) % abs(b) != 0:
        while x <= 0:
            if b > 0:
                x += b
                y -= a
            elif b < 0:
                x += -b
                y -= -a
    elif b == 0:
        x = 1
        y = 0
    elif abs(a) == abs(b):
        x = 1
        g = abs(a)
        y = (g-a)//b
    elif abs(b) % abs(a) == 0 and b < 0:
        if a < 0:
            y = -1
            x = (b+g)//a
    elif abs(b) % abs(a) == 0 and b > 0:
        if a < 0:
            y = 1
            x = (g-b)//a
    else:
        x = 1
        y = (g - a) // b
else:
    if abs(a) != abs(b):
        x = 1
        y = g // b
print(x, y, g, end=' ')'''
