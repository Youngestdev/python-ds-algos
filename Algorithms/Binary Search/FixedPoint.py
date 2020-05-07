def FixedPoint(array):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2

        if array[mid] < mid:
            low = mid + 1

        elif array[mid] > mid:
            high = mid-1
        else:
            return array[mid]
    return None

print(FixedPoint([-10, -5, 0, 3, 7]))