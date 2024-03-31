def solution(s):
    l, r = 0, len(s) - 1
    s = s.upper()

    while l < r:
        if not s[l].isalnum():
            l += 1
            continue

        if not s[r].isalnum():
            r -= 1
            continue

        if s[l] != s[r]:
            return False
        else:
            l += 1
            r -= 1

    return True


def main():
    s = input()

    res = solution(s)

    print(res)


if __name__ == '__main__':
    main()
