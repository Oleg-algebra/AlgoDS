"""
Для монотонної на відрізку [a, b] функції f розв'яжіть рівняння
                     f(x) = c
"""

def argument(f,m,l,r,eps):
    return r - l > eps

def value(f,m,l,r,eps):
    return abs(f(r)-f(l)) > eps

def neighbours(f,m,l,r,eps):
    return l != m and m != r

condition = neighbours

def solve(f, c, a, b):
    """ Для неспадної на відрізку [a, b] функції f розв'язує рівняння
                     f(x) = c

    :param f: Монотонна функція
    :param c: Шукане значення
    :param a: Ліва межа проміжку на якому здійснюється пошук
    :param b: Права межа проміжку на якому здійснюється пошук
    :return: Розв'язок рівняння
    """

    left = a
    right = b

    eps = 1e-11
    m = (left + right) / 2.0
    count = 0
    while condition(f,m,left,right,eps):
        count+=1
        # print(f'left: {left}, right: {right}')
        if f(m) < c:
            left = m
        else:
            right = m

        m = (left + right) / 2.0

    print(count)
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
    f1 = lambda x : (-1)*f(x)
    return solve(f1, -c, a, b)
