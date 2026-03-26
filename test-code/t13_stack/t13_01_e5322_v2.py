
def convert(number: str, from_base: int, to_base: int) -> str:

    decimal = 0
    for d in number:
        decimal = from_base * decimal + int(d,from_base)

    # print(decimal)

    res = ""
    while decimal > 0:
        rem = decimal % to_base
        decimal //= to_base
        res += get_char(rem)




    return res[::-1]

def get_char(n: int):
    if n < 10:
        return str(n)
    else:
        return chr(ord("A") + n - 10)

if __name__ == "__main__":
    n = input()
    print(convert(n,2,16))
