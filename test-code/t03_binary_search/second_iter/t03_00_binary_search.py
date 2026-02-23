from time import time
import numpy as np
import matplotlib.pyplot as plt


def binary_search(arr,x):

    left = 0
    right = len(arr) - 1

    while left < right:
        m = left + (right - left) // 2
        # print(f'left: {left} , right: {right}, mid: {m}')
        if arr[m] < x:
            left = m + 1

        else:
            right = m

    return arr[left],left

if __name__ == "__main__":


    # arr = [1,2,3,4,4,4,4,5,6,6,6,7,8]
    # x = 4
    # print(binary_search(arr, x))

    exuction_time = []
    n = 10000*2
    x = 10
    for i in range(10,n+1):
        arr = np.random.randint(0,100,i)
        x = np.random.choice(arr,1)
        arr.sort()

        start = time()
        binary_search(arr,x)
        end = time()
        exuction_time.append(end - start)

    plt.plot(exuction_time)
    plt.show()




