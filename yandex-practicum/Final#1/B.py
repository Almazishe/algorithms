# https://contest.yandex.ru/contest/22450/run-report/111165254/

def count_values(matrix):
    counts = [0] * 10

    for i in range(4):
        for n in matrix[i]:
            if n.isdigit():
                counts[int(n)] += 1
    return counts


def solution(k, matrix):
    res = 0
    counts = count_values(matrix)

    for t in range(1, 10):
        if 0 < counts[t] <= k * 2:
            res += 1

    return res


def main():
    k = int(input())

    matrix = []
    for i in range(4):
        matrix.append(input())

    res = solution(k, matrix)

    print(res)


if __name__ == '__main__':
    main()
