def a():
    x, a, b = map(int, input().split())
    print('A' if abs(x-a) < abs(x-b) else 'B')


def b():
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    s = input()
    # print(set(alphabets), set(s))
    diff = set(alphabets) - set(s)
    try:
        print( sorted(list(diff))[0] )
    except:
        print('None')


def c():
    from collections import deque
    n = int(input())
    A = [int(ai) for ai in input().split()]
    A = deque(sorted(A, reverse=True))
    xy = []
    for i in range(1, n):
        # print(A)
        if A[0] == A[1]:
            tmp = A.popleft(); A.popleft()
            xy.append(tmp)
        else:
            A.popleft()

        if len(xy) == 2:
            print(xy[0] * xy[1])
            break
    if len(xy) < 2:
        print(0)


def d():
    N  = int(input())
    S1 = input()
    S2 = input()
    from collections import deque
    s = deque(S1)
    S = ''
    for _ in range(N):
        if len(s) >= 2:
            if s[0] == s[1]:
                S += 'Z'
                s.popleft()
                s.popleft()
            else:
                S += 'I'
                s.popleft()
        elif len(s) == 1:
            S += 'I'
            s.popleft()
        else:
            break
    res = 6 if S[0] == 'Z' else 3
    for i in range(len(S)-1):
        if S[i:i+2] == 'II':
            res *= 2
        if S[i:i+2] == 'IZ':
            res *= 2
        if S[i:i+2] == 'ZI':
            res *= 1
        if S[i:i+2] == 'ZZ':
            res *= 3
    print(res % 1000000007)

d()
