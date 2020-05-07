def FindBitonicPeak(array):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2

        mid_left = array[mid - 1] if mid - 1 > 0 else float("-inf")
        mid_right = array[mid + 1] if mid + 1 > 0 else float("inf")

        if mid_left < array[mid] and mid_right > array[mid]:
            low = mid + 1
        elif mid_left > array[mid] and mid_right < array[mid]:
            high = mid - 1
        elif mid_left < array[mid] and mid_right < array[mid]:
            return array[mid]
    return None
