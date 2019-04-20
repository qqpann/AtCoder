
def a():
    r, g, b = map(int, input().split())
    n = 100*r + 10*g + 1*b
    print('YES' if n % 4 == 0 else 'NO')

def b():
    n = int(input())
    a = list(map(int, input().split()))
    print(max(a) - min(a))

def c0():
    n = int(input())
    a = list(map(int, input().split()))
    x = []
    def set_col(rate):
        if rate <= 399:
            return '灰色'
        elif rate <= 799:
            return '茶色'
        elif rate <= 1199:
            return '緑色'
        elif rate <= 1599:
            return '水色'
        elif rate <= 1999:
            return '青色'
        elif rate <= 2399:
            return '黄色'
        elif rate <= 2799:
            return '橙色'
        elif rate <= 3199:
            return '赤色'
        else:
            x.append(1)
            return

    res = set(map(set_col, a))
    if None in res: res.remove(None)
    mi = max(1, len(res))
    ma = len(res) + len(x)
    print(mi, ma)

def c():
    n = int(input())
    a = list(map(lambda i: min(8, int(i)//400), input().split()))
    over_rate = a.count(8)
    res = set(a)
    if 8 in res: res.remove(8)

    mi = max(1, len(res))
    ma = len(res) + over_rate
    print(mi, ma)

import numpy as np
def d():
    n = int(input())
    s = input()
    l = [ 1 if x=='(' else -1 for x in s[:] ]
    mt = np.cumsum(l) # mountain
    mi = np.amin(mt)
    left = ''; right = ''
    if mi < 0:
        left = '('*(mi*-1)
    if mt[-1]-mi > 0:
        right = ')'*(mt[-1]-mi)
    # print(mt, mi)
    print(left + s + right)

import numpy as np
# import random
def d2():
    n = int(input())
    s = input()
    l = [ 1 if x=='(' else -1 for x in s[:] ]
    mt = np.cumsum(l) # mountain
    mi = min(0, np.amin(mt))
    left = ''; right = ''
    if mi < 0:
        left = '('*(mi*-1)
    if mt[-1]-mi > 0:
        right = ')'*(mt[-1]-mi)
    # print(mt, mi)
    print(left + s + right)

# d2()
