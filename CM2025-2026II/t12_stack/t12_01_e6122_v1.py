class Stack:

    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)
        return "ok"

    def pop(self):
        return self._items.pop()

    def back(self):
        return self._items[-1]

    def size(self):
        return len(self._items)

    def clear(self):
        self._items = []
        return "ok"

    def exit(self):
        return "bye"

    def execute(self, command: str):
        method, *args = command.split()
        return getattr(self, method)(*args)


if __name__ == "__main__":
    with open("input.txt") as f:
        stack = Stack()
        for line in f:
            res = stack.execute(line)
            print(res)
            if res == "bye":
                break




