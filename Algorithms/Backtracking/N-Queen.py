def SolveNQueens(n):
    arr = [0] * (n)
    count = []
    def placequeens(arr, r=0):
        if r == n:
            count.append(arr)
            return
        else:
            for j in range(0, n, 1):
                legal = True
                for i in range(0, r, 1):
                    if (arr[i] == j) or (arr[i] == j + r - i) or (arr[i] == j - r + i):
                        legal = False
                if legal:
                    arr[r] = j
                    placequeens(arr, r+1)
    placequeens(arr, 0)
    return len(count)
