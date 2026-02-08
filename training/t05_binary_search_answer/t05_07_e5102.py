import sys

input = sys.stdin.readline

def binary_search(n,x,y):

    left = 1
    right = n*max(x,y)

    if n == 1:
        return min(x,y)
    first_copy = min(x,y)
    while left < right:
        t = left + (right - left) // 2
        count = (t // x) + (t // y)
        if count < (n - 1):
            left = t + 1
        else:
            right = t

    return left + first_copy

if __name__ == "__main__":
    n,x,y = list(map(int,input().split()))
    print(binary_search(n, x, y))

