from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput


def main():
    b_len = eval(input().strip())
    p = eval(input().strip())
    q = eval(input().strip())
    s = eval(input().strip())
    ans = ''

    n = p * q
    x = (pow(s, 2, n))
    for i in range(b_len):
        x = pow(x, 2, n)
        ans += str(x%2)
    #注意倒序
    print(eval('0b'+ans[::-1]))


if __name__ == '__main__':
    with PyCallGraph(output=GraphvizOutput()):
        main()