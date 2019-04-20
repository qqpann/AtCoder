def a():
    a, b = map(int, input().split())
    print(a + b if a + b < 10 else 'error')


def b():
    s = input()
    l = list(s)
    print('yes' if len(set(l)) == len(l) else 'no')


def c():
    n = int(input())
    ss = []
    s_min = 101
    for _ in range(n):
        si = int(input())
        ss.append(si)
        if si % 10 != 0:
            s_min = min(s_min, si)

    m = sum(ss)
    if m % 10 == 0:
        if s_min > 100:
            print(0)
        else:
            print(m - s_min)
    else:
        print(m)


def d0():
    import numpy as np
    n, a, b = map(int, input().split())
    d = a - b
    hs = np.array([])
    for _ in range(n):
        hs = np.append(hs, int(input()))
    hs = np.sort(hs)
    # 1≤N≤10^5
    # 1≤B<A≤10^9
    # 1≤hi≤10^9
    result = 0
    # while bool(hs.any()) == True:
    # for _ in range(3):
    #     print(hs)
    #     # print(np.ceil(hs/b))
    #     # print(np.ceil(hs/a))
    #     # ceil_a = np.ceil(hs/a)
    #     print(np.floor(hs/b))
    #     # print(np.argmax(ceil_a))
    #     floor_b = np.floor(hs/b)
    #     # idx_argmax = np.argmax(ceil_a)
    #     idx_argmin = np.argmin(floor_b)
    #     # arg_max = ceil_a[idx_argmax]
    #     arg_min = floor_b[idx_argmin]
    #     # bs = b * arg_max
    #     bs = b * arg_min
    #     a_s = a * arg_min
    #     hs -= bs
    #     result += arg_min if arg_min > 0 else 0
    #     continue
    # print(int(result))

    # while np.amin(hs) > 0:
    #     hs[np.argmax(hs)] -= d
    #     hs -= b
    #     result += 1


    hdiff = hs - np.append(0, np.delete(hs, -1))
    print(hs, hdiff)

def d1():
    import numpy as np
    import math
    n, a, b = map(int, input().split())
    d = a - b
    hs = np.array([])
    for _ in range(n):
        hs = np.append(hs, int(input()))
    hs = np.sort(hs)

    result = 0
    # for i in range(len(hs)):
    #     # enough?
    #     k = math.ceil(hs[i] / b)
    #     hsi = hs - k*b
    #     if np.sum(hsi[i+1:]) - k*(a-b) < 0:
    #         result = k
    #         break
    start = int(hs[0]//a)
    for k in range(start, 10**9):
        print('k:', k)
        hsi = hs - k*b
        print('np.sum:', np.sum(hsi))
        if np.sum(hsi) - k*(a-b) < 0:
            result = k
            break

    print(result)


def d():
    n, a, b = map(int, input().split())
    l = [int(input()) for _ in range(n)]
    d = a - b

    left = 0
    right = 10**9

    def is_ok(t):
        return sum(map(lambda x: max(0, x - b*t + d-1) // d, l)) <= t

    while abs(left - right) > 1:
        now = (left + right) // 2
        if is_ok(now):
            right = now
        else:
            left = now

    print((right, left)[is_ok(left)])

d()
