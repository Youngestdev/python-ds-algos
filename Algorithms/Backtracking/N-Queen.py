def SolveNQueens(n):
    arr = [0] * (n)
    count = []

    def placequeens(arr, r=0):
        if r == n:
            count.append(arr)
            return
        else:
            for j in range(0, n):
                legal = True
                for i in range(0, r):
                    if (arr[i] == j) or (arr[i] == j + r - i) or (arr[i] == j - r + i):
                        legal = False
                if legal:
                    arr[r] = j
                    placequeens(arr, r + 1)

    placequeens(arr, 0)
    return len(count)


def Nqueens(n):
    column = [0 for _ in range(n * n)]
    diag = [0 for _ in range(n * n)]
    diag2 = [0 for _ in range(n * n)]

    def placequeens(y):
        count = 0
        if y == n:
            count += 1
            return
        for i in range(0, n):
            if column[i] or diag[i + y] or diag2[i - y + n - 1]: continue
            column[i] = diag[i + y] = diag2[i - y + n - 1] = 1
            placequeens(y + 1)
            column[i] = diag[i + y] = diag2[i - y + n - 1] = 0

    placequeens(0)
    return column


if __name__ == '__main__':
    # SolveNQueens(64)
    print(Nqueens(4))
