"""
    Return the minimum number of bills to make "k" dream dollars
    This should be under backtracking tbh.
"""


def minNoOfBills(change):
    arr = [1, 4, 13, 28, 52, 91, 365]
    res = []

    def backtrack(values, current):
        if sum(current) == change:
            if current not in res:
                res.append(current[:])
                return
            return
        else:
            for i in range(len(values)):
                backtrack(values[:i] + values[i+1:], current + values[i+1:])

    backtrack(arr, [])
    return res or -1

def minNoOfBills2(amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    denominations = [1, 4, 13, 28, 52, 91, 365]

    for currency in denominations:
        for i in range(currency, amount+1):
            dp[i] = min(dp[i], dp[i-currency] + 1)

    print(dp)
    return dp[amount] if dp[amount] != float('inf') else -1

print(minNoOfBills2(121))