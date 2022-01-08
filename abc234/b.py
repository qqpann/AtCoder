from math import sqrt

n = int(input())
xs, ys = [], []
for _ in range(n):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)

dist = 0
for i in range(n):
    for j in range(i, n):
        if i == j:
            continue
        xdiff = abs(xs[i] - xs[j])
        ydiff = abs(ys[i] - ys[j])
        dist = max(dist, sqrt(xdiff ** 2 + ydiff ** 2))
print(dist)
