"""
Longest Increasing Subsequence backtracking solutions..

Doesn't work for some edge cases but e go be!

"""
def longestIncreasingSubsequence(arr):
    n = len(arr) - 1
    arr[0] = float('-inf')
    def LIFirst(i):
        _best = 0
        for j in range(i+1, n):
            if arr[j] > arr[i]:
                _best = max(_best, LIFirst(j))
        return 1 + _best
    return LIFirst(0) - 1

def LIS(arr):
    n = len(arr) - 1
    best = 0
    def LIFirst(i):
        _best = 0
        for j in range(i+1, n):
            if arr[j] > arr[i]:
                _best = max(_best, LIFirst(j))
        return 1 + _best
    for i in range(0, n):
        best = max(best, LIFirst(i))
    return best

print(LIS([10, 9, 2, 5, 3, 7, 101, 18]))
print(longestIncreasingSubsequence([-2, -1]))