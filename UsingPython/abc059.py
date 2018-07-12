# abc = input().split(' ')
# ABC = ''
# for i in abc:
#     ABC += i[0]
# ABC = ABC.upper()
# print(ABC)

# a = int(input())
# b = int(input())
# if a > b:
#     print("GREATER")
# elif a < b:
#     print("LESS")
# else:
#     print("EQUAL")

n = int(input())
a = input().split(' ')
a = map(int, a)
plus = lambda x: True if x > 0 else False if x < 0 else 0

i = 0
while i < n:
    if plus(sum(a[:i+1])) != plus(sum(a[:i])) and sum(a[:i+1]) != 0:
        pass


    i += 1
