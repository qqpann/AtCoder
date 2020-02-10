h = int(input())

count = 0
n = 1
while h > 1:
    count += n
    h = h // 2
    n = n * 2
print(count + n)