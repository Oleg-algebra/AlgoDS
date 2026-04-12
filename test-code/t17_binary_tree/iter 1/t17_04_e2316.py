import sys
sys.setrecursionlimit(100500)

class BinaryTree:

    def __init__(self,key, parent = None):

        self.key = key
        self.left = None
        self.right = None
        self.size = 1
        self.parent = parent

    def insert(self,key):
        node = self
        while True:
            if key < node.key:
                if node.left is not None:
                    node = node.left
                else:
                    node.left = BinaryTree(key, node)
                    self.size += 1
                    break

            elif node.key < key:
                if node.right is not None:
                    node = node.right
                else:
                    node.right = BinaryTree(key, node)
                    self.size += 1
                    break
            else:
                break

    def print(self):

        if self.left is not None:
            self.left.print()
        if self.left is None and self.right is None:
            print(self.key, end=" ")
            return
        if self.right is not None:
            self.right.print()
        if self.left is None and self.right is None:
            print(self.key, end=" ")
            return


    def getTreeSize(self) -> int:
        return self.size

    def getSecondMax(self):
        node = self
        parent = None
        while node.right is not None:
            parent = node
            node = node.right

        if node.left is None:
            return parent.key

        node  = node.left
        while node.right is not None:
            node = node.right
        return node.key

    def getLeaves(self):
        result = []
        stack = [self]
        while stack:
            node = stack.pop()
            if node.left is None and node.right is None:
                result.append(node.key)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

        return result



if __name__ == "__main__":
    with open("input.txt") as f:
        lst = list(map(int, f.readline().strip().split()))
        if lst[0] == 0:
            exit(0)
        tree = BinaryTree(lst[0])

        for i in range(0, len(lst)):
            if lst[i] == 0:
                break
            tree.insert(lst[i])
        # tree.print()
        # print()
        # print(tree.getSecondMax())
        print(*tree.getLeaves())



