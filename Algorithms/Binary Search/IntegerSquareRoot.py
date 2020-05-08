def IntegerSquareRoot(k):
    low = 0
    high = k

    while low <= high:
        mid = (low + high) // 2
        mid_squared = mid * mid
        if mid_squared <= k:
            low = mid + 1
        else:
            high = mid - 1
    return low - 1