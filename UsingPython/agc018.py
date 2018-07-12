def a():
    n, k = map(int, input().split())
    A = {int(a) for a in input().split()}

    if k > max(A):
        print('IMPOSSIBLE')
        return
    # combination of two nums in A
    # keep making the combination -
    # until it finds k or doesn't increase in number.
    from itertools import combinations as combi
    l = len(A)
    while True:
        A |= { abs(c[0] - c[1]) for c in combi(A, 2) }
        if k in A or 1 in A:
            print('POSSIBLE')
            return
        if len(A) == l:
            break
        l = len(A)
    print( 'POSSIBLE' if k in A else 'IMPOSSIBLE' )

    # 差が1の組みがあれば絶対可能
    # 差が2の組みがあり、kと偶奇が同じ数があれば可能

a()
