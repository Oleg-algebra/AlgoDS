def func(m,w,h):
    return (m//w) * (m // h)

def binary_search(w,h,n):
    left = 1
    right = max(w,h)*n


    while left < right:
        m = left + (right - left) // 2
        count = (m//w) * (m // h)
        if count < n:
            left = m + 1
        else:
            right = m

    return left



if __name__ == "__main__":
    w,h,n = map(int,input().split())
    print(binary_search(w,h,n))