# https://contest.yandex.ru/contest/22450/run-report/111030981/

def count_values(matrix):
    counts = {}
    for i in range(4):
        for j in range(4):
            n = matrix[i][j]
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1
    return counts


def solution(k, matrix):
    res = 0
    counts = count_values(matrix)

    for t in range(1, 10):
        if str(t) not in counts:
            continue

        if counts[str(t)] <= k * 2:
            res += 1

    return res


def main():
    k = int(input())

    matrix = []
    for i in range(4):
        row = []
        for n in input():
            row.append(n)
        matrix.append(row)

    res = solution(k, matrix)

    print(res)


if __name__ == '__main__':
    main()
