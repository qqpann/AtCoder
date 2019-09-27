from itertools import combinations
import operator as op
from functools import reduce
from math import factorial as f

def nCr(n,r):
    return f(n) // f(r) // f(n-r)

def calcResult(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    n = n - 1
    possible2 = n // 2
    res = 0
    for r in range(possible2 + 1):
        _n = max(n-2*r+r, r)
        _r = min(n-2*r+r, r)
        res += nCr(_n, _r)
    return res

N, M = map(int, input().split())
prev_a = -1
B = 1
for i in range(M):
    a = int(input())
    B *= calcResult(a - prev_a)
    prev_a = a
B *= calcResult(N - prev_a)

print(int(B % 1000000007))