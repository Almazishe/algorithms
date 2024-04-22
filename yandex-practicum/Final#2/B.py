# https://contest.yandex.ru/contest/22781/run-report/112490969/
"""
-- ПРИНЦИП РАБОТЫ --
На самом деле логика этой задачи описана в самой задаче. Изза этого сильно думать не пришлось.

``` https://contest.yandex.ru/contest/22781/problems/B/#:~:text=%D0%94%D0%BB%D1%8F%20%D0%B2%D1%8B%D1%87%D0%B8%D1%81%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F%20%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D1%8F,%D1%82%D0%BE%D0%BB%D1%8C%D0%BA%D0%BE%20%D0%B2%D0%B5%D1%80%D1%85%D0%BD%D0%B8%D0%B9%20%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82.
Для вычисления значения выражения, записанного в обратной польской нотации, нужно считывать выражение слева направо и придерживаться следующих шагов:
 1. Обработка входного символа:
     - Если на вход подан операнд, он помещается на вершину стека.
     - Если на вход подан знак операции, то эта операция выполняется над требуемым количеством значений, взятых из стека в порядке добавления. Результат выполненной операции помещается на вершину стека.
 2. Если входной набор символов обработан не полностью, перейти к шагу 1.
 3. После полной обработки входного набора символов результат вычисления выражения находится в вершине стека. Если в стеке осталось несколько чисел, то надо вывести только верхний элемент.
```

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Из описания алгоритма следует, что перед знаком(+, -, *, /) обязательно есть 2 числа
над которыми можно провести операцию с имеющимся после них знаком.

Соответственно постоянно кладя любое число в конец стека и при натыкании на знак,
доставать два последних и кладя их результат обратно в конец, все будет работать))

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --

Общая сложность алгоритма O(n), зависит линейно от длины переданного выражения.
"""

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