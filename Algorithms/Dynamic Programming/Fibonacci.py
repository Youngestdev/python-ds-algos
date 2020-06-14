def fastRecursiveFibonacci(n):
    if n == 1:
        return 0, 1
    m = n // 2
    _pvr, _cur = fastRecursiveFibonacci(m)
    prev = _pvr**2 + _cur**2
    curr = _cur * ((2 * _pvr) + _cur)
    nxt = prev + curr
    if n % 2 == 0:
        return prev, curr
    else:
        return curr, nxt
print(fastRecursiveFibonacci(9))
print(fastRecursiveFibonacci(10))