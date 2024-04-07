class Node:
    def __init__(self, value, next, prev_max):
        self.value = value
        self.next = next
        self.prev_max = prev_max


class StackMaxEffective:
    def __init__(self):
        self.size = 0
        self.max = float('-inf')
        self.last = None

    def push(self, x):
        self.size += 1
        self.last = Node(x, self.last, self.max)
        self.max = max(self.max, x)

    def pop(self):
        if self.size == 0:
            print("error")
            return

        self.size -= 1
        self.last = self.last.next
        if self.last is not None:
            self.max = max(self.last.prev_max, self.last.value)
        else:
            self.max = float('-inf')

    def get_max(self):
        if self.size == 0:
            print(None)
            return
        print(self.max)

    def top(self):
        if self.last is None:
            print("error")
            return
        print(self.last.value)


def main():
    n = int(input())
    stack = StackMaxEffective()

    for _ in range(n):
        command_name, *args = input().split()

        if command_name == "get_max":
            stack.get_max()
        elif command_name == "push":
            stack.push(int(args[0]))
        elif command_name == "pop":
            stack.pop()
        elif command_name == "top":
            stack.top()


if __name__ == '__main__':
    main()
