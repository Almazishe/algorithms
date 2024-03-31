def get_primes(n):
    nums = list(range(n+1))
    primes = []

    for num in range(2, n):
        if prime := nums[num]:
            primes.append(prime)
            for i in range(num * num, n + 1, num):
                nums[i] = False

    return primes


def is_prime(n):
    if n == 1:
        return True

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def solution(n):
    i = 2
    while not is_prime(n):
        if n % i == 0:
            print(i, end=" ")
            n /= i
            continue
        i += 1

    if n > 1:
        print(int(n))


def main():
    n = int(input())
    solution(n)


if __name__ == '__main__':
    main()
