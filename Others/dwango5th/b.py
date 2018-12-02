N, K = map(int, input().split())
a = [int(ai) for ai in input().split()]

beauty = list()
for i in range(N):
    for j in range(i, N):
        # print(sum(a[i:j+1]), end=', ')
        beauty.append(sum(a[i:j + 1]))
    # print()

inf = 1099511627775
dp = [[0] * K for _ in range((N * (N + 1)) // 2)]
for i in range((N * (N + 1)) // 2 - 1):
    for k in range(K):
        if k > 0:
            dp[i + 1][k] = max(dp[i][k - 1] & beauty[i], dp[i][k])
        else:
            dp[i + 1][k] = max(beauty[i], dp[i][k])
#     print(beauty[i])
# print(dp)

print(max([d[-1] for d in dp]))
