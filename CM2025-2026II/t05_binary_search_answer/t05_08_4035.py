
import sys

input = sys.stdin.readline

def condition(dist,n,k,coordinate):

    count = 1
    last_position = coordinate[0]
    for i in range(1,n):
        if (coordinate[i] - last_position) >= dist:
            count += 1
            last_position = coordinate[i]

        if count == k:
            return True

    return False


def solve(n,k,coordinate):

    low = 0
    high = coordinate[-1] - coordinate[0]
    ans = 0

    while low <= high:
        dist = low + (high - low) // 2
        if condition(dist,n,k,coordinate):
            ans = dist
            low = dist + 1
        else:
            high = dist - 1

    return ans

if __name__ == "__main__":
    n,k = list(map(int,input().split()))
    coordinate = list(map(int,input().split()))
    print(solve(n,k,coordinate))