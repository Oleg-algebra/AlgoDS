"""
Реалізуйте алгоритм пошуку номеру найпершого входження до заданого масиву, заданого числа x.
Якщо заданий елемент відсутній у списку - поверніть номер першого елементу, що більший за число x:
                            array[i] >= x
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
