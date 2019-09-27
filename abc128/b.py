N = int(input())
L = list()
for i in range(N):
    s, p = input().split()
    p = int(p)
    L.append((s, p, i+1))

L.sort(key=lambda x: x[1], )
L.sort(key=lambda x: x[0], reverse=True)
for _, _, i in reversed(L):
    print(i)