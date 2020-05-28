def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        swapped = True
        for j in range(0, n -i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = False
                if swapped:
                    break
    return arr

print(bubblesort([1, 3]))