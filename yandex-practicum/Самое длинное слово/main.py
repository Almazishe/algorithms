def solution(sentence):
    res_word = ""
    res_length = 0

    temp_word = ""
    temp_length = 0

    for letter in sentence:
        if letter.isspace():
            temp_word = ""
            temp_length = 0
        else:
            temp_word += letter
            temp_length += 1

        if temp_length > res_length:
            res_word = temp_word
            res_length = temp_length

    return f"{res_word}\n{res_length}"


def main():
    _ = int(input())
    sentence = input()

    res = solution(sentence)

    print(res)


if __name__ == '__main__':
    main()
