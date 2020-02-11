import numpy as np
N = int(input())
ABC = np.zeros([N, 3])
for i in range(N):
    ABC[i] = list(map(int, input().split()))

dp = np.zeros([N, 3])
dp[0] = ABC[0]
for i in range(N-1):
    dp[i+1, 0] = max(dp[i, 1], dp[i, 2]) + ABC[i+1, 0]
    dp[i+1, 1] = max(dp[i, 0], dp[i, 2]) + ABC[i+1, 1]
    dp[i+1, 2] = max(dp[i, 0], dp[i, 1]) + ABC[i+1, 2]

print(int(max(dp[N-1])))