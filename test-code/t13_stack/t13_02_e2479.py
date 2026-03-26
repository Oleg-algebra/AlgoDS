BRACKETS = {"(" : ")", "[" : "]"}


def solve(sequence:str) -> bool:

    stack = []
    for bracket in sequence:
        print(stack)
        if bracket in BRACKETS:
            stack.append(bracket)
        elif len(stack) == 0 or BRACKETS[stack.pop()] != bracket:
                return False



    return len(stack) == 0


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())

        for _ in range(n):
            sequence = f.readline()

            if solve(sequence.strip()):
                print("Yes")
            else:
                print("No")