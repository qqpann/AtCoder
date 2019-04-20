def a():
    n = input()
    print('Yes' if n[0] == n[2] else 'No')


def b():
    a, b, c, d = map(int, input().split())
    begin = max(a, c)
    end = min(b, d)
    print(max(0, end-begin))


def c():
    n = int(input())
    t = {int(input()) for _ in range(n)}
    # lowest common minimum
    from fractions import gcd
    from functools import reduce
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    print( reduce(lcm, t) )


def d():
    from collections import deque

    N = int(input())
    edges = [[] for _ in range(N+1)]
    for _ in range(N-1):
        ai, bi, ci = map(int, input().split())
        edges[ai].append((bi, ci))
        edges[bi].append((ai, ci))
    Q, K = map(int, input().split())

    distance = [-1]*(N+1)
    # def add_weight(k, pre):
    #     for v in edges[k]:
    #         d, w = v
    #         if d != pre:
    #             distance[d] = w + distance[k]
    #             add_weight(d, k)
    # add_weight(K, -1)
    que = deque()
    que.append(K); distance[K] = 0
    while len(que):
        a = que.popleft()
        for b, c in edges[a]:
            if distance[b] == -1:
                distance[b] = c + distance[a]
                que.append(b)

    for _ in range(Q):
        s, e = map(int, input().split())
        print(distance[s] + distance[e])

d()
