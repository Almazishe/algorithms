def naive(n, nums, k):
    for i in range(n):
        n1 = nums[i]
        for j in range(i+1, n):
            n2 = nums[j]
            if n1 + n2 == k:
                return (n1, n2)
    return None

def two_pointer(n, nums, k):
    nums = sorted(nums)
    l, r = 0, n-1

    while l < r:
        n1, n2 = nums[l], nums[r]
        if n1 + n2 == k:
            return n1, n2
        elif n1 + n2 < k:
            l+=1
        else:
            r-=1
    return None


def sorted_two_pointer(n, nums, k):
    l, r = 0, n-1

    while l < r:
        n1, n2 = nums[l], nums[r]
        if n1 + n2 == k:
            return n1, n2
        elif n1 + n2 < k:
            l+=1
        else:
            r-=1
    return None


def with_map(_, nums, k):
    nums_map = {v: k for k, v in enumerate(nums)}

    for i, n in enumerate(nums):
        if nums_map.get(k-n, False) and nums_map.get(k-n, -1) != i:
            return n, k-n

    return None

def with_set(_, nums, k):
    nums_set = set()

    for n in nums:
        x = k - n
        if x in nums_set:
            return n, x
        else:
            nums_set.add(n)

    return None

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    k = int(input())

    res = sorted_two_pointer(n, nums, k)

    if res is None:
        print(res)
    else:
        print(*res)


if __name__ == "__main__":
    main()
