n = int(input())
d = {
    i: {j: 0 for j in range(10)} for i in range(1, 10)
}
res = 0
for i in range(n+1):
    str_i = str(i)
    t_i = int(str_i[0])
    b_i = int(str_i[-1])
    if b_i == 0:
        continue
    res += d[b_i][t_i] * 2
    d[t_i][b_i] += 1
    res += 1 if t_i == b_i else 0
print(res)
