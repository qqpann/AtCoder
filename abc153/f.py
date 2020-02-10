from collections import deque
N, D, A = map(int, input().split())
XH = []
for _ in range(N):
    x, h = map(int, input().split())
    XH.append((x, h))

XH = sorted(XH, key=lambda xh: xh[0])

bar = 0
count = 0
while XH[-1][1] > 0:
    start, cost = XH[bar]
    throw = cost // A + (1 if cost%A != 0 else 0)
    boom = A * throw
    for i, x, h in enumerate(XH[bar:]):
        if start <= x <= start + 2 * D and h > 0:
            count += throw
            H[i] -= boom
            print(H, throw, boom, count)
        else:
            break

print(count)