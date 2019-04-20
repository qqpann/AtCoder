def a():
    n = int(input())
    print('ABC'+str(n))


def b():
    n = int(input())
    two_l = [ 2**x for x in range(7) ]
    res = 1
    for i in two_l:
        if i <= n:
            res = i
        else:
            break
    print(res)


def c():
    n, m = map(int, input().split())
    ship_loot = []
    for _ in range(m):
        a, b = map(int, input().split())
        ship_loot.append( (a, b) )

    loot = { x:set() for x in range(1, n+1)}
    for l in ship_loot:
        a, b = l
        loot[a].add(b)
        loot[b].add(a)

    print('POSSIBLE' if loot[1] & loot[n] else 'IMPOSSIBLE')
    # print(ship_loot)
    # print(loot)
    # print(loot[1] & loot[n])


def d():
    k = int(input())
    a = [0]*n
    # 2≦N≦50, 0≦ai≦1016+1000
    print(n)
    print(' '.join(a))
