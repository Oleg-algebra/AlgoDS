import sys

def solve():
    # Швидке читання вхідних даних
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0]) # Кількість точок
    k = int(input_data[1]) # Кількість відрізків
    # Сортуємо координати, щоб іти по порядку
    coords = sorted(int(x) for x in input_data[2:])

    def can_cover(length):
        count = 0
        last_covered = -float('inf')

        for p in coords:
            # Якщо поточна точка не входить у попередній відрізок
            if p > last_covered:
                count += 1
                # Ставимо новий відрізок, що починається в цій точці
                last_covered = p + length

        return count <= k

    # Бінарний пошук за відповіддю
    low = 0
    high = coords[-1] - coords[0]
    ans = high

    while low <= high:
        mid = (low + high) // 2
        if can_cover(mid):
            ans = mid
            # Пробуємо знайти ще меншу довжину
            high = mid - 1
        else:
            # Довжина замала, треба збільшити
            low = mid + 1

    print(ans)

if __name__ == "__main__":
    solve()
