import time

def fastRecursiveFibonacci(n):
    if n == 1:
        return 0, 1
    m = n // 2
    _pvr, _cur = fastRecursiveFibonacci(m)
    prev = _pvr ** 2 + _cur ** 2
    curr = _cur * ((2 * _pvr) + _cur)
    nxt = prev + curr
    if n % 2 == 0:
        return prev, curr
    else:
        return curr, nxt


def fibonacci(n):
    Fibonacci = [0, 1] + [0] * (n - 2)
    prev, curr = 1, 0
    for i in range(2, n):
        Fibonacci[i] = Fibonacci[i - 1] + Fibonacci[i - 2]
    print(Fibonacci)
    return Fibonacci[n - 1]


def iterativeFibonacci(n):
    prev, curr = 1, 0
    for i in range(1, n):
        _next = prev + curr
        prev = curr
        curr = _next
    return curr


if __name__ == "__main__":

    begin = time.perf_counter()
    fastRecursiveFibonacci(5000)
    end = time.perf_counter()
    print(f"5000 fibonacci steps done in {end - begin:0.4f} seconds")

