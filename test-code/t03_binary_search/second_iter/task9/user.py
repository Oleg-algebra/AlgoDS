"""
Знайдіть кількість входжень заданого числа x до впорядкованого за неспаданням масиву цілих чисел array
"""

def bsearch_leftmost(array, x):

    left = 0
    right = len(array)

    while left < right:
        m = left + (right - left) // 2
        # print(f'left: {left} , right: {right}, mid: {m}')
        if array[m] < x:
            left = m + 1

        else:
            right = m

    return left

def binary_right_most(array,x):
    left = 0
    right = len(array)

    while left < right:
        mid = left + (right - left) // 2
        if array[mid] <= x:
            left = mid + 1
        else:
            right = mid

    # left = left - 1
    return left - 1

def counter(array, x):
    """ кількість входжень заданого числа.
    :param array: Масив цілих чисел впорядкований за неспаданням
    :param x:     Шуканий елемент
    :return:      Кількість входжень
    """
    left = bsearch_leftmost(array,x)
    if left < len(array):
        if array[left] != x:
            return 0
    else:
        return 0

    right = binary_right_most(array, x)
    return right - left + 1



