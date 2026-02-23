import sys

input = sys.stdin.readline


def can_place(n,m,k,coordinates):
    count = 1
    last_coordinate = coordinates[0]

    for i in range(1,n):
        if (coordinates[i] - last_coordinate) >= m:
            count += 1
            last_coordinate = coordinates[i]
            if count == k:
                return True

    return False

def binary_search(n,k,coordinates):
    left = 0
    right = coordinates[-1] - coordinates[0]
    ans = 0

    while left <= right:
        m = left + (right - left) // 2
        if can_place(n,m, k,coordinates):
            ans = m
            left = m + 1
        else:
            right = m - 1
    return ans




if __name__ == "__main__":
    n,k = list(map(int,input().split()))
    coordinates = list(map(int,input().split()))

    print(binary_search(n,k,coordinates))