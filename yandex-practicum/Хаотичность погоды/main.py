def solution(n, days):
    res = 0

    days.insert(0, -274)
    days.append(-274)

    for i in range(1, len(days) - 1):
        if days[i] > days[i + 1] and days[i] > days[i - 1]:
            res += 1

    return res


def main():
    n = int(input())
    days = list(map(int, input().split()))

    res = solution(n, days)

    print(res)


if __name__ == '__main__':
    main()
