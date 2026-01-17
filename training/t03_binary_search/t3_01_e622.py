def int_to_binary(n):
    return bin(n)[2:]


# n1 = 5
# n2 = 6
#
# print(n1, n2)
# print(bin(n1)[2:], bin(n2)[2:])
# shift = 1
# print(f"{n1} >> {shift} = " ,int_to_binary(n1 >> shift))
# print(f"{n1} << {shift} = ",int_to_binary(n1 << shift))
# print(f"{n1} & {n2} = ",int_to_binary(n1 & n2))
# print(f"{n1} | {n2} = ",int_to_binary(n1 | n2))
# print(f"{n1} ^ {n2} = ",int_to_binary(n1 ^ n2))
# print(~5)

def solve(n):

    count = 0
    while n > 0:
        count += n & 1
        n = n >> 1

    return count

if __name__ == '__main__':
    n = int(input())
    print(solve(n))

