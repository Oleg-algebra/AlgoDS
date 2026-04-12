


class BinaryTree:

    def __init__(self,key):

        self.key = key
        self.left: [BinaryTree | None] = None
        self.right: [BinaryTree | None] = None

    def insert(self,key):
        node = self
        while True:
            if key < node.key:
                if node.left is not None:
                    node = node.left
                else:
                    node.left = BinaryTree(key)
                    break

            elif node.key < key:
                if node.right is not None:
                    node = node.right
                else:
                    node.right = BinaryTree(key)
                    break
            else:
                break

    def print(self):

        if self.left is not None:
            self.left.print()
        print(self.key, end="->")
        if self.right is not None:
            self.right.print()


    def height(self):
        stack = [(self,1)]
        max_height = 0
        while stack:
            node, height = stack.pop()
            if height > max_height:
                max_height = height

            if node.left is not None:
                stack.append((node.left,height + 1))

            if node.right is not None:
                stack.append((node.right, height + 1))

        return max_height


if __name__ == "__main__":
    with open("input.txt") as f:
        lst = list(map(int,f.readline().strip().split()))
        if lst[0] == 0:
            print(0)
            exit(0)
        tree = BinaryTree(lst[0])

        for i in range(1,len(lst)):
            if lst[i] == 0:
                break
            tree.insert(lst[i])
        # tree.print()
        # print()
        print(tree.height())



