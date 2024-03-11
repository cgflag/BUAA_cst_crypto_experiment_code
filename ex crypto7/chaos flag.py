from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
from AITMCLAB.libnum import n2s


def len_in_bits(n):
    """
    Return number of bits in binary representation of @n.
    Probably deprecated by .bit_length().
    """
    if not isinstance(n, int):
        raise TypeError("len_in_bits defined only for ints")
    return n.bit_length()


'''def n2s(n):
    r"""
    Number to string (big endian).

    >>> n2s(0x4241)
    b'BA'
    >>> n2s(0x100)
    b'\x01\x00'
    """
    nbits = len_in_bits(n)
    nbytes = (nbits + 7) >> 3
    return n.to_bytes(nbytes, "big")'''


def Egcd(a, b):
    r, s, t = a, 1, 0
    r1, s1, t1 = b, 0, 1
    while r1 != 0:
        q = r//r1
        temp1, temp2, temp3 = r - q * r1, s - q * s1, t - q * t1
        r, s, t = r1, s1, t1
        r1, s1, t1 = temp1, temp2, temp3
    return r, s, t


def gcd(a, b):
    r = a
    r1 = b
    while r1 != 0:
        q = r//r1
        t = r - q*r1
        r = r1
        r1 = t
    return r


def invmod(a, n):
    if gcd(a, n) == 1:
        _, result, _ = Egcd(a, n)
    return result % n


def main():
    p = 8060224167508953559985795829105353706264995426539040211450848476875819847783411399182952191088483169979850012499608700022085398954278777225222262273498079
    q = 5776606591131731176687221654555806721589749446513729573168881347635227133113794767302741712092017955351737968930616386238529534813063208506333298381433797
    N = 46560744052031492000075598084262814175984839629218579003339825251165084535288738001196294968344403225296587992393409186512832442084313772062189640462381680977493272839744503195012137744652370256066011590369737294828406013950810998314546935103160880000499234316605414326064476117367727072344004644766745175963
    phi = (p-1) * (q-1)#为什么比较固定
    e = 65537
    d = invmod(e, phi)
    c = 23334367507777982721463578689282517343702422017568936413397591619899938216343800551132594869485665306596562901129144338015710969994575939792628945297846703002122172051500112438041566171992504143239954624689779597268840813422509867439815100802585538453946245512563984478922752113443379737653491922857109660034
    ans = pow(c, d, N)
    #print(ans)
    print(n2s(ans).decode())


if __name__ == '__main__':
    with PyCallGraph(output=GraphvizOutput()):
        main()