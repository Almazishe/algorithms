class StackMax:
    def __init__(self):
        self.size = 0
        self.items = []

    def push(self, x):
        self.size += 1
        self.items.append(x)

    def pop(self):
        if self.size == 0:
            return "error"
        self.size -= 1
        return self.items.pop()

    def get_max(self):
        if self.size == 0:
            return None
        return max(self.items)


def main():
    n = int(input())
    stack = StackMax()

    for _ in range(n):
        command_name, *args = input().split()

        if command_name == "get_max":
            print(stack.get_max())
        elif command_name == "push":
            stack.push(int(args[0]))
        elif command_name == "pop":
            res = stack.pop()
            if isinstance(res, str):
                print(res)

if __name__ == '__main__':
    main()
