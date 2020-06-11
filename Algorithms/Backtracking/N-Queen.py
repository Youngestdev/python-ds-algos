def placequeens(arr, r):
    n = len(arr)
    res = []
    if r == n:
        print(arr)
    else:
        for j in range(0, n):
            legal = True
            for i in range(0, r):
                if (arr[i] == j) or (arr[i] == j + r - i) or (arr[i] == j - r + i):
                    legal = False
            if legal:
                arr[r] = j
                res.append(arr)
                placequeens(arr, r+1)
    return len(res)
#     2,5,7,0,4,6,1,3
#                 5,7,1,4,2,8,6,3
print(placequeens([0,0,0,0,0,0,0,0], 0))
print(placequeens([0,0,0,0], 0))
