def a():
    n = input()
    print('Yes' if '9' in n else 'No')

def b():
    n = int(input())
    total = 0
    for _ in range(n):
        l, r = map(int, input().split())
        total += r - l + 1
    print(total)

def c():
    from collections import Counter
    n = int(input())
    a = [int(input()) for _ in range(n)]
    c = dict(Counter(a))
    total = 0
    for v in c.values():
        total += v % 2
    print(total)

def d():
    N, M, R = map(int, input().split())
    r = [int(i) for i in input().split()]
    route = {}
    for _ in range(M):
        a, b, c = map(int, input().split())
        tmp = route.get(a, list())
        route[a] = tmp.append((b, c))
        # route[b] = route.get(b, list()).append((a, c))
    print(route)

d()
