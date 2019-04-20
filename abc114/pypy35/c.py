# 357
# 0,1,2
# 1000000000
#  777777753
N = int(input())
tfs = '0357'


count = 0
a = [0] * 6 + [1, 2, 3]
gen = int(''.join([tfs[i] for i in a]))
while gen < N:
    s = str(gen)
    if '3' in s and '5' in s and '7' in s:
        count += 1
    a[-1] += 1
    for i in range(len(a)):
        if a[len(a) - i - 1] > 3:
            a[len(a) - i - 1] = 1
            a[len(a) - i - 1 - 1] += 1
        else:
            gen = int(''.join([tfs[i] for i in a]))
            break


print(count)
