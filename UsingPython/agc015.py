# AtCoder Grand Contest 015

def a():
    n, a, b = map(int, input().split())
    if (a > b) or ((a != b)and(n == 1)):
        print(0)
        return
    elif (a == b) and (n == 1):
        print(1)
        return
    else:
        min_sum = a * (n-1) + b
        max_sum = a + b * (n-1)
        num = max_sum - min_sum + 1
        print(num)
        return
    pass

def b():
    s = input()
    n = len(s)
    result = n * (n-1)
    for i in range(1,n):
        # 1,2...n-1
        if s[i] == 'U':
            result += i
        elif s[i] == 'D':
            result += n-1 - i

    print(result)
    pass

def c():
    import numpy as np
    n, m, q = map(int, input().split())
    grid = np.zeros([n*2-1, m*2-1])

    # n*m
    for i in range(n):
        s = list(map(int, input()))
        for j in range(m):
            grid[i*2][j*2] = s[j]

    # n*m
    for i in range(0, 2*n-1, 2): # 0,1,2
        for j in range(0, 2*m-3, 2): # 0,1,2(,3)
            grid[i][j+1] = grid[i][j]*grid[i][j+2]*(-1)

    # n*m
    for j in range(0, 2*m-1, 2):
        for i in range(0, 2*n-3, 2):
            grid[i+1][j] = grid[i][j]*grid[i+2][j]*(-1)

    # q
    ans = []
    for _ in range(q):
        x1, y1, x2, y2 = map(lambda i: (int(i)-1)*2, input().split())
        s = grid[x1:x2+1, y1:y2+1]
        res = s.sum()
        ans.append(res)
        # print(s)
        # print(res)

    for a in ans:
        print(int(a))
    pass

c()

def d():
    a = int(input())
    b = int(input())
    pass
