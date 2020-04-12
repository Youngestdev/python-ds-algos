
def solution(X, Y, D):
    # write your code in Python 3.6
    if ((Y - X) % D == 0):
        return (Y - X) // D
    return (Y - X) // D + 1
