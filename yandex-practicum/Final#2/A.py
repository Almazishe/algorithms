# https://contest.yandex.ru/contest/22781/run-report/112205170/
"""
-- ПРИНЦИП РАБОТЫ --
Я реализовал Deck используя ограниченный массив элементов
и 2 точки с индексами (head, tail) указывающие на начало
и конец очереди. Все что находится между tail -> head
не учитывается.

Подобно решение мы делали во втором спринте
в задаче "Ограниченная очередь", только добавив методы
push_front и pop_back расширил функционал до
двухстороннего Дека.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Если взять функционал "Ограниченной очереди" он добавляет
элементы в конец и меняет tail на точку будущего элемента,
также с забором элемента с начала индекс head меняется на
индекс элемента удаленного будущего.

Осталось лишь добавить добавление элемента в начало, но
изза того что head изначально указывает на индекс первого
элемента, нужно сначала посчитать новый индекс head и
добавить туда. Также с удаление с конца, так как tail указывает на
пустой элемент(last element + 1) нам сначала нужно посчитать tail
затем удалить его.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --

Добавление в конец/начало - O(1)
Так как добавление по индексу в ограниченный массив O(1)

Удаление с конца/начала - O(1)
Так как при удалении мы не удаляем элемент а просто меняем точку
последнего элемента с конца/начала
"""



class Deck:
    def __init__(self, max_size):
        self.max_size = max_size
        self.items = [None] * max_size
        self.qsize = 0
        self.head = 0
        self.tail = 0

    def push_back(self, x):
        if self.qsize == self.max_size:
            print("error")
            return

        self.items[self.tail] = x
        self.qsize += 1
        self.tail = (self.tail + 1) % self.max_size

    def pop_front(self):
        if self.qsize == 0:
            print("error")
            return

        head = self.items[self.head]
        self.qsize -= 1
        self.head = (self.head + 1) % self.max_size
        print(head)

    def push_front(self, x):
        if self.qsize == self.max_size:
            print("error")
            return

        self.head = (self.head - 1) % self.max_size
        self.items[self.head] = x
        self.qsize += 1

    def pop_back(self):
        if self.qsize == 0:
            print("error")
            return

        self.tail = (self.tail - 1) % self.max_size
        tail = self.items[self.tail]
        self.qsize -= 1
        print(tail)



def main():
    n = int(input())
    max_size = int(input())
    queue = Deck(max_size)

    for _ in range(n):
        command_name, *args = input().split()

        if command_name == "push_back":
            queue.push_back(int(args[0]))
        elif command_name == "push_front":
            queue.push_front(int(args[0]))
        elif command_name == "pop_front":
            queue.pop_front()
        elif command_name == "pop_back":
            queue.pop_back()


if __name__ == '__main__':
    main()