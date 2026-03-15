


class Stack:

    def __init__(self,max_size = 100):
        self._items = [0 for _ in range(max_size)]
        self.top = -1

    def push(self,item):
        self.top += 1
        self._items[self.top] = item
        return "ok"

    def pop(self):
        item = self._items[self.top]
        self.top -= 1
        return item

    def back(self):
        return self._items[self.top]

    def size(self):
        return self.top + 1

    def clear(self):
        self.__init__(len(self._items))
        return "ok"

    def exit(self):
        return "bye"


    def execute(self,command: str):
        method, *args = command.split()
        return getattr(self,method)(*args)


if __name__ == "__main__":
    with open("input.txt") as f:
        stack = Stack()
        for line in f:
            res = stack.execute(line)
            print(res)
            if res == "bye":
                break




