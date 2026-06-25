

class MaxHeap:

    def __init__(self):
        self._items: list[int] = []

    def insert(self,item: int):
        self._items.append(item)
        # print(f"added {item}: ",self._items)
        self.siftUp(len(self._items) - 1)

    def extract_maximum(self) -> int:
        self.swap(0,-1)
        # print(f'moved max {self._items[-1]} : ', self._items)
        item = self._items.pop()
        # print(f'extracted {item} : ',self._items)
        self.siftDown(0)
        return item

    def parent(self,idx: int) -> int:
        return (idx - 1) // 2

    def leftChild(self,idx: int) -> int:
        return 2*idx + 1

    def rightChild(self,idx: int ) -> int:
        return 2*idx + 2

    def swap(self,idx1,idx2):
        self._items[idx1], self._items[idx2] = self._items[idx2], self._items[idx1]

    def siftUp(self,idx):
        i = idx
        while i > 0:
            parent = self.parent(i)
            if self._items[parent] >= self._items[i]:
                break

            self.swap(i,parent)
            # print(f"sift up: {self._items[i]} {self._items[parent]} ", self._items)
            i = parent

    def siftDown(self,idx):
        i = idx
        while self.leftChild(i) < len(self._items):
            left = self.leftChild(i)
            right = self.rightChild(i)
            if right < len(self._items) and self._items[left] < self._items[right]:
                max_child = right
            else:
                max_child = left

            if self._items[max_child] <= self._items[i]:
                break

            self.swap(i,max_child)
            # print(f"sift down: {self._items[i]} {self._items[max_child]} ", self._items)
            i = max_child


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline().strip())
        heap = MaxHeap()
        for i in range(n):
            cmd_id, *args = map(int,f.readline().split())
            if cmd_id == 0:
                heap.insert(*args)
            elif cmd_id == 1:
                print(heap.extract_maximum())



