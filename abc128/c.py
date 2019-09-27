N, M = map(int, input().split())
mat = list()
for _ in range(M):
    mat.append(list(map(lambda x: int(x)-1, input().split()[1:])))
p = list(map(int, input().split()))

from itertools import product
bit = product([1, 0], repeat=N)

total = 0
for switch in bit:
    for i, m in enumerate(mat):
        ison = 0
        for j in m:
            ison += switch[j] 
        match = ison % 2 == p[i]
        if not match:
            break
    else:
        total += 1
print(total)