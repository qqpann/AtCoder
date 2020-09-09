from collections import defaultdict
from typing import DefaultDict


def main():
    company = defaultdict(list)
    N = int(input())
    for i in range(2, N + 1):
        b = int(input())
        company[b].append(i)

    salary: DefaultDict[int, int] = defaultdict(lambda: 1)
    for k, v in sorted(company.items(), key=lambda x: x[0], reverse=True):
        staffs = [salary[p] for p in v]
        salary[k] = min(staffs) + max(staffs) + 1

    return salary[1]


if __name__ == "__main__":
    print(main())