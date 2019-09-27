n, y = map(int, input().split())

found = False
for a in range(n+1):
    for b in range(n-a+1):
        c = n - a - b
        total = 10000 * a + 5000 * b + 1000 * c
        if total == y:
            found = True
            print(a, b, c)
            break
    if found:
        break

if not found:
    print('-1 -1 -1')