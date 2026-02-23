def binary_search(arr,x):
    return _binary_search(arr,0,len(arr)-1,x)

def _binary_search(array, left, right, x):
    if left == right:
        return left

    m = left + (right - left) // 2
    if array[m] < x:
        return _binary_search(array,m + 1,right, x)
    else:
        return _binary_search(array,left,m,x)


if __name__ == "__main__":
    arr = [1,2,3,4,4,4,4,5,6,6,6,7,8]
    x = 4
    print(binary_search(arr, x))