# thx: https://python.ms/factorize/#実装
def factorize(n, fct_d):
    fct = dict()
    b, e = 2, 0  # base, exponent
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e = e + 1
        if e > 0:
            fct_d[b] = max(fct_d.get(b, 0), e)
            fct[b] = max(fct_d.get(b, 0), e)
        b, e = b + 1, 0
    if n > 1:
        print('n>1', n)
        fct_d[n] = max(fct_d.get(n, 0), 1)
        fct[n] = max(fct_d.get(n, 0), 1)
    return fct

_ = int(input())
a = list(map(int, input().split()))
fct = dict()
af = list()
for ai in a:
    af.append(factorize(ai, fct))
print(fct)
print(af)
res = 0
for afi in af:
    afin = 1
    for f, n in fct.items():
        afin *= f ** (n - afi.get(f, 0))
        print(f, n, afin)
    res += afin
    print(afin)
print(res % 1000000007)