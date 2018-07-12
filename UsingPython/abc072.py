def a():
    x, t = map(int, input().split())
    print(max(0, x - t))


def b():
    s = input()
    print(s[::2])


def c():
    n = int(input())
    a = [int(ai) for ai in input().split()]
    maxN = 10**5
    A = [0]*maxN
    for i in a:
        A[i] += 1
        if i != 0:
            A[i-1] += 1
        if i != maxN-1:
            A[i+1] += 1
    print(max(A))


def d():
    from collections import deque
    n = int(input())
    p = [int(pi) for pi in input().split()]
    continuous = deque()
    tmp = 0
    for i, k in enumerate(p):
        if i+1 == k:
            tmp += 1
        else:
            if tmp > 0:
                continuous.append(tmp)
            tmp = 0
    else:
        if tmp > 0:
            continuous.append(tmp)
        tmp = 0
    res = 0
    while len(continuous):
        k = continuous.popleft()
        res += k//2 + k%2
    print(res)

d()
