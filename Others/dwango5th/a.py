N = int(input())
a = [int(ai) for ai in input().split()]

mean = sum(a) / N
mini = (0, abs(a[0] - mean))
for i, ai in enumerate(a):
    if abs(ai - mean) < mini[1]:
        mini = (i, abs(ai - mean))
print(mini[0])
