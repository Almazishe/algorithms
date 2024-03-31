def solution(n):
    degree = 0
    temp = 1

    while temp <= n:
        if temp == n:
            return True

        degree += 1
        temp = 4 ** degree

    return False


def main():
    n = int(input())

    res = solution(n)

    print(res)


if __name__ == '__main__':
    main()
