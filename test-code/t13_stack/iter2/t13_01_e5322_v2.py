
def convert(number: str, from_base: int, to_base: int) -> str:

    decimal = 0
    for d in number:
        decimal  = decimal * from_base + int(d,from_base)

    # print(decimal)

    res = ""
    while decimal > 0:
        res += get_char(
            decimal % to_base
        )
        decimal //= to_base

    # print(stack)




    return res[::-1]

def get_char(n: int):
    if n < 10:
        return str(n)
    else:
        return chr(ord("A") + n - 10)

if __name__ == "__main__":
    n = input()
    print(convert(n,2,16))