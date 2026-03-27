
def convert(number: str, from_base: int, to_base: int) -> str:

    decimal = 0
    for d in number:
        decimal = from_base * decimal + int(d,from_base)

    # print(decimal)
    if decimal == 0:
        return 0
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

    with open("input.txt") as f:
        from_base, to_base = map(int,f.readline().split())
        n = f.readline().strip()
        print(convert(n,from_base, to_base))