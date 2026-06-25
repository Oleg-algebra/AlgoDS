"""
Для монотонної на відрізку [a, b] функції f розв'яжіть рівняння
                     f(x) = c
"""


def argument(f,m,l,r,eps,c):
    return r - l > eps

def value(f,m,l,r,eps,c):
    return abs(f(m) - c) > eps

def neighbours(f,m,l,r,eps,c):
    return m != l and m != r


condition = argument

def solve(f, c, a, b):
    """ Для неспадної на відрізку [a, b] функції f розв'язує рівняння
                     f(x) = c

    :param f: Монотонна функція
    :param c: Шукане значення
    :param a: Ліва межа проміжку на якому здійснюється пошук
    :param b: Права межа проміжку на якому здійснюється пошук
    :return: Розв'язок рівняння
    """
    eps = 1e-15

    left = a
    right = b

    count = 0
    m = (left + right) / 2.0
    while condition(f,m,left,right,eps,c):
        count += 1
        if f(m) < c:
            left = m
        else:
            right = m

        m = (left + right) / 2.0

    print(f"count: {count}")
    return m


def solve_decreasing(f, c, a, b):
    """ Для незростаючої на відрізку [a, b] функції f розв'язує рівняння
                     f(x) = c

    :param f: Монотонна функція
    :param c: Шукане значення
    :param a: Ліва межа проміжку на якому здійснюється пошук
    :param b: Права межа проміжку на якому здійснюється пошук
    :return: Розв'язок рівняння
    """
    # f1 = lambda x: f(x) * (-1)
    # return solve(f1,-c,a,b)

    eps = 1e-15

    left = a
    right = b

    count = 0
    m = (left + right) / 2.0
    while condition(f, m, left, right, eps, c):
        count += 1
        if f(m) > c:
            left = m
        else:
            right = m

        m = (left + right) / 2.0

    print(f"count: {count}")
    return m