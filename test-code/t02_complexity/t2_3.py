def f(n):
    k = 0                   #   2
    i = n - 1               #   4
    while i != 0:           #   3*log(n)
        k += 1.0 / i        #   6*log(n)
        i = i // 2          #   4*log(n)
    return k                #   1

# --> f(n) = O(log(n))


# n - 1 = 2^m -> m = log(n - 1)
#   1 / 2^m + 1 / 2^m / 2 + 1 / 2^m / 2^2 + ... + 1 / 2^m / 2^m =
# = 2^{-m} sum_{j=0}^{m} 2^j = 2^{-m} (2^{m+1} - 1) =
# = 2 - 2^{-m} = 2 - 1 / (n - 1)