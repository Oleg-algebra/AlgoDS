"""
Реалізуйте інтерфейс асоціативного масиву, ключами якого є цілі числа,
а значеннями – рядки.
Реалізацію здійсніть як хеш-таблицю з відкритою адресацією
"""

import math

class Node:
    def __init__(self, key: int, value: str) -> None:
        self.key = key
        self.value = value
        self.next: [None | Node]= None


    def __repr__(self) -> str:
        return f"Node: (key: {self.key}, value: {self.value}, next: {self.next})"

size: int = 1000003
count: int
slots: list[Node]

def is_prime(n: int) -> bool:

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

def rehash():

    global size

    size = size * 2 + 1
    while not is_prime(size):
        size += 2

    _slots = slots
    init()
    for i in range(len(_slots)):
        if _slots[i] is not None:
            set(_slots[i].key, _slots[i].value)

def hash(key: int) -> int:
    return key % size




def init():
    """ Викликається 1 раз на початку виконання програми. """
    global slots, count
    count = 0
    slots = [None for _ in range(size)]

def set(key: int, value: str) -> None:
    """ Встановлює значення value для ключа key.
    Якщо такий ключ відсутній у структурі - додає пару, інакше змінює значення для цього ключа.
    :param key: Ключ
    :param value: Значення
    """
    global count

    if size * 0.7 < count:
        rehash()

    i = hash(key)
    node = slots[i]
    while node is not None:
        if node.key == key:
            node.value = value
            return
        node = node.next

    node = Node(key, value)
    node.next = slots[i]

    slots[i] = node
    count += 1



def get(key: int):
    """ За ключем key повертає значення зі структури.
    :param key: Ключ
    :return: Значення, що відповідає заданому ключу або None, якщо ключ відсутній у структурі.
    """
    i = hash(key)
    node = slots[i]
    while node is not None:
        if node.key == key:
            return node.value
        node = node.next

    return None


def delete(key: int) -> None:
    """ Видаляє пару ключ-значення за заданим ключем.
    Якщо ключ у структурі відсутній - нічого не робить.
    :param key: Ключ
    """
    i = hash(key)
    node = slots[i]
    if node is None:
        return

    if node.key == key:
        slots[i] = node.next
        return

    prev_node = node
    node = node.next
    while node is not None:
        if node.key == key:
            prev_node.next = node.next
            return
        prev_node = node
        node = node.next


if __name__ == "__main__":
    init()
    set(5,"5")
    set(9,"9")
    set(16,"16")
    set(27,"27")

    print(slots)

    print(get(5))
    print(get(9))
    print(get(30))

    delete(16)
    print(get(16))
    set(16,"16")
    print(slots)
    print()
    delete(5)
    print(slots)
    print()
    set(5,"5")
    print(slots)

    delete(5)
    print(slots)