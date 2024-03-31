def solution(s1, s2):
    mp = {}
    for l in s1:
        if l in mp:
            mp[l] += 1
        else:
            mp[l] = 1

    for l in s2:
        if l not in mp:
            return l
        mp[l] -= 1
        if mp[l] < 0:
            return l
    return None


def main():
    s1 = input()
    s2 = input()

    res = solution(s1, s2)

    print(res)


if __name__ == '__main__':
    main()
