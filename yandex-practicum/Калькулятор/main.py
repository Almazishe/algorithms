# https://contest.yandex.ru/contest/22781/run-report/112490969/

def solution(exp: list[str]) -> int:
    stack = []

    commands = {
        "-": "__sub__",
        "+": "__add__",
        "*": "__mul__",
        "/": "__floordiv__"
    }

    for el in exp:
        if el.lstrip('-').isdigit():
            stack.append(int(el))
        else:
            command_name = commands[el]
            n2 = stack.pop()
            n1 = stack.pop()
            command = getattr(n1, command_name)
            stack.append(command(n2))
    return stack.pop()


def main():
    exp = input().split()
    res = solution(exp)
    print(res)


if __name__ == '__main__':
    main()