def binary_left(array,x):
    left = 0
    right = len(array)

    while left < right:
        mid = left + (right - left) // 2
        print(f'left: {left}, right: {right}, mid: {mid}')
        # mid = (left + right) // 2

        if array[mid] < x:
            left = mid + 1
        else:
            right = mid

    return left

if __name__ == "__main__":
    array = [1,2,3,4,4,4,4,5,5,5,5,6,6,7,7,8,10]#
    x = 0
    print(binary_left(array, x))