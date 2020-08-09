def solution(x, y):
    # Your code here
    # This looks like a GCD question. Problem statement is confusing.
    moves = 0
    x, y = int(x), int(y)

    while not (x == 1 and y == 1):
        if x <= 0 or y <= 0:
            return "impossible"
        if y == 1:
            return str(moves + x - 1)
        else:
            moves += int(x / y)
            x, y = y, x % y
    return str(moves)

if __name__ == '__main__':
    print(solution(4, 7))