def fastLIS(arr):
    if arr == sorted(arr):
        return len(arr)

    n = len(arr) - 1
    arr.insert(0, float('-inf'))

    def LIFirst(v):
        _best = 0
        for k in range(v + 1, n):
            if arr[k] > arr[v]:
                _best = max(_best, LIFirst(k))
        return 1 + _best

    for i in range(n, -1, -1):
        LIFirst(i)
        for j in range(i + 1, n):
            if arr[j] > arr[i] and (1 + LIFirst(j) > LIFirst(i)):
                LIFirst(i) + LIFirst(j)
    return LIFirst(0)


def longestIncreasingSubsequence(arr):
    result = [1] + [0] * (len(arr) - 1)

    for i in range(1, len(arr)):
        if arr[i - 1] < arr[i]:
            result[i] = result[i - 1] + 1
        else:
            result[i] = 1
    print(arr, result)
    return max(result)


def longestIncreasingSubsequence2(arr):
    result = [1] + [0] * (len(arr) - 1)
    # maxSum = 1
    n = len(arr)
    for i in range(1, n):
        maxSum = 1
        for j in range(1, i):
            if arr[j] < arr[i] and result[j] + 1 > maxSum:
                maxSum = result[j] + 1
        result[i] = maxSum
    maxSum = 0

    for k in range(n):
        if result[k] > maxSum:
            maxSum = result[k]
    print(result)
    return maxSum


print(longestIncreasingSubsequence2([1, -1, 2, 3, 8, 9, 0, 12, 13, 14, 15]))
print(longestIncreasingSubsequence([-2, -1]))
print(longestIncreasingSubsequence([10, 9, 2, 5, 3, 7, 101, 18]))
print(longestIncreasingSubsequence([3, 2, 1]))
