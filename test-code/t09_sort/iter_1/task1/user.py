"""
Реалізуйте алгоритм сортування злиттям.
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


    if len(array) > 1:
        # print(f'Sorting: {array}')
        mid = len(array) // 2
        left_part = array[:mid]
        right_part = array[mid:]

        # print(f"Splitting: {left_part} {right_part}")
        sort(left_part)
        sort(right_part)

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

        # print(f"Merged: {array}")



if __name__ == "__main__":
    array = [3,7,4,0,-1,30,25,38,-9]
    print(array)
    sort(array)
    print(array)
