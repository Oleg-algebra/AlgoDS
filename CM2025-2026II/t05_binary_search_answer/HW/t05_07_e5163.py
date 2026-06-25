import sys
import math

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    a = [int(x) for x in input_data[1:n+1]]
    k = int(input_data[n+1])

    # Спеціальний випадок: фен сушить так само, як повітря
    if k == 1:
        print(max(a))
        return

    def can_dry(time):
        feyn_time_needed = 0
        bonus_speed = k - 1
        for humidity in a:
            if humidity > time:
                # Скільки додаткових одиниць треба висушити феном
                extra = humidity - time
                # Скільки хвилин фен має працювати над цією річчю
                # math.ceil(extra / bonus_speed)
                feyn_time_needed += (extra + bonus_speed - 1) // bonus_speed

        return feyn_time_needed <= time

    low = 0
    high = max(a)
    ans = high

    while low <= high:
        mid = (low + high) // 2
        if mid == 0: # Уникнення ділення на 0 та перевірка початкового стану
            if max(a) == 0:
                ans = 0
                break
            low = 1
            continue

        if can_dry(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    print(ans)

if __name__ == "__main__":
    solve()
