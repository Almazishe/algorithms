def is_correct_bracket_seq(seq: str):
    stack = []

    brackets = {
        "}": "{",
        "]": "[",
        ")": "(",
    }

    for bracket in seq:
        if bracket in brackets.values():
            stack.append(bracket)
        elif stack and brackets[bracket] == stack[-1]:
            stack.pop()
        else:
            return False

    return len(stack) == 0


def main():
    seq = input()

    print(is_correct_bracket_seq(seq))


if __name__ == '__main__':
    main()