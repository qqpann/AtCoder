N, A, B, C = map(int, input().split())
ll = [int(input()) for _ in range(N)]

# 10以下はMP1の方が効率いい。
# 11以上は結合で増やす方が効率いい。
needs = 0
