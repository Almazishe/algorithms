def solution(n, k):
    i1, i2 = 1, 1

    for i in range(n - 1):
        i1, i2 = i2, i1
        i2 += i1

    return i2 % (10 ** k)

# With arr
def solution_arr(n, k):
    fibb = [1, 1]

    for i in range(n - 1):
        fibb.append(fibb[-1] + fibb[-2])

    return fibb[n] % (10 ** k)


def main():
    in_arr = input().split()
    n = int(in_arr[0])
    k = int(in_arr[1])
    res = solution(n, k)

    print(res)


if __name__ == '__main__':
    main()
