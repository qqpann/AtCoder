# A
def a():
    s = input().split()
    if s[0][-1] == s[1][0] and s[1][-1] == s[2][0]:
        print('YES')
    else:
        print('NO')

a()


# B
def b():
    a, b, c = map(int, input().split())
    for i in range(2, b):
        if a*i % b == c:
            print('YES')
            break
    else: print('NO')

b()


# C
def c():
    n, t = map(int, input().split())
    ti = list(map(int, input().split()))
    ttl = t
    for i in range(n-1):
        ttl += min(ti[i+1]-ti[i], t)
    print(ttl)

c()


# D
def d():
    n, w = map(int, input().split())
    shop = []
    for i in range(n):
        shop.append( list(map(int, input().split())) )
    # s = sorted(shop, key= lambda item: item[1]/item[0], reverse=True)
    # print(n, w, s)
    best = 0
    k = n-2
    while k <= n:
        bag = [0, 0]
        i = 0
        while i < k:
            item = s[i]
            i += 1
            if bag[0]+item[0] <= w:
                bag[0] += item[0]
                bag[1] += item[1]
            else:
                continue
        best = max(best, bag[1])
        k += 1
    print(best)

d()
