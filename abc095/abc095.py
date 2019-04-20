def a():
    s = input()
    total = 700
    for i in s:
        total += 100 if i == 'o' else 0
    print(total)


def b():
    n, x = map(int, input().split())
    m = [int(input()) for _ in range(n)]
    print(len(m) + ((x - sum(m)) // min(m)))


def c():
    a, b, c, x, y = map(int, input().split())
    total = 0
    while x > 0 or y > 0:
        # compare a, b, c
        xi = min(x, 1)  # 0, 1
        yi = min(y, 1)  # 0, 1
        x -= xi
        y -= yi
        total += min(xi*a+yi*b, 2*c)
        # if xi*a+yi*b < 2*c:
        #     print(f'A pizza * {xi}, B pizza * {yi}')
        # else:
        #     print('AB pizza * 2')
    print(total)


def d():
    import numpy as np
    n, c = map(int, input().split())
    sushi = np.zeros((c, ), dtype=int)
    for _ in range(n):
        xi, vi = map(int, input().split())
        sushi[xi] = vi
    sushi = sushi - 1
    print(
        max(
            max(
                np.max(np.cumsum(sushi)),
                np.max(np.cumsum(np.flip(sushi, axis=0)))
            )+1,
            0
        )
    )


d()
