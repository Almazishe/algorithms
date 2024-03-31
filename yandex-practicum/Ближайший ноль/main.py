def solution(n, street):
    count = 0

    for i in range(n):
        if street[i] == 0:
            count = 1
            continue
        if count == 0:
            street[i] = float("inf")
            continue

        street[i] = count
        count += 1

    count = 0
    for i in range(n - 1, -1, -1):
        if street[i] == 0:
            street[i] = "0"
            count = 1
            continue
        if count == 0:
            street[i] = str(street[i])
            continue

        street[i] = str(min(street[i], count))
        count += 1

    return " ".join(street)


def main():
    n = int(input())
    street = list(map(int, input().split()))

    res = solution(n, street)

    print(res)


if __name__ == '__main__':
    main()
