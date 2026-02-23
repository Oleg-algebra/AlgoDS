import math
import sys


input = sys.stdin.readline

def is_prime(n):

    for i in range(2,int(math.sqrt(n)+1)):
        if n % i == 0:
            return False

    return True

class Node:

    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None




class Dict:

    M = 31

    def __init__(self,size: int = 1000003):
        self.size = size
        self.count = 0
        self.slots: list[None | Node] = [None for _ in range(size)]

    def hash(self,key):

        h = 0
        for s in key:
            h = (h * self.M + ord(s)) % self.size

        return h




    def set(self,key,value):



        h = self.hash(key)
        node = self.slots[h]
        while node is not None:
            if node.key == key:
                node.value = value

            node = node.next

        node = Node(key, value)
        node.next = self.slots[h]
        self.slots[h] = node


    def get(self,key):

        h = self.hash(key)

        node = self.slots[h]
        while node is not None:
            if node.key == key:
                return node.value

            node = node.next
        return None

    def keys(self):
        keys_list = []
        for i in range(self.size):
            node = self.slots[i]
            while node is not None:
                keys_list.append(node.key)
                node = node.next
        return keys_list

    def __setitem__(self, key, value):
        self.set(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        return False if self.get(key) is None else True


if __name__ == "__main__":

    file = open("input.txt")
    dct = Dict()
    for line in file:
        if line.strip() == "":
            break
        eng, latin = line.strip().split(" - ")
        latins = latin.split(", ")
        for latin in latins:
            if latin in dct:
                dct[latin].append(eng)
            else:
                dct[latin] = [eng]

    latins = sorted(dct.keys())
    print(len(latins))

    for latin in latins:
        print(latin, end=" - ")
        print(*dct[latin], sep=", ")

    file.close()


