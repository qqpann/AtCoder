n, k = map(int, input().split())
ps = list(map(int, input().split()))


# TLE
# for i in range(k - 1, n):
#     print(sorted(ps[: i + 1], reverse=True)[k - 1])


# TLE
# from bisect import insort
# tmp = sorted(ps[:k])
# key = tmp[-k]
# print(key)
# for i in range(k, n):
#     if key > ps[i]:
#         print(key)
#         continue
#     insort(tmp, ps[i])
#     key = tmp[-k]
#     print(key)

import heapq

heap = ps[:k]
heapq.heapify(heap)
root = heapq.heappop(heap)
print(root)
for i in range(k, n):
    if root > ps[i]:
        print(root)
    else:
        heapq.heappush(heap, ps[i])
        root = heapq.heappop(heap)
        print(root)
