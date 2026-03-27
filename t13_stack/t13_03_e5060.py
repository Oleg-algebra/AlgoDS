# Postfix
#  3 + 2 * 3  --> 3 2 3 * + --> 9
#  (3 + 2) * 3 --> 3 2 + 3 * --> 15

# Prefix
#  3 + 2 * 3 --> + 3 * 2 3 --> 9
#  (3 + 2) * 3 --> * + 3 2 3 --> 15

# add(3, multiply(2,3))
OPERATORS = "+-*/"

def evaluate(expr: str) -> int:
    tokens = expr.split()
    stack = []
    for token in tokens:
        if token in OPERATORS:

            b = stack.pop()
            a = stack.pop()

            if token == "+":
                stack.append( a + b )
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            else:
                stack.append(a // b)
        else:
            stack.append(int(token))

    return stack.pop()

if __name__ == "__main__":
    expr = input()
    print(evaluate(expr))