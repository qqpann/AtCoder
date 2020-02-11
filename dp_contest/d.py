N, WW = map(int, input().split())
W, V = [], []
for _ in range(N):
    _w, _v = list(map(int, input().split()))
    if _w > WW:
        continue
    W.append(_w)
    V.append(_v)

dp = [[0] * (WW+1) for _ in range(N+1)]
for i in range(1, N+1):
    # i := 1...N
    for j in range(1, WW+1):
        # j := 0...WW
        
        wi = W[i-1]
        vi = V[i-1]
        if j-wi < 0:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-wi] + vi)

# import numpy as np
# print(np.array(dp))
print(dp[N][WW])