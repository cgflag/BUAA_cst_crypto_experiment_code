def encrypt(t1, t2, m):
    ans = ''
    for i in range(0, len(m)):
        ans += t2[t1.index(m[i])]
    return ans


f = open("original.txt", "r",encoding='UTF-8')
f1 = open("singlecipher.txt", "w")
f2 = open("madeup.txt", "w")
ori = f.read()
ori1 = ''
for i in range(0, len(ori)):
    #if ord('a') <= ord(ori[i]) and ord(ori[i]) <= ord('z') or ord('A') <= ord(ori[i]) and ord(ori[i]) <= ord('Z'):
    if ord('a') <= ord(ori[i]) and ord(ori[i]) <= ord('z') or ord('A') <= ord(ori[i]) and ord(ori[i]) <= ord('Z'):
        ori1 += ori[i].lower()

s1 = 'abcdefghijklmnopqrstuvwxyz'
k = 'qazwsxedcrfvtgbyhnujmiklop'
f1.write(encrypt(s1, k, ori1))
f2.write(ori1)

