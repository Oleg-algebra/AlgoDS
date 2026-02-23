import sys

input = sys.stdin.readline

def binary_right_most(array,x):
    left = 0
    right = len(array)

    while left < right:
        mid = left + (right - left) // 2
        if array[mid] <= x:
            left = mid + 1
        else:
            right = mid

    # left = left - 1
    if array[left - 1] == x:
        return left
    else:
        return 0


if __name__ == "__main__":
    n,m = map(int,input().split())
    array = list(map(int,input().split()))
    xs = []
    for i in range(m):
        xs.append(int(input()))

    for x in xs:
        print(binary_right_most(array,x))