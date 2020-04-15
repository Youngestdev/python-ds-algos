def intersect_sorted_array(arr1, arr2):
    i = 0
    j = 0
    intersection = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            if i == 0 or arr1[i] != arr1[i - 1]:
                intersection.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    return intersection
