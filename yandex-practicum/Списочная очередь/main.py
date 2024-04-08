class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next
        self.prev = None

class Queue:
    def __init__(self):
        self.qsize = 0
        self.tail = None
        self.head = None

    def put(self, x):
        self.qsize += 1
        self.tail = Node(x, self.tail)

        if self.qsize == 1:
            self.head = self.tail
        else:
            self.tail.next.prev = self.tail

    def get(self):
        if self.qsize == 0:
            print("error")
            return

        head = self.head
        self.head = self.head.prev
        self.qsize -= 1
        print(head.value)

    def size(self):
        print(self.qsize)

def main():
    n = int(input())
    queue = Queue()

    for _ in range(n):
        command_name, *args = input().split()

        if command_name == "put":
            queue.put(int(args[0]))
        elif command_name == "get":
            queue.get()
        elif command_name == "size":
            queue.size()


if __name__ == '__main__':
    main()