import sys

input = sys.stdin.readline

def binary_search_right(array,x):

    left = 0
    right = len(array)

    while left <= right:
        mid  = left + (right - left) // 2
        print(f'left: {left}, right: {right}, mid: {mid}')
        # mid = (left + right) // 2

        if array[mid] <= x:
            left = mid + 1
        else:
            right = mid

    return left - 1

if __name__ == "__main__":
    n,m = list(map(int,input().split()))
    array = list(map(int,input().split()))
    request_x = []
    for i in range(m):
        x = int(input())
        request_x.append(x)

    for x in request_x:
        res = binary_search_right(array,x)
        if array[res] == x:
            print(res + 1)
        else:
            print(0)
    # array = [2,3,3,3,5,6,7,8,8,8,9,9]
    # print(len(array))
    # print(binary_search_right(array,3))
    # print(binary_search_right(array, 4))
    # print(binary_search_right(array, 10))
    # print(binary_search_right(array, 0))
