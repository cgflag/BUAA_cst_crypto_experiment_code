'''n = eval(input())
pr = [0,1]
temp_l1 = [0]*1000000
pr = pr + temp_l1
for i in range(1, n+1):
    if pr[i] == 1:
        continue
    else:
        for j in range(2*i, n+1, i):
            pr[j] = 1
for i in range(1, n+1):
    if pr[i] == 0 and i != n:
        print(i, end = ' ')
    elif pr[i] == 0 and i == n:
       print(i, end = '')'''
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

def calculate_primes(n):
    pr = [0,1]
    temp_l1 = [0]*1000000
    pr = pr + temp_l1
    for i in range(1, n+1):
        if pr[i] == 1:
            continue
        else:
            for j in range(2*i, n+1, i):
                pr[j] = 1
    for i in range(1, n+1):
        if pr[i] == 0 and i != n:
            print(i, end=' ')
        elif pr[i] == 0 and i == n:
            print(i, end='')


def main():
    n = eval(input())
    calculate_primes(n)


if __name__ == '__main__':
    with PyCallGraph(output=GraphvizOutput()):
        main()