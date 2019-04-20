def c():
    h, w = map(int, input().split())
    if (h*w)%3 == 0: print(0); return

    # S = h * w
    # one_three_S = S / 3
    # approx_P =
    # def approx_cut(one_three_S):
    #     s = one_three_S
    #     h1, h2 = s//w, s//w+1
    #     w1, w2 = s//h, s//h+1
    # diff =
    s = h * w
    ave_s = s // 3
    dif_s = s % 3
    def func(i, j):
        # func(h, w)
        candidate1 = ave_s // i
        candidate2 = candidate1 + 1

        func(w, h)

def d():
    n = int(input())
    lst = list(map(int, input().split()))

    import numpy as np
    # former half = 2N, latter half = N
    # gradually shift to
    # former half = N, latter half = N
    score = -10**(5*9)
    for sep in range(n-1, 2*n):
        a = np.array(lst)
        a_rank = a.argsort()[::-1]

        fh = sep+1
        lh = 3*n - fh
        fh_ru = fh - n
        lh_rf = 3*n - (lh - n)
        b = np.hstack([a_rank[:fh_ru],a_rank[lh_rf:]])
        print(a_rank, b, fh, lh, fh_ru, lh_rf)
        a[b] = 0
        # print(a)
        sum_fh = np.sum(a[:fh])
        sum_lh = np.sum(a[3*n-lh:])
        # print(a, sum_fh, sum_lh)
        score = max(score, int(sum_fh - sum_lh))

    print(score)
d()
