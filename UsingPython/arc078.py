def c():
    import numpy as np

    N = int(input() )
    A = np.array([int(a) for a in input().split()])

    A_cum = np.cumsum(A)
    A_rev = A_cum[-1] - A_cum
    res = np.abs(A_rev - A_cum)[:-1]
    print(int(np.min(res)))


def d():
    N = int(input())
    nodes = []
    for _ in range(N-1):
        a, b = map(int,input().split())
        nodes.append((a, b))


def e():
    n = list(range(10))
    left = 0
    right = 9
    tmp = left + right // 2
    
