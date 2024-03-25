def solution(m, n, x, y, matrix):
    res = []

    if x > 0:
        res.append(str(matrix[x - 1][y]))
    if x < n - 1:
        res.append(str(matrix[x + 1][y]))
    if y > 0:
        res.append(str(matrix[x][y - 1]))
    if y < m - 1:
        res.append(str(matrix[x][y + 1]))

    return " ".join(sorted(res))


def main():
    n = int(input())
    m = int(input())
    matrix = []

    for i in range(n):
        matrix.append(list(map(int, input().split())))

    x = int(input())
    y = int(input())

    res = solution(m, n, x, y, matrix)

    print(res)


if __name__ == '__main__':
    main()
