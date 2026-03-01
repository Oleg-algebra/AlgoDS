
"""
Реалізуйте швидкий алгоритм сортування QuickSort.
"""

N = 1000000  # Кількість елементів масиву.
             # Використовується у головній програмі для генерування масиву з випадкових чисел
             # Для повільних алгоритмів сортування з асимптотикою n**2 рекомендується
             # використовувати значення не більше 10к
             # Для швидких алгоритмів сортування з асимптотикою
             # nlog(n) встановіть значення 1 000 000


def sort(array):
    """ Сортування масиву
    :param array: Вхідний масив даних, що треба відсортувати.
    """
    _quick_sort(array,0, len(array) - 1)

def _quick_sort(array,a,b):

    if a >= b:
        return

    pivot = array[a + (b - a) // 2]
    left = a
    right = b
    # print(array[a:b+1], a,b,f"pivot: {pivot}")

    while True:
        while array[left] < pivot:
            left += 1

        while array[right] > pivot:
            right -= 1

        if left >= right:
            break

        array[left],array[right] = array[right], array[left]
        left += 1
        right -= 1

    # print(array[:right + 1], array[right + 1: b + 1])
    _quick_sort(array,a,right)
    _quick_sort(array,right + 1, b)

if __name__ == "__main__":
    array = [3,7,4,0,-1,30,25,38,-9]
    print(array)
    sort(array)
    print(array)



