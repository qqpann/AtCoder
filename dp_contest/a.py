N = int(input())
H = list(map(int, input().split()))

# memo = [0] + [abs(H[i] - H[i-1]) for i in range(1, N)]
# memo = [H[i] - H[i-1] for i in range(1, N)]
memo = [sum(H)] * (N+2)
memo[0] = 0
for i in range(N):
    memo[i+1] = min(memo[i+1], memo[i] + abs(H[i+1] - H[i]))
    if i > N-3:
        break
    memo[i+2] = min(memo[i+2], memo[i] + abs(H[i+2] - H[i]))

print((memo[N-1]))