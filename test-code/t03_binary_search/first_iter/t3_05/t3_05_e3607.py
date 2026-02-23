import sys
input = sys.stdin.readline

def solve(arr,a,b):
    count = 0
    for i in range(len(arr)):
        if arr[i] <= b and arr[i] >= a:
            count += 1
    return count



if __name__ == '__main__':

    while True:
        line  = input()
        if not line:
            break
        n = int(line)
        arr = [int(a) for a in input().split()]
        a,b = [int(a) for a in input().split()]
        print(solve(arr,a,b))

