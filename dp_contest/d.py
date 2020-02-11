N, WW = map(int, input().split())
W, V = [], []
for _ in range(N):
    _w, _v = list(map(int, input().split()))
    if _w > WW:
        continue
    W.append(_w)
    V.append(_v)

# dp = [[0] * (WW+1) for _ in range(N+1)]
dp = [[0] * (N+1) for _ in range(WW+1)]
for j in range(WW+1):
    # アイテムの数だけ探索する
    for i in range(1, N+1):
        w = W[i-1]
        v = V[i-1]
        if j+w > WW:
            continue
        dp[j+w][i] = max(dp[j+w][i-1], max(dp[j][:i]) + v)

# import numpy as np
# print(np.array(dp))
print(max(dp[WW]))
