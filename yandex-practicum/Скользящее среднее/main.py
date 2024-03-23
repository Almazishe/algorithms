def solution(n: int, arr: list, k: int) -> list:
    summ = sum(arr[:k])
    res = [summ / k]

    for i in range(n - k):
        summ -= arr[i]
        summ += arr[i + k]
        res.append(summ / k)

    return res

def main():
    n = int(input())
    arr1 = list(map(int, input().split()))
    k = int(input())

    res = solution(n, arr1, k)

    print(" ".join(list(map(str, res))))

if __name__ == "__main__":
    main()