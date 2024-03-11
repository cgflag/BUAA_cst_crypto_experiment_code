'''def gcd(a, b):
    r = a
    r1 = b
    while r1 != 0:
        q = r // r1
        t = r - q * r1
        r = r1
        r1 = t
    return r


def Egcd(a, b):
    r, s, t = a, 1, 0
    r1, s1, t1 = b, 0, 1
    while r1 != 0:
        q = r//r1
        temp1, temp2, temp3 = r - q * r1, s - q * s1, t - q * t1
        r, s, t = r1, s1, t1
        r1, s1, t1 = temp1, temp2, temp3
    return r, s, t


def invmod(a, n):
    if gcd(a, n) == 1:
        _, result, _ = Egcd(a, n)
    return result % n


a_list = list(map(int, input().split(" ")))
b_list = list(map(int, input().split(" ")))
M_list = []
Minv_list = []
ans = 0
if gcd(b_list[0], b_list[1]) == 1 and gcd(b_list[1], b_list[2]) == 1 and gcd(b_list[2], b_list[0]) == 1:
    M = b_list[0]*b_list[1]*b_list[2]
    for i in range(0, 3):
        M_list.append(M//b_list[i])
    for i in range(0, 3):
        Minv_list.append(invmod(M_list[i], b_list[i]))
    for i in range(0, 3):
        ans += a_list[i]*M_list[i]*Minv_list[i]
    ans %= M
    print(ans)'''
# -*- coding: UTF-8 -*-
'''def Get_Mi(m_list, M):  # 获取所有的Mi
    M_list = []
    for mi in m_list:
        M_list.append(M // mi)
    return M_list


def Get_ei_list(M_list, m_list):  # 取所有的Mi的逆元
    ei_list = []
    for i in range(len(M_list)):
        ei_list.append(Get_ei(M_list[i], m_list[i])[0])
    return ei_list


def Get_ei(a, b):
    # 计算ei

    if 0 == b:
        x = 1;
        y = 0;
        q = a
        return x, y, q
    xyq = Get_ei(b, a % b)
    x = xyq[0];
    y = xyq[1];
    q = xyq[2]
    temp = x;
    x = y;
    y = temp - a // b * y
    return x, y, q


def crt(a_list, m_list):
    # 计算中国剩余定理，返回计算结果
    M = 1  # M是所有mi的乘积
    for mi in m_list:
        M *= mi
    Mi_list = Get_Mi(m_list, M)
    Mi_inverse = Get_ei_list(Mi_list, m_list)
    x = 0
    for i in range(len(a_list)):  # 开始计算x
        x += Mi_list[i] * Mi_inverse[i] * a_list[i]
        x %= M
    return x

if __name__ == '__main__':
    m_list = list(map(int, input().split(" ")))
    a_list = list(map(int, input().split(" ")))
    M = 1  # M是所有mi的乘积
    for mi in m_list:
        M *= mi
    if crt(a_list, m_list):
        print(crt(a_list, m_list))
    else:
        print(M)'''
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

def Get_Mi(m_list, M):  # 获取所有的Mi
    M_list = []
    for mi in m_list:
        M_list.append(M // mi)
    return M_list


def Get_ei_list(M_list, m_list):  # 取所有的Mi的逆元
    ei_list = []
    for i in range(len(M_list)):
        ei_list.append(Get_ei(M_list[i], m_list[i])[0])
    return ei_list


def Get_ei(a, b):
    # 计算ei

    if 0 == b:
        x = 1;
        y = 0;
        q = a
        return x, y, q
    xyq = Get_ei(b, a % b)
    x = xyq[0];
    y = xyq[1];
    q = xyq[2]
    temp = x;
    x = y;
    y = temp - a // b * y
    return x, y, q


def crt(a_list, m_list):
    # 计算中国剩余定理，返回计算结果
    M = 1  # M是所有mi的乘积
    for mi in m_list:
        M *= mi
    Mi_list = Get_Mi(m_list, M)
    Mi_inverse = Get_ei_list(Mi_list, m_list)
    x = 0
    for i in range(len(a_list)):  # 开始计算x
        x += Mi_list[i] * Mi_inverse[i] * a_list[i]
        x %= M
    return x


def main():
    m_list = list(map(int, input().split(" ")))
    a_list = list(map(int, input().split(" ")))
    M = 1  # M是所有mi的乘积
    for mi in m_list:
        M *= mi
    if crt(a_list, m_list):
        print(crt(a_list, m_list))
    else:
        print(M)

if __name__ == '__main__':
    with PyCallGraph(output=GraphvizOutput()):
        main()







