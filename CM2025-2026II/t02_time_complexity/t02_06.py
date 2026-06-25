def sum_arithm(n):
    return n*(n+1)/2    #O(1)

def sum_geom(a,n):
    if a == 1:
        return n + 1        # O(1)
    else:
        return (a**n - 1)/(a-1)     # O(log n)


def sum_geom2(a):
    return 1/(1-a)          # O(1)