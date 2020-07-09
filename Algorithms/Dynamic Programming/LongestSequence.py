"""
    Given an array of numbers in any order - sorted or not, return the length of the longest sequence..
    This is a variant to a stock question - longest price rise and drop.
    Original code by Adesanya Tomiwa [https://github.com/Tomesyy]
    What this code does is compute the longest sequence in increasing and decreasing order then returns the max length
"""


def longestSequence(array):
    dp = [[1 for _ in range(len(array))] for _ in range(2)]
    for i in range(len(array)):
        for j in range(i - 1, len(array)):
            if array[j] < array[i]:
                dp[0][i] = max(dp[0][j] + 1, dp[0][i])
            if array[j] > array[i]:
                dp[1][i] = max(dp[1][j] + 1, dp[1][i])

    # There should be a beautiful way to do this but ko kan aye.
    return max(max(dp[0]), max(dp[1]))


if __name__ == '__main__':
    print(longestSequence([1, 2, 3, 0, 6, 5, 4, 3, 2, 1]))
    print(longestSequence([1, 2, 2, 1]))
    print(longestSequence([1, 2, 4, 0, -1, 19, 4, 3, 2, 1]))
    print(longestSequence([1, 2, 3, 4, 2, 1]))
    print(longestSequence([1, -1]))