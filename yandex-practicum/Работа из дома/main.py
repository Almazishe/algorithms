def solution(n):
    if n == 0:
        return 0

    res = []

    while n != 0:
        res.insert(0, str(n % 2))
        n //= 2

    return "".join(res)


def main():
    n = int(input())

    res = solution(n)

    print(res)


if __name__ == '__main__':
    main()
