# A
def a():
    A, B, C = list(map(int, input().split()))
    cnt = 0
    rcd = [[A,B,C]]
    while True:
        if A%2==1 or B%2==1 or C%2==1:
            break
        if [A,B,C] in rcd:
            cnt = -1
            break
        A, B, C = B/2+C/2, A/2+C/2, A/2+B/2 # exchange
        cnt += 1
        rcd.append([A,B,C])
    print(cnt)
    return

# B
def b():

    return

if __name__ == '__main__':
    # a()
    pass
