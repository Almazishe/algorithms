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