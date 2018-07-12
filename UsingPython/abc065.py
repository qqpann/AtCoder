def a():
    X, A, B = map(int, input().split())
    print(
        'delicious' if B-A <= 0 else
        'safe' if 0 < B-A <= X else
        'dangerous'
    )


def b():
    N = int(input())
    A = {i:int(input()) for i in range(1,N+1)}
    tmp = 1; times = 0
    for _ in range(N):
        tmp = A[tmp]; times += 1
        if tmp == 2:
            print(times)
            break
        elif tmp == 1:
            print(-1)
            break
    else:
        print(-1)


import math
def c():
    N, M = map(int, input().split())
    f = math.factorial
    if abs(N-M) > 1:
        print(0)
    elif N > M or M > N:
        print( f(N)*f(M) % (10**9 + 7) )
    elif N == M:
        print( (f(N)*f(M))*2 % (10**9 + 7))


import numpy as np
def d():
    N = int(input())
    # cities
    # cities = np.zeros((10, 10))
    # for _ in range(N):
    #     x, y = map(int, input().split())
    #     cities[x, y] += 1
    # print(N, cities)
    C = [list(map(int,input().split())) for _ in range(N)]
    Cx = list(map(lambda l: l[0], C))
    Cy = list(map(lambda l: l[1], C))
    nC = np.array(C)
    nCx = np.array(Cx)
    nCy = np.array(Cy)
    print(nC, nCx, nCy)
    print(np.argsort(nCx), np.argsort(nCy))
    nCx[0]

d()
