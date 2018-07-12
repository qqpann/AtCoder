def a():
    n, m = map(int, input().split())
    print((n-1) * (m-1))


def b():
    s = input()
    print(s[0] + str(len(s) - 2) + s[-1])


def c():
    n = int(input())
    a = [int(ai) for ai in input().split()]
    div = {4:0, 2:0, 1:0}
    for i in a:
        if i % 4 == 0:
            div[4] += 1
        elif i % 2 == 0:
            div[2] += 1
        else:
            div[1] += 1
    if div[2] == 0:
        need = -1
    else:
        need = 0
    if div[4] - div[1] >= need:
        print('Yes')
    else:
        print('No')


def d():
    h, w = map(int, input().split())
    n = int(input())
    a = [int(ai) for ai in input().split()]
    s = ''
    tmp = ''
    for i in range(h*w):
        if (i // w) % 2 == 0:
            # print('l2r')
            # from left to right
            tmp += '{'+str(i)+'}'
            if i%w == w-1:
                tmp += '\n'
                s += tmp
                tmp = ''
            else:
                tmp += ' '
        else:
            # print('r2l')
            # from right to left
            tmp = '{'+str(i)+'}' + tmp
            if i%w == w-1:
                tmp += '\n'
                s += tmp
                tmp = ''
            else:
                tmp = ' ' + tmp
    aa = []
    for i, n in enumerate(a):
        aa += [i+1]*n
    print(s.format(*aa)[:-1])

d()
