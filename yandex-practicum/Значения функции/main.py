import sys


def solution(a, x, b, c):
    return a * x * x + b * x + c


def main():
    line = sys.stdin.readline().rstrip()
    sa, sx, sb, sc = line.split()
    a = int(sa)
    x = int(sx)
    b = int(sb)
    c = int(sc)

    res = solution(a, x, b, c)

    print(res)


if __name__ == '__main__':
    main()
