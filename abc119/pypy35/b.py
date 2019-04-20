N = int(input())

otoshidama = 0.
for _ in range(N):
    x, u = input().split()
    x = float(x)
    if u == 'JPY':
        otoshidama += x
    else:
        otoshidama += (x * 380000.)

print(otoshidama)
