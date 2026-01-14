def f(n):                   #
    i = n - 1               #   O(1)
    while i != 0:           #   3*log(n) = O(log(n)
        j = 0               #   2*log(n) = = O(log(n)
        while j < n:        #   3*(n+1)*log(n) = O(n*log(n)
            j += 1          #   4*n*log(n) = O(n*log(n)
        i = i // 2          #   4*log(n) = = O(log(n)
                            #

# f(n) = O(nlog(n))