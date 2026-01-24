
import re
import math
import sys

EMPTY = None


def is_prime(n: int):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


class Set:

    M = 31

    def __init__(self, size=11):
        self._size = size
        self._count = 0
        self._words: list[EMPTY | str] = [EMPTY for _ in range(size)]

    def _rehash(self):
        self._size = self._size * 2 + 1
        while not is_prime(self._size):
            self._size += 2

        _words = self._words
        self.__init__(self._size)
        for i in range(len(_words)):
            if _words[i] is not EMPTY:
                self.add(_words[i])

    # H(s) = C0 * M^n + C1 * M^{n-1} + ... + C{n-1} * M + C{n}
    # (((...) * M + C{n-2}) * M + C{n-1}) * M + C{n}
    # S = C0 C1 C2
    # C0 M^2 + C1 M + C2 = ((C0) * M + C1) * M + C2
    def hash(self, s):
        h = 0
        for i in range(len(s)):
            h = (h * self.M + ord(s[i])) % self._size
        return h

    def add(self, word: str):
        if self._size * 0.7 < self._count:
            self._rehash()

        i = self.hash(word)
        while self._words[i] is not EMPTY:
            if self._words[i] == word:
                return
            i = (i + 1) % self._size

        self._count += 1
        self._words[i] = word

    def get(self, word: str):
        i = self.hash(word)
        while self._words[i] is not EMPTY:
            if self._words[i] == word:
                return self._words[i]
            i = (i + 1) % self._size

    def keys(self):
        res = []
        for i in range(self._size):
            if self._words[i] is not EMPTY:
                res.append(self._words[i])
        return res


    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        return False if self.get(key) is None else True

    def __iter__(self):
        res = []
        for i in range(self._size):
            if self._words[i] is not EMPTY:
                res.append(self._words[i])
        return iter(res)

if __name__ == '__main__':
    f = open("input.txt")
    dct = Set()



    # lines = f.readlines()
    for line in sys.stdin:
        words = re.findall(r'[a-zA-Z]+', line)
        for word in words:
            word = word.lower()
            if word not in dct:
                dct.add(word)

    words_sorted = sorted(dct.keys())
    for word in words_sorted:
        print(word)
    f.close()
