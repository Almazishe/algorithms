import sys


def solution(n1, n2, n3):
    return "WIN" if n1 % 2 == n2 % 2 == n3 % 2 else "FAIL"


def main():
    line = sys.stdin.readline().rstrip()
    sn1, sn2, sn3 = line.split()
    n1 = int(sn1)
    n2 = int(sn2)
    n3 = int(sn3)

    res = solution(n1, n2, n3)

    print(res)


if __name__ == '__main__':
    main()
