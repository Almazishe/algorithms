class MyQueueSized:
    def __init__(self, max_size):
        self.max_size = max_size
        self.items = [None] * max_size
        self.qsize = 0
        self.head = 0
        self.tail = 0

    def push(self, x):
        if self.qsize == self.max_size:
            print("error")
            return

        self.items[self.tail] = x
        self.qsize += 1
        self.tail = (self.tail + 1) % self.max_size

    def pop(self):
        if self.qsize == 0:
            print(None)
            return

        head = self.items[self.head]
        self.qsize -= 1
        self.head = (self.head + 1) % self.max_size
        print(head)

    def peek(self):
        if self.qsize == 0:
            print(None)
            return

        print(self.items[self.head])

    def size(self):
        print(self.qsize)


def main():
    n = int(input())
    max_size = int(input())
    queue = MyQueueSized(max_size)

    for _ in range(n):
        command_name, *args = input().split()

        if command_name == "peek":
            queue.peek()
        elif command_name == "push":
            queue.push(int(args[0]))
        elif command_name == "pop":
            queue.pop()
        elif command_name == "size":
            queue.size()


if __name__ == '__main__':
    main()