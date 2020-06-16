def subsetSum(array, target):
    # if target == 0:
    #     return True
    #
    # store = [[False for i in range(target+1)] for j in range(len(array)+1)]
    # n = len(array) - 1
    # store[n][0] = True
    # for i in range(1, target):
    #     store[n][i] = False
    #
    # for i in range(n - 1, -1, -1):
    #     store[i][0] = True
    #     for t in range(0, array[i] - 1):
    #         # store[i][t] = store[i + 1][t]
    #         store[i][t] = subsetSum([i+1], t)
    #     for t in range(array[i], target):
    #         store[i][t] = subsetSum([i+1], t) + subsetSum([i+1], t-array[i])
    # # print(store[0])
    # return store[0][target-1]

    n = len(array)
    store = ([[False for i in range(target + 1)] for i in range(n + 1)])

    for i in range(n + 1):
        store[i][0] = True

    for i in range(1, target + 1):
        store[0][i] = False

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if j < array[i - 1]:
                store[i][j] = store[i - 1][j]
            if j >= array[i - 1]:
                store[i][j] = (store[i - 1][j] or store[i - 1][j - array[i - 1]])

    return store[n][target]


print(subsetSum([9, 1, 100, 0], 10))
print(subsetSum([1, 2], 3))
