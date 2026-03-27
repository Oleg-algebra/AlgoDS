# base 2:   1101 --> 1 * 2^0 + 0 * 2^1 + 1 * 2^2 + 1 * 2^3 = 13
# base 3:   1101 --> 1 * 3^0 + 0 * 3^2 + 1 * 3^3 + 1 * 3^4 = 109

# base 10:   1101 --> 1 * 10^0 + 0 * 10^2 + 1 * 10^3 + 1 * 10^4 = 1101

# base 16:  11 --> 1 * 16^0 + 1 * 16^1 = 17
# base 16:  1F --> 15 * 16^0 + 1 * 16^1 = 31

# base b: (a0a1a2a3...an)_b --> a0 * b^0 + a1 * b^2 + a3 * b^3 + ... + an * b^n

# base 2: 0,1
# base 3: 0,1,2
# base 10: 0,...,9
# base 16: 0,...,9,A,B,C,D,E,F  -- A --> 10, B --> 11, C --> 12, ... , F --> 15

# convert from base 2 to base 10:
# 1 * 2^0 + 0 * 2^1 + 1 * 2^2 + 1 * 2^3 = 1 + 2 * (0 + 1 * 2^1 + 1 * 2^2) =
#       = 1 + 2 * (0 + 2 * (1 + 1 * 2^1)) =
#       = 1 + 2 * (0 + 2 * (1 + 2 * (1))) =
#       = 1 + 2 * (0 + 2 * (1 + 2 * (1 + 2 * 0)))

def convert(number: str, from_base: int, to_base: int) -> str:

    decimal = 0
    for d in number:
        decimal = from_base * decimal + int(d,from_base)

    # print(decimal)

    stack = []
    while decimal > 0:
        rem = decimal % to_base
        decimal //= to_base
        stack.append(rem)

    res = ""
    while stack:
        res += get_char(stack.pop())

    return res

def get_char(n: int):
    if n < 10:
        return str(n)
    else:
        return chr(ord("A") + n - 10)

if __name__ == "__main__":
    n = input()
    print(convert(n,2,16))
