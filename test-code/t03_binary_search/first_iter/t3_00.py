def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = low + (high - low) // 2
        print(f"low = {low}, high = {high}, mid = {mid}")
        a = arr[mid]
        if arr[mid] < x:
            low = mid + 1
        else:
            high = mid

    return low


if __name__ == '__main__':
    arr = [1,1,1,1, 2, 3,3,3,3, 4, 5,5,5,5, 6, 7, 8, 9, 10]
    x = int(input())
    print(binary_search(arr, x))