"""
Проведіть аналіз швидкодії реалізованих алгоритмів сортування
для різних типів та розмірів масивів (не відсортований масив
згенерований випадковим чином, масив відсортований за зростанням,
масив відсортований за спаданням елементів).
"""

N = 5000     # Кількість елементів масиву.
              # Використовується у головній програмі для генерування
              # масиву з випадкових чисел


def bubble_sort(array):
    """ Сортування "Бульбашкою"

    :param array: Масив (список однотипових елементів)
    """
    n = len(array)
    for pass_num in range(n - 1, 0, -1):
        for j in range(pass_num):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def bubble_sort_optimized(array):
    """ Модификований алгоритм сортування "Бульбашкою"

    :param array: Вхідний масив даних, що треба відсортувати.
    """
    n = len(array)
    for j in range(n - 1, 0, -1):
        _sorted = True
        for i in range(j):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                _sorted = False
        if _sorted:
            return


def selection_sort(array):
    """ Сортування вибором

    :param array: Масив (список однотипових елементів)
    :return: None
    """
    n = len(array)
    for i in range(n - 1, 0, -1):
        pos = 0
        for j in range(1, i + 1):
            if array[pos] < array[j]:
                pos = j
        array[pos], array[i] = array[i], array[pos]


def insertion_sort(array):
    """ Сортування вставкою

    :param array: Масив (список однотипових елементів)
    :return: None
    """
    n = len(array)
    for i in range(1, n):
        pos = i
        x = array[pos]
        while pos > 0:
            if array[pos - 1] > x:
                # if array[pos - 1] > array[pos]:
                #     array[pos],array[pos - 1] = array[pos - 1], array[pos]
                array[pos] = array[pos - 1]
            else:
                break

            pos -= 1
        array[pos] = x


def merge_sort(array):
    """ Сортування злиттям

    :param array: Масив (список однотипових елементів)
    :return: None
    """
    if len(array) > 1:
        # print(f'Sorting: {array}')
        mid = len(array) // 2
        left_part = array[:mid]
        right_part = array[mid:]

        # print(f"Splitting: {left_part} {right_part}")
        merge_sort(left_part)
        merge_sort(right_part)

        # print(f"Merging: {left_part} {right_part}")

        i = 0
        j = 0
        k = 0
        while i < len(left_part) and j < len(right_part):
            if left_part[i] < right_part[j]:
                array[k] = left_part[i]
                i += 1
            else:
                array[k] = right_part[j]
                j += 1
            k += 1

        while i < len(left_part):
            array[k] = left_part[i]
            i += 1
            k += 1

        while j < len(right_part):
            array[k] = right_part[j]
            j += 1
            k += 1


def merge_sort_optimized(array):
    """ Сортування масиву
    :param array: Вхідний масив даних, що треба відсортувати.
    """
    _merge_sort_optimized(array, 0, len(array) - 1)


def _merge_sort_optimized(array, a, b):

    if a == b:
        return

    m = a + (b - a) // 2
    _merge_sort_optimized(array, a, m)
    _merge_sort_optimized(array, m + 1, b)

    left = array[a:m+1]

    i = 0
    j = m + 1
    k = a

    while i < len(left) and j <= b:
        if left[i] < array[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = array[j]
            j += 1

        k += 1

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1


def quick_sort(array):
    """ Сортування масиву
    :param array: Вхідний масив даних, що треба відсортувати.
    """
    _quick_sort(array,0, len(array) - 1)

def _quick_sort(array,a,b):
    if a >= b:
        return

    pivot = array[a]
    left = a
    right = b

    # print(array[a: b+1], a,b, f"pivot: {pivot}")
    while True:
        while array[left] < pivot:
            left += 1
        while array[right] > pivot:
            right -= 1

        if left >= right:
            break

        array[left], array[right] = array[right], array[left]

        left += 1
        right -= 1

    # print(array[a:right + 1], array[right + 1: b+1])
    _quick_sort(array,a,right)
    _quick_sort(array,right + 1,b)

