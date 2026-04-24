from math import ceil, log2


class SegmentTree:

    def __init__(self,array):
        k = len(array)
        n = 1 << ceil(log2(k))

        self.items = [0] * n + array + [0] * (n - k)
        print(self.items)

        for i in range(n - 1, 0, -1):
            self.items[i] = self.items[2 * i] + self.items[2 * i + 1]

        print(self.items)

        self.size = n

    def update(self,pos, new_value):

        pos += self.size
        self.items[pos] = new_value

        while pos > 1:
            pos //= 2
            self.items[pos] = self.items[2 * pos] + self.items[2 * pos + 1]

        print(self.items)

    def sum(self,from_idx, to_idx):

        result = 0
        left = from_idx + self.size
        right = to_idx + self.size

        while left <= right:
            if left % 2 == 1:
                result += self.items[left]
                left += 1

            # if right % 2 == 0:
            #     result += self.items[right]
            #     right -= 1

            left //= 2
            right //= 2


            # if left == right:
            #     result = self.items[left]
            #     break

        return result



if __name__ == "__main__":
    array = [2,3,8,5,9,1,0,0]
    tree = SegmentTree(array)
    # tree.update(5,2)
    print(tree.sum(1,4))
