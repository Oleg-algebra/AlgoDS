from math import ceil, log2


class SegmentTree:

    def __init__(self, array):

        k = len(array)
        n = 1 << ceil(log2(k))
        # print(n)
        self.items = [0]*n + array + [0]*(n - k)
        # print(self.items)
        for i in range(n - 1, 0, -1):
            self.items[i] = self.items[2 * i] + self.items[2 * i + 1]

        # print(self.items)
        self.size = n


    def update(self,pos,new_value):
        pos += self.size
        self.items[pos] = new_value

        while pos > 1:
            pos //= 2
            self.items[pos] = self.items[2*pos] + self.items[2*pos + 1]

        # print(self.items)

    def sum(self,from_idx, to_idx):

        left = from_idx + self.size
        right = to_idx + self.size
        res = 0
        iteration = 1

        while left <= right:
            # print(f"\nІтерація №{iteration}:")
            # print(f"  Поточні маркери: left={left}, right={right}")

            # Перевірка лівого маркера
            if left % 2 == 1:
                # print(f"  [!] left({left}) - правий син. Додаємо {self.items[left]} до суми.")
                res += self.items[left]
                left += 1
                # print(f"      Зміщуємо left на {left}")
            else:
                # print(f"  [ ] left({left}) - лівий син. Чекаємо підйому до батька.")
                pass

            # Перевірка правого маркера
            if right % 2 == 0:
                # print(f"  [!] right({right}) - лівий син. Додаємо {self.items[right]} до суми.")
                res += self.items[right]
                right -= 1
                # print(f"      Зміщуємо right на {right}")
            else:
                # print(f"  [ ] right({right}) - правий син. Чекаємо підйому до батька.")
                pass

            # Підйом вгору
            left //= 2
            right //= 2
            # print(f"  Піднімаємося на рівень вище: нові left={left}, right={right}")
            # print(f"  Поточна сума res = {res}")
            iteration += 1

        # print(f"\n--- Фінальний результат: {res} ---")
        return res


if __name__ == "__main__":
    arr = [2,4,7,8,3,1,0,0]
    # arr = [2,4,7,8,3,1,0,0]
    # n = len(arr)
    # arr = [0]*n + arr
    # print(arr)
    # arr = [0, 25, 21, 4, 6, 15, 4, 0, 2, 4, 7, 8, 3, 1, 0, 0]
    # tree = SegmentTree(arr)
    # # tree.update(5,3)
    # tree.sum(0,7)

    with open("input.txt") as f:

        n,q = map(int,f.readline().split())
        array = list(map(int,f.readline().split()))
        tree = SegmentTree(array)
        for _ in range(q):
            cmd,x,y = f.readline().split()
            x = int(x)
            y = int(y)

            if cmd == "?":
                print(tree.sum(x - 1, y - 1))
            elif cmd == "=":
                tree.update(x - 1, y)