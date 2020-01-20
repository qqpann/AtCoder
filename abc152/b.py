a, b = map(int, input().split())
ab = str(a)*b
ba = str(b)*a
print(ba if ba < ab else ab)