def a():
    a, b, c = map(int, input().split())
    if a <= c <= b:
        print('Yes')
    else:
        print('No')
    pass

def b():
    n, m = map(int, input().split())
    city = [0]*n
    for i in range(m):
        ai, bi = map(int, input().split())
        city[ai-1] += 1
        city[bi-1] += 1
    for c in city: print(c)

def c():
    n, k = map(int, input().split())
    U = []
    for i in range(n):
        U.append(tuple(map(int, input().split())))
    U = sorted(U, key=lambda i: i[0])
    # print(U)
    for i in U:
        k -= i[1]
        if k <= 0:
            print(i[0])
            break

def d1():
    n, m = map(int, input().split())
    node = []
    for i in range(m):
        ai, bi, ci = map(int, input().split())
        node.append([ai, bi, ci])
    # node = sorted(node, key=lambda n: n[1])
    node = sorted(node, key=lambda n: n[0])
    route = []
    score = None
    for i in node:
        ai, bi, ci = i
        if ai == 1:
            route.append([[ai, bi], ci])
        elif 1 < ai < n:
            temp = []
            for j in route:
                if j[0][-1] == ai:
                    k = [j[0][:],j[1]]
                    k[0].append(bi); k[1]+=ci
                    temp.append(k)
            else:
                route.extend(temp)
        else:
            for j in route:
                if bi in j[0]:
                    print('inf')
                    return
    for i in route:
        if i[0][-1] == n:
            if score == None:
                score = k[1]
            else:
                score = max(score, k[1])
    print(score)
    # print(route)
    pass

def d():
    n, m = map(int, input().split())
    node = []
    for i in range(m):
        ai, bi, ci = map(int, input().split())
        node.append([ai, bi, ci])
    node = sorted(node, key=lambda n: n[0])
    route = [None]*n
    route[0] = 0
    updated = True
    updated_route = []
    while updated:
        updated = False
        temp_updated_route = []
        for i in node:
            ai, bi, ci = i
            if route[ai-1] != None:
                # then, reflesh bi.
                if route[bi-1] == None:
                    route[bi-1] = route[ai-1] + ci
                else:
                    if route[bi-1] < route[ai-1] + ci:
                        route[bi-1] = route[ai-1] + ci
                        updated = True
                        temp_updated_route.append(bi-1)
        if temp_updated_route in updated_route:
            print('inf')
            break
        if updated:
            updated_route.append(temp_updated_route)
    else:
        print(route[-1])
    print(route, updated_route)
    pass

d()
