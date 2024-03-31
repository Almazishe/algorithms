def solution(b1, b2):
    if b1 == b2 == "0":
        return 0

    ml = max(len(b1), len(b2))
    b1 = b1.zfill(ml)
    b2 = b2.zfill(ml)
    res = []
    remainder = 0

    for i in range(ml - 1, -1, -1):
        summ = int(b1[i]) + int(b2[i]) + remainder
        res.insert(0, str(summ % 2))
        remainder = summ // 2

    if remainder > 0:
        res.insert(0, str(remainder))

    return "".join(res)


def main():
    b1 = input()
    b2 = input()

    res = solution(b1, b2)

    print(res)


if __name__ == '__main__':
    main()
