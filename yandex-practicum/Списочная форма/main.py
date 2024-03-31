def solution(X, K):
    if X == K == "0":
        return 0

    ml = max(len(X), len(K))

    X = X.zfill(ml)
    K = K.zfill(ml)
    res = []
    remainder = 0

    for i in range(ml - 1, -1, -1):
        summ = int(X[i]) + int(K[i]) + remainder
        res.insert(0, str(summ % 10))
        remainder = summ // 10

    if remainder > 0:
        res.insert(0, str(remainder))

    return " ".join(res)


def main():
    input()
    X = "".join(input().split())
    K = input()

    res = solution(X, K)

    print(res)


if __name__ == '__main__':
    main()
