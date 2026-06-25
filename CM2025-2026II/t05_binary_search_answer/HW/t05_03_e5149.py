import sys

def solve():
    # Читання вхідних даних
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0]) # Кількість стійл
    k = int(input_data[1]) # Кількість корів
    coords = sorted(int(x) for x in input_data[2:])

    def can_place(dist):
        count = 1  # Першу корову ставимо в перше стійло
        last_pos = coords[0]

        for i in range(1, n):
            if coords[i] - last_pos >= dist:
                count += 1
                last_pos = coords[i]
                if count >= k:
                    return True
        return False

    # Бінарний пошук за відповіддю
    low = 0
    high = coords[-1] - coords[0]
    ans = 0

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
