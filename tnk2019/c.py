N = int(input())
S = input()

w = S.count('.')
b = 0

k = w

for i in range(N):
    if S[i] == '.':
        w -= 1
    else:
        b += 1

    k = min(k, w + b)

print(k)
