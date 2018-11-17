from collections import deque

N = int(input())


# 0 or 5
# 1-4 -> 0
# 6-9 -> 5
# 0-4 -> 0
# 5-9 -> 5
def s_int(s):
    n = int(s[3])
    return s[:3] + ('5' if n // 5 % 2 else '0')


# 0 or 5
# 1-4 -> 5
# 6-9 -> 0
# 1-5 -> 5
# 6-0 -> 0
def e_int(e):
    n = int(e[3])
    if 1 <= n <= 5:
        return e[:3] + '5'
    elif 6 <= n <= 9:
        return str(int(e[:3]) * 10 + 10)
    else:
        return e


def get_se(l):
    return (s_int(l[0]), e_int(l[1]))


se = deque(sorted([get_se(input().split('-'))
                   for _ in range(N)], key=lambda x: x[0]))

last_e = ''
while len(se):
    s, e = se.popleft()
    if s <= last_e:
        last_e = max(e, last_e)
        continue
    elif last_e:
        print(last_e, str(s) + '-', sep='\n', end='')
        last_e = max(e, last_e)
    else:
        print(s, end='-')
        last_e = max(e, last_e)
print(last_e)
