def ClosestNumber(array, target):
    min_difference = float("inf")
    low = 0
    high = len(array) - 1
    closest_number = None

    if len(array) == 0:
        return None
    if len(array) == 1:
        return array[0]

    while low <= high:
        mid = (low + high) // 2

        if mid + 1 < len(array):
            min_difference_right = abs(array[mid + 1] - target)

        if mid > 0:
            min_difference_left = abs(array[mid - 1] - target)

        if min_difference_left < min_difference:
            min_difference = min_difference_left
            closest_number = array[mid - 1]

        if min_difference_right < min_difference:
            min_difference = min_difference_right
            closest_number = array[mid + 1]

        if array[mid] < target:
            low = mid + 1

        elif array[mid] > target:
            high = mid - 1
        else:
            return array[mid]

    return closest_number
