def solution(n):
    if n == 0 or n == 1:
        return 1

    return solution(n - 1) + solution(n - 2)


def main():
    n = int(input())
    res = solution(n)

    print(res)


if __name__ == '__main__':
    main()
