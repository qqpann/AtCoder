n = input()
n = n.rstrip("0")
print("Yes" if n == n[::-1] else "No")
