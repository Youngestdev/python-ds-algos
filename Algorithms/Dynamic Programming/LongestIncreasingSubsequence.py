def fastLIS(arr):
    arr.insert(0, float('-inf'))
    n = len(arr)
    dp = [[0 for i in range(n+1)] for j in range(n+1)]

    for j in range(n-1, 0, -1):
        for k in range(0, j):
            keep = 1 + dp[j][j+1]
            skip = dp[k][j+1]
            if arr[k] >= arr[j]:
                dp[k][j] = skip
            else:
                dp[k][j] = max(keep, skip)
    return dp[0][1]


def fastLIS2(arr):
    arr.insert(0, float('-inf'))
    n = len(arr)
    dp = [0 for _ in range(n)]
    for i in range(n-1, -1, -1):
        dp[i] = 1
        for j in range(i+1, n):
            if arr[j] >= arr[i] and 1 + dp[j] > dp[i]:
                dp[i] = 1 + dp[j]
    return dp[0] - 1


print(fastLIS([10,9,2,5,3,7,101,18]))