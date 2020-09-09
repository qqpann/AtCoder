def main():
    N = int(input())
    arr = list(map(int, input().split()))
    total = sum(arr)
    if total % N != 0:
        return -1
    one = total // N
    if one == 0:
        return 0
    # print("one is", one)
    bridges = 0
    begin = 0
    for end in range(len(arr)):
        # print(begin, end, end - begin)
        # print(arr[begin : end + 1], one * (end - begin + 1))
        if sum(arr[begin : end + 1]) == one * (end - begin + 1):
            bridges += end - begin
            begin = end + 1
    return bridges


if __name__ == "__main__":
    res = main()
    print(res)
