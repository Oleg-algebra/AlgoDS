def f(n):
    k = 0                   # O(1)
    i = n - 1               # O(1)
    while i != 0:           # O(logn)
        k += 1.0 / i        # O(logn)
        i = i // 2          # O(logn)
    return k                # O(1)


# T(n) = O(logn)

# n - 1 --> 2^m
# sum = 1/2^m + 1/2^{m-1} + .... + 1/2^{m-m} =
#   = 2^{-m}*(1+ 2 +4 + ... + 2^m) = 2^{-m} (2^{m+1} - 1)