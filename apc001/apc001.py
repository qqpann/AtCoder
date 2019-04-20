def a():
    x, y = map(int, input().split())


def b():
    import numpy as np
    n = int(input())
    a = np.asarray(list(map(int, input().split())))
    b = np.asarray(list(map(int, input().split())))
    x = b.sum() - a.sum()
    d = b - a
    a_req = 0
    b_req = 0
    for i in d:
        if i <= 0:
            b_req += i // -1
        else:
            a_req += i // 2 + i % 2
            b_req += i % 2
    # total require
    if (a_req >= b_req and (0 < a_req + (a_req - b_req) == x)) or (a_req == 0 and b_req == 0):
        print('Yes')
    else:
        print('No')


def d():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    G = []
    for _ in range(m):
        s = set(map(int, input().split()))
        for S in G:
            if s & S:
                s |= S
        G = [i for i in G if not s >= i]
        G.append(s)
    G = [sorted([a[i] for i in S], reverse=True) for S in G]
    # 見なしのv, e
    _v = len(G)
    _e = _v - 1
    e = _e * 2
    cost = 0
    tmp = []
    for D in G:
        cost += D.pop()
        tmp += D
    tbd = e - _v
    cost += sum(sorted(tmp[:tbd]))
    print(cost)


if __name__ == '__main__':
    d()
