"""
Реалізуйте інтерфейс асоціативного масиву, ключами якого є цілі числа,
а значеннями – рядки.
Реалізацію здійсніть як хеш-таблицю з відкритою адресацією
"""
import math

size: int = 11
keys: list[int]
values: list[str]
count: int

EMPTY = "EMPTY"
DELETED = "DELETED"

threshold = 0.7

def is_prime(n: int):
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def reshash():

    global size

    size = size * 2 + 1
    while not is_prime(size):
        size += 2

    _keys = keys
    _values = values

    init()

    for i in range(len(_keys)):
        if _keys[i] not in (DELETED,EMPTY):
            set(_keys[i],_values[i])



def hash(key):
    return key % size

def init():
    """ Викликається 1 раз на початку виконання програми. """
    global keys, values, count
    count = 0
    keys = [EMPTY for _ in range(size)]
    values = [EMPTY for _ in range(size)]


def set(key: int, value: str) -> None:
    """ Встановлює значення value для ключа key.
    Якщо такий ключ відсутній у структурі - додає пару, інакше змінює значення для цього ключа.
    :param key: Ключ
    :param value: Значення
    """
    global count

    if size*threshold < count:
        reshash()

    h = hash(key)
    j = -1
    while keys[h] is not EMPTY:
        if keys[h] == key:
            values[h] = value
            return
        if keys[h] == DELETED:
            j = h
        h = (h+1) % size

    if j == -1:
        j = h
        count += 1

    keys[j] = key
    values[j] = value





def get(key: int):
    """ За ключем key повертає значення зі структури.
    :param key: Ключ
    :return: Значення, що відповідає заданому ключу або None, якщо ключ відсутній у структурі.
    """

    h = hash(key)
    while keys[h] is not EMPTY:
        if keys[h] == key:
            return values[h]

        h = (h + 1) % size
    return None


def delete(key: int) -> None:
    """ Видаляє пару ключ-значення за заданим ключем.
    Якщо ключ у структурі відсутній - нічого не робить.
    :param key: Ключ
    """

    h = hash(key)
    while keys[h] is not EMPTY:
        if keys[h] == key:
            keys[h] = DELETED
            values[h] = DELETED
            return

        h = (h + 1) % size


if __name__ == "__main__":
    init()
    print(keys)
    print(values)

    set(5, "5")
    # set(17, "17")
    set(27,"27")
    set(6,"6")

    set(1, "1")
    set(12,"12")

    print(keys)

    print(get(5))
    print(get(27))
    print(get(17))

    delete(27)
    print(keys)
    delete(7)
    print(keys)
    print(get(6))

    set(49,"49")
    set(27,"27")
    print(keys)
    delete(49)
    print(keys)
    set(17,"+17")
    print(values)

    for i in range(18,32):
        set(i,str(i))

    print(values)