BRACKETS = {"(" : ")", "[" : "]"}

def check(sequence: str) -> bool:

    stack = []
    for bracket in sequence:
        if bracket in BRACKETS:
            stack.append(bracket)

        elif len(stack) == 0 or BRACKETS[stack.pop()] != bracket:
            return False
        # else:
        #     if len(stack) == 0:
        #         return False
        #     opening_bracket = stack.pop()
        #     closing_bracket = BRACKETS[opening_bracket]
        #     if closing_bracket != bracket:
        #         return False

    return len(stack) == 0

if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())

        for _ in range(n):
            sequence = f.readline().strip()

            if check(sequence):
                print("Yes")
            else:
                print("No")