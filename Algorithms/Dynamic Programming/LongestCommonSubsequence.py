def lcslength(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    b = c = [[0 for i in range(m+1)] for i in range(n+1)]
    for i in range(0, m):
        c[i][0] = 0
    # print(c)
    for i in range(0, n):
        c[0][i] = 0
    # print(c)
    for i in range(1, m):
        for j in range(1, n):
            if arr1[i] == arr2[j]:
                c[i][j] += c[i-1][j-1] + 1
                b[i][j] = 1
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] += c[i-1][j]
                b[i][j] = 2
            else:
                c[i][j] += c[i][j-1]
                b[i][j] = 3
    return c and b

print(lcslength("ABCBDAB", "BDCABA"))