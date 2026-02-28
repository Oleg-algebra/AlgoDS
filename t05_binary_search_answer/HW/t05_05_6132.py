import sys

def solve():
    # Читання вхідних даних
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    k = int(input_data[0]) # кількість пасажирів
    n = int(input_data[1]) # кількість зупинок (рейсів)
    weights = [int(x) for x in input_data[2:]]

    if not weights:
        return

    def can_transport(limit):
        trips = 1
        current_load = 0

        for w in weights:
            if current_load + w <= limit:
                current_load += w
            else:
                trips += 1
                current_load = w
                # Якщо один пасажир важчий за ліміт, цей ліміт неможливий
                if trips > n:
                    return False
        return trips <= n

    # Бінарний пошук
    low = max(weights) # Автобус має підняти найважчого
    high = sum(weights) # Максимум — всі пасажири разом
    ans = high

    while low <= high:
        mid = (low + high) // 2
        if can_transport(mid):
            ans = mid
            high = mid - 1 # Шукаємо меншу вантажопідйомність
        else:
            low = mid + 1 # Треба збільшити ліміт

    print(ans)

if __name__ == "__main__":
    solve()
