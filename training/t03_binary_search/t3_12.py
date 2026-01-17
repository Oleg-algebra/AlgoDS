def binary_search(arr,x):
    return _binary_search(arr,0,len(arr)-1,x)

def _binary_search(arr,low,high,x):
    if low == high:
        return low

    mid = low + (high-low)//2
    if arr[mid] < x:
        return _binary_search(arr,mid+1,high,x)
    else:
        return _binary_search(arr,low,mid,x)


if __name__ == '__main__':
    arr = [1,1,1,1, 2, 3,3,3,3, 4, 5,5,5,5, 6, 7, 8, 9, 10]
    x = int(input())
    print(binary_search(arr, x))