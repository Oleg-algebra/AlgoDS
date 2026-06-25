# a = 5   # 101           ~5 = 11111....1010
# b = 6   # 110
#
# print(a >> 1)   # 10
# print(a << 1)   # 1010
#
#
#
# print(a & b)    # 100
# print(a | b)    # 111
# print(a ^ b)    # 11
# print(~a)       #   ~x = -(x+1)

def count_ones(n):
    count = 0
    one = 1
    for i in range(n.bit_length()):
        if (one << i) & n:
            count += 1


    return count


if __name__ == "__main__":
    n = int(input())
    print(count_ones(n))

# 101 & 001 --> True
# 101 & 010 --> False
# 101 & 100 --> True