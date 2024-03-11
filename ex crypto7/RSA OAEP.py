import hashlib
import sys
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput


def to_bytes(n, length):
    b = bytearray()
    while n:
        b.append(n & 0xff)
        n >>= 8
    return bytes(bytearray(reversed(b)).rjust(length, b'\x00'))


def from_bytes(b):
    return int.from_bytes(b, byteorder='big')
    #return int.from_bytes(b, byteorder='little')


def sha1(m):#sha1 #L不是空时怎么处理？
    return hashlib.sha1(m).digest()


'''def mgf1(seed, mask_len):#有错
    t = b''
    #print(mask_len)
    for i in range((mask_len + 31) // 32):
        c = to_bytes(i, 4)
        t += sha1(seed + c)
    #if 32 * ((mask_len + 31) // 32)-32 < mask_len:
        #t += sha1(seed[32 * ((mask_len + 31) // 32):])#不对
    #c = 0c的长度？
    #if mask_len == len(seed):
        return seed

    #elif mask_len > len(seed):
    #    while (mask_len > len(t)):
    #        t = t + sha1(seed + c)
    #return t[:mask_len]
    return t[:mask_len]'''


def mgf1(seed, maskLen):
    #hLen = hashlib.sha256().digest_size
    hLen = hashlib.sha1().digest_size
    T = b''
    #for i in range(0, (maskLen+hLen-1)//hLen):#i应该遍历多大
    for i in range(0, ((maskLen + hLen - 1) // hLen)+2):
        #C = i.to_bytes(4, 'big')
        C = to_bytes(i, 4)
        #hash_obj = hashlib.new('sha256')
        #hash_obj.update(seed + C)
        T += sha1(seed+C)
    return T[:maskLen]


def oaep_encode(m, L, k, seed):#补0？
    #assert len(m) <= k - 2 * len(sha1(''.encode())), 'Message too long'
    #print(hex(from_bytes(m)))#对
    #print(L)
    #l_hash = sha1(L.encode())
    if L == '':
        l_hash = sha1(L.encode())
    else:
        l_hash = sha1(to_bytes(eval(L), (len(L)-2)//2))
        #l_hash = bytes(eval(L))
        #l_hash = sha1(L.encode())
        #l_hash = L.encode()
        #l_hash = sha1(bytes(eval(L[2:])))
        #l_hash = sha1(L[2:].encode())
        #l_hash = L[2:].encode()
        #l_hash = sha1(str(eval(L)).encode())
        #print(hex(from_bytes(l_hash)))#不对 已改正
    PS_len = k - len(m) - 2 * len(sha1(''.encode())) - 2
    PS = b'\x00' * PS_len if PS_len > 0 else b''
    db = l_hash + PS + b'\x01' + m
    #print(hex(from_bytes(db)))
    #seed = os.urandom(len(sha1(''.encode())))
    #db_mask = mgf1(seed, k - len(sha1(''.encode())) - 1)
    db_mask = mgf1(seed, len(db))
    #print(hex(from_bytes(db_mask)))#问题估计出在这个的长度
    masked_db = bytes(a ^ b for a, b in zip(db, db_mask))
    #print(hex(from_bytes(masked_db)))#masked_db短了
    seed_mask = mgf1(masked_db, len(sha1(''.encode())))
    masked_seed = bytes(a ^ b for a, b in zip(seed, seed_mask))
    #print(hex(from_bytes(masked_seed)))#masked_seed
    return b'\x00' + masked_seed + masked_db


def oaep_decode(EM, L='', k=128):
    #if len(EM) != k // 8 or EM[0] != 0:
    #print(hex(from_bytes(EM)))#
    #print(len(EM))
    #？要补吗
    while len(EM) < k:
        EM = b'\x00' + EM
    '''if len(EM) != k or EM[0] != 0:
        raise ValueError('Decryption error')'''
    #print(L)
    #l_hash = sha1(L.encode())
    if L == '':
        l_hash = sha1(L.encode())
    else:
        #l_hash = sha1(eval(L))
        #l_hash = sha1(L.encode())
        l_hash = sha1(to_bytes(eval(L), (len(L) - 2) // 2))
    #print(hex(from_bytes(l_hash)))
    masked_seed = EM[1: 1 + len(sha1(''.encode()))]
    masked_db = EM[1 + len(sha1(''.encode())):]
    #print(len(masked_db))#491
    #seed_mask = mgf1(masked_db, len(sha1(''.encode())))
    seed_mask = mgf1(masked_db, len(l_hash))
    #print(len(seed_mask))#20
    seed = bytes(a ^ b for a, b in zip(masked_seed, seed_mask))
    #db_mask = mgf1(seed, k - len(sha1(''.encode())) - 1)
    db_mask = mgf1(seed, k - len(l_hash) - 1)
    #print(k - len(l_hash) - 1)
    #print(len(db_mask))#360
    db = bytes(a ^ b for a, b in zip(masked_db, db_mask))
    l_hash_ = db[:len(sha1(''.encode()))]
    #print(hex(from_bytes(l_hash_)))#居然不一样？ 已纠正
    #PS = db[len(sha1(''.encode())):].split(b'\x00', 1)[0] or b''
    for i in range(len(sha1(''.encode())), len(db)):
        #if db[i] == b'\x01':
        if db[i] == 1:
            break
    one = db[i]
    i += 1
    #print(hex(from_bytes(PS)))
    #one = db[len(sha1(''.encode())) + len(PS)]
    #print(hex(one))
    #m = db[len(sha1(''.encode())) + len(PS) + 1:]#没截对
    #m = db[len(sha1(''.encode())) + len(PS) + 2:]
    #m = db[len(sha1(''.encode())) + len(PS) + 3:]
    m = db[i:]#后面不一样 短了好多
    #l_hash_, PS, one, m = db[:len(sha1(''.encode()))], db[len(sha1(''.encode())):].split(b'\x00', 1)[0] or b'', db[len(sha1(''.encode())) + len(PS)], db[len(sha1(''.encode())) + len(PS) + 1:]
    #PS怎么搞
    if l_hash_ != l_hash or one != 1:
        #raise ValueError('Decryption error')
        print("Ree")
        sys.exit(0)
    return m


def main():
    op = int(input())
    k = int(input())
    e = eval(input().strip())
    N = eval(input().strip())
    #m = from_bytes(bytes.fromhex(input()))
    #L = bytes.fromhex(input()).decode()
    #m = bytes.fromhex(input().strip()[2:])
    #m = eval(input().strip())
    m = input().strip()
    L = input().strip()
    if len(L)//2 > pow(2, 61)-1:
        print("Err")
        sys.exit(0)
    if op == 1:
        #if len(m) > k - 2 * len(sha1(''.encode())):
        if (len(m)-2) // 2 > k - 2 * len(sha1(''.encode()))-2:
            print("Err")

        #elif len(m) <= k - 2 * len(sha1(''.encode())):
        elif (len(m)-2) // 2 <= k - 2 * len(sha1(''.encode()))-2:
            m = eval(m)
            #print(hex(m))
            seed = bytes.fromhex(input().strip()[2:])
            if L == '0x':
                L = ''
            else:
                #L = L[2:]
                #L = str(eval(L))
                #L = L
                L = L
            #EM = oaep_encode(to_bytes(m, (k + 7) // 8), L, k, seed)#传进去错
            EM = oaep_encode(to_bytes(m, (m.bit_length() + 7) // 8), L, k, seed)

            m_ = pow(from_bytes(EM), e, N)
            #print(to_bytes(m_, (k + 7) // 8).hex().lower())
            ans = hex(m_)[2:]
            while len(ans) < 2 * k:
                ans = '0' + ans
            ans = '0x'+ans
            print(ans)

    elif op == 0:
        #何时解密错误？
        if k <= 42:
            print("Ree")
            sys.exit(0)
        if (len(m)-2)//2 != k:
            print("Ree")
        else:
            m = eval(m)
            m_ = pow(m, e, N)
            if L == '0x':
                L = ''
            else:
                #L = L[2:]
                #L = str(eval(L))
                #L = L
                L = L
            EM = to_bytes(m_, (k + 7) // 8)
            #print(hex(from_bytes(EM)))#可能0开头
            m__ = from_bytes(oaep_decode(EM, L=L, k=k))
            ans = hex(m__)[2:]
            '''while len(ans) < 2 * k - 2 * 20 - :
                ans = '0' + ans'''
            ans = '0x' + ans
            print(ans)


if __name__ == '__main__':
    with PyCallGraph(output=GraphvizOutput()):
        main()
#0x8f0561fde00be5389970dbdd86b4d26c818df74eca412b520209e79296e74d8ecd07081f7e1c68bf489ad39468712140a3a0a945f3d496288e81c0f7d53bb38c9250a939036f4dddb313ae904aab1aac57764dd9f8d6828345975ab4b003929cb05c2ecc920ee7302bf0f1c3b63cfc30396569df0c76c71d728f4756e88bb334480092ffbc96ed0ea5ba014fcd2a4cb4b56853843abe1e86ebd77623d62401d404d04caeb59c0fe9d184c7071fe377ad14b7dfc1f27ec657d5e449
#0x8f0561fde00be5389970dbdd86b4d26c818df74eca412b520209e79296e74d8ecd07081f7e1c68bf489ad39468712140a3a0a945f3d496288e81c0f7d53bb38c9250a939036f4dddb313ae904aab1aac57764dd9f8d6828345975ab4b003929cb05c2ecc920ee7302bf0f1c3b63cfc30396569df0c76c71d728f4756e88bb334480092ffbc96ed0ea5ba014fcd2a4cb4b56853843abe1e86ebd77623d62401d404d04caeb59c0fe9d184c7071fe377ad14b7dfc1f27ec657d5e449
#0x8f0561fde00be5389970dbdd86b4d26c818df74eca412b520209e79296e74d8ecd07081f7e1c68bf489ad39468712140a3a0a945f3d496288e81c0f7d53bb38c9250a939036f4dddb313ae904aab1aac57764dd9f8d6828345975ab4b003929cb05c2ecc920ee7302bf0f1c3b63cfc30396569df0c76c71d728f4756e88bb334480092ffbc96ed0ea5ba014fcd2a4cb4b56853843abe1e86ebd77623d62401d404d04caeb59c0fe9d184c7071fe377ad14b7dfc1f27ec657d5e449
#0x605318c4d0e28c33cd4e2bf4a24e75989e2047283bec52f369b560031f7f24e9437749a15742cbfafa3864803c2541df8dfafd7f018509c166c6b582522eb3c957b12f75d68a2084feefec3018b2a98a42cd7613569e5fe5cf4636f4fab344874f5bf068cf6b4b83a44dba7b516000a99d91b0450e696f2abef54b8d07fc3fb52f4c9e31a355144c55463f71344df832c258ba0398125065e5b012b748be9c2ab09754a2b6070689fc46c403ae1a2de28d67dfac4978af57273c0507a46dcb415fedd1072da2463b51b473d12a3f9ef44e1650f717964ac264afd743e7c58f4a1dc1cabbf79664efa6405b83e76fb41e569886125a9d5140d4cae59c8b1ef6a8
#0x208fcf802848897c60fbca2b8f991705879bcef6ac225175e18b4853b5c1c18d609bb6b30f72c7c0f557acc5187827fd4bdc12d7a8dc0b01a30cda68c4572e82d59c541c10316bfb5cf15d29699bbb6fd11529d0c10418471c2c982056797f6ae6616b2a23bc7ca1a705974f5b7253334db0c047a06c7bd4f65cac258ebb27b4549acf97b0b078034d9d3151e2a779b8cff651936a7a11f03b3f583a98fc66d0d1f3960dd1730adaa531fb48aab28370197bd40b4b87a83517464f112dd82d826f1f12f454a823a904e8cc63255cda322a49fc4b40d7b17b0e15eb1eeebe0bc2e6304792ab01c94efe1d4f82a8b360e1b1e74acb48542512e3839c3dd66a04f0


