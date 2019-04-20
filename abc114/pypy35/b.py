s = input()
target = 753
diff = abs(int(s[:3]) - target)
for si in range(len(s) - 3 + 1):
    diff = min(diff, abs(int(s[si:si + 3]) - target))
print(diff)
