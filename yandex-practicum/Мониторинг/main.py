def solution(matrix, n, m):
    for i in range(m):
        for j in range(n):
            print(matrix[j][i], end=" ")
        print()


def main():
    n = int(input())
    m = int(input())

    matrix = []

    for i in range(n):
        matrix.append(input().split())

    solution(matrix, n, m)



if __name__ == '__main__':
    main()
