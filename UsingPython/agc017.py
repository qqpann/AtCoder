def a():
    # import math
    # import itertools
    import scipy.misc as scm

    n, p = map(int, input().split())
    A = [int(a)%2 for a in input().split()]
    odd = A.count(1)
    even = A.count(0)
    def combination(pick_from, pick_how_many):
        # return math.factorial(pick_from) / math.factorial(pick_how_many)
        # return len(list(itertools.combinations(range(pick_from), pick_how_many)))
        return scm.comb(pick_from, pick_how_many, 1)

    result = 0
    for o in range(0+p, odd+1, 2):
        for e in range(0, even+1):
            result += combination(even, e) * combination(odd, o)
    print(result)


def b():
    n, a, b, c, d = map(int, input().split())
    distance = abs(a - b)


def c():
    n, m = map(int, input().split())
    A = [int(a) for a in input().split()]
    nums = [0]*201
    for i in range(1,201):
        nums[i] = A.count(i)

    # print(nums)

    for _ in range(m):
        x, y = map(int, input().split())
        nums[A[x-1]] -= 1; nums[y] += 1
        A[x-1] = y
        

c()
