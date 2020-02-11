N = int(input())
ABC = []
for i in range(N):
    ABC.append(list(map(int, input().split())))

dp = [[0]*3 for _ in range(N)]
dp[0] = ABC[0]
for i in range(N-1):
    dp[i+1][0] = max(dp[i][1], dp[i][2]) + ABC[i+1][0]
    dp[i+1][1] = max(dp[i][0], dp[i][2]) + ABC[i+1][1]
    dp[i+1][2] = max(dp[i][0], dp[i][1]) + ABC[i+1][2]

print(max(dp[N-1]))