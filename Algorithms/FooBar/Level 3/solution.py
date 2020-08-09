def solution(n):
    # Naive solution.
    n = int(n)
    count = 0
    while n > 1:
        if n % 2 == 0:
            n //= 2
        elif n == 3 or n % 4 == 1:
            n -= 1
        else:
            n += 1
        count += 1
    return count


if __name__ == '__main__':
    print(solution(4))
    print(solution(2))