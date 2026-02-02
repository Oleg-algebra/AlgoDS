import sys

input = sys.stdin.readline

def count_ones(n):
    res = 0
    while n != 0:
        is_one = n & 1
        res += is_one
        n = n >> 1

    return res


if __name__ == "__main__":
    n = int(input())
    print(count_ones(n))

# 101 & 1 --> 1
#  10 & 1 --> 0
#   1 & 1 --> 1