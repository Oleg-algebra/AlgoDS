import math
import sys


input = sys.stdin.readline
EMPTY = "EMPTY"

def is_prime(n):

    for i in range(2,int(math.sqrt(n)+1)):
        if n % i == 0:
            return False

    return True


class Dict:

    M = 31

    def __init__(self,size: int = 11):
        self.size = size
        self.count = 0
        self._keys: list[EMPTY | str] = [EMPTY for _ in range(size)]
        self._values: list[EMPTY | list[str]] = [EMPTY for _ in range(size)]

    def hash(self,key):

        h = 0
        for s in key:
            h = (h * self.M + ord(s)) % self.size

        return h


    def rehash(self):
        self.size = self.size * 2 + 1
        while not is_prime(self.size):
            self.size += 2

        _keys = self._keys
        _values = self._values

        self.__init__(self.size)

        for i in range(len(_keys)):
            if _keys[i] is not EMPTY:
                self.set(_keys[i],_values[i])

    def set(self,key,value):

        if self.count > self.size * 0.7:
            self.rehash()

        h = self.hash(key)
        while self._keys[h] is not EMPTY:

            if self._keys[h] == key:
                self._values[h] = value

            h = (h + 1) % self.size

        self._keys[h] = key
        self._values[h] = value
        self.count += 1

    def get(self,key):

        h = self.hash(key)

        while self._keys[h] is not EMPTY:
            if self._keys[h] == key:
                return self._values[h]

            h = (h + 1) % self.size

    def keys(self):
        keys_list = []
        for i in range(self.size):
            if self._keys[i] is not EMPTY:
                keys_list.append(self._keys[i])

        return keys_list

    def __setitem__(self, key, value):
        self.set(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        return False if self.get(key) is None else True


if __name__ == "__main__":

    f = open("input.txt")
    dct = Dict()
    for line in f:
        eng,latin = line.strip().split(" - ")
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
        print(*dct[latin],sep=", ")

    f.close()


