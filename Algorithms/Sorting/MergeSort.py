def mergesort(seq):
    mid = len(seq) // 2
    lft, rgt = seq[:mid], seq[mid:]
    if len(lft) > 1: lft = mergesort(lft)
    if len(rgt) > 1: rgt = mergesort(rgt)
    res = []
    while lft and rgt:
        if lft[-1] >= rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    return (lft or rgt) + res


def merge(left, right):
    result = []
    l = r = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    result.extend(left[l:])
    result.extend(right[r:])

    return result


def MergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = MergeSort(arr[0:mid])
    right = MergeSort(arr[mid:])

    return merge(left, right)


print(MergeSort([1, 3, 2, 5, 4, 6]))
