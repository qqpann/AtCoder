H, n = map(int, input().split())
A, B = [], []
for _ in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

dp = [1000000000] * (H + max(A) + 1)
dp[0] = 0

for n in range(H+1):
    for a, b in zip(A, B):
        dp[n + a] = min(dp[n + a], dp[n] + b)

print(min(dp[H:]))