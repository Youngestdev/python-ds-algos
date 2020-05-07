def FindFirstOccurence(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2

        if array[mid] < target:
            low = mid + 1
        elif array[mid] > target:
            high = mid - 1
        else:
            if mid - 1 == 0:
                return mid
            if array[mid-1] != target:
                return mid
            high = mid - 1

print(FindFirstOccurence([0,17,243,-13,14,14,56], 14))