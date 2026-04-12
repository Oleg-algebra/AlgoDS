

class Node:
    def __init__(self,key,left=None,right = None):
        self.key = key
        self.left = left
        self.right = right

    def hasLeft(self):
        return self.left is not None

    def hasRight(self):
        return self.right is not None

    def getLeft(self) :
        return self.left
    def getRight(self):
        return self.right

    def setLeft(self, key):
        self.left = Node(key)

    def setRight(self, key):
        self.right = Node(key)

class BinaryTree:

    def __init__(self, root: Node):
        self.root = root
        self.size = 1


    def insert(self, key):
        node = self.root
        while True:
            if key < node.key:
                if node.hasLeft():
                    node = node.getLeft()
                else:
                    node.setLeft(key)
                    self.size += 1
                    break
            elif key > node.key:
                if node.hasRight():
                    node = node.getRight()
                else:
                    node.setRight(key)
                    self.size += 1
                    break

            else:
                break

    def getTreeSize(self) -> int:
        return self.size

if __name__ == "__main__":
    with open("input.txt") as f:
        lst = [int(x) for x in f.readline().split()]
        if lst[0] == 0:
            print(0)
            exit(0)
        tree = BinaryTree(Node(lst[0]))
        for i in range(1,len(lst)):
            if lst[i] == 0:
                break
            tree.insert(lst[i])

        print(tree.getTreeSize())