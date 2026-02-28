import sys

def solve():
    # Швидке читання вхідних даних
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])  # кількість корів
    m = int(input_data[1])  # кількість інтервалів

    intervals = []
    idx = 2
    for _ in range(m):
        a = int(input_data[idx])
        b = int(input_data[idx+1])
        intervals.append((a, b))
        idx += 2

    # 1. Попередньо сортуємо інтервали
    intervals.sort()

    def can_place(d):
        count = 1  # перша корова
        curr_pos = intervals[0][0]
        interval_idx = 0

        for _ in range(n - 1):
            target = curr_pos + d

            # Шукаємо інтервал, який може вмістити наступну корову
            while interval_idx < m and intervals[interval_idx][1] < target:
                interval_idx += 1

            if interval_idx == m:
                return False

            # Ставимо корову або на початок інтервалу, або на target
            curr_pos = max(intervals[interval_idx][0], target)
            count += 1

        return count >= n

    # 2. Бінарний пошук за відповіддю
    low = 1
    high = 10**18 # або (intervals[-1][1] - intervals[0][0]) // (n - 1)
    ans = 1

    while low <= high:
        mid = (low + high) // 2
        if can_place(mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    print(ans)

if __name__ == "__main__":
    solve()
