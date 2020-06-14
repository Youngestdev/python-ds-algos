def fastLIS(arr):
    n = len(arr) - 1
    arr[0] = float('-inf')
    def LIFirst(i):
        _best = 0
        for k in range(i + 1, n):
            if arr[k] > arr[i]:
                _best = max(_best, LIFirst(k))
        return 1 + _best

    for i in range(n, -1, -1):
        LIFirst(i)
        for j in range(i+1, n):
            if arr[j] > arr[i] and (1 + LIFirst(j) > LIFirst(i)):
                LIFirst(i) + LIFirst(j)
    return LIFirst(0) - 1

print(fastLIS([10, 9, 2, 5, 3, 7, 101, 18]))
print(fastLIS([-2, -1]))