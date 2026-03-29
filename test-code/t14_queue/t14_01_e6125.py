

class Queue:

    def __init__(self, max_size = 100):
        self.max_size = max_size
        self._size = 0
        self._front = 0
        self._back = 0
        self._items = [None for _ in range(max_size)]


    def push(self,item):
        if self._size > 0:
            self._back = (self._back + 1) % self.max_size
        self._items[self._back] = item
        self._size += 1

        return "ok"

    def pop(self):
        item = self._items[self._front]
        self._size -= 1
        if self._size > 0 :
            self._front = (self._front + 1) % self.max_size

        return item

    def front(self):
        return self._items[self._front]

    def size(self):
        return self._size

    def clear(self):
        self.__init__(self.max_size)
        return "ok"

    @staticmethod
    def exit():
        return "bye"


    def execute(self,command: str):
        method, *args = command.split()
        return getattr(self,method)(*args)


if __name__ == "__main__":
    queue = Queue(100)
    with open("input.txt") as f:
        for line in f:
            result = queue.execute(line)
            print(result)
            if result == "bye":
                break
