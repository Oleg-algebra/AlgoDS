import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    idx = 0
    R = int(input_data[idx]); idx += 1 # кількість полів
    L = int(input_data[idx]); idx += 1 # максимальна координата (не використовується в бінарному пошуку)
    B = int(input_data[idx]); idx += 1 # бюджет

    x = [int(input_data[i]) for i in range(idx, idx + R)]

    # Будуємо префіксні суми для швидкого знаходження суми на відрізку
    pref = [0] * (R + 1)
    for i in range(R):
        pref[i+1] = pref[i] + x[i]

    def get_sum(l, r):
        """Повертає суму координат на відрізку [l, r] включно"""
        return pref[r+1] - pref[l]

    def check(length):
        """Перевіряє, чи можна зібрати length полів у межах бюджету B"""
        # Використовуємо ковзне вікно довжиною length
        for i in range(R - length + 1):
            j = i + length - 1
            mid_idx = (i + j) // 2
            median = x[mid_idx]

            # Поля зліва від медіани (включаючи саму медіану в розрахунок суми)
            left_count = mid_idx - i
            left_sum = get_sum(i, mid_idx - 1)
            cost_left = left_count * median - left_sum

            # Поля справа від медіани
            right_count = j - mid_idx
            right_sum = get_sum(mid_idx + 1, j)
            cost_right = right_sum - right_count * median

            if cost_left + cost_right <= B:
                return True
        return False

    # Бінарний пошук за кількістю полів
    low = 1
    high = R
    ans = 0

    while low <= high:
        mid = (low + high) // 2
        if check(mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    print(ans)

if __name__ == "__main__":
    solve()
