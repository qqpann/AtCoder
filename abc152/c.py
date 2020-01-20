n = int(input())
p = list(map(int, input().split()))

count = 0
m = p[0]
for pi in p:
    if m >= pi:
        count += 1
    m = min(m, pi)
print(count)