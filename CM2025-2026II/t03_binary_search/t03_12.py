
def binary_search(array,x):
    return _binary_search_recursive(array,x,0,len(array) - 1)

def _binary_search_recursive(array,x,left,right):

    if left == right:
        return left

    mid = left + (right - left) // 2

    if array[mid] < x:
        print(f" left: {left}, right: {right}, mid: {mid} ---> right part")
        return _binary_search_recursive(array,x,mid + 1,right)
    else:
        print(f" left: {left}, right: {right}, mid: {mid} ---> left part")
        return _binary_search_recursive(array, x, left, mid)


if __name__ == "__main__":
    array = [1,2,3,4,4,5,6,6,7,7,8] #
    x = 4
    print(binary_search(array, x))