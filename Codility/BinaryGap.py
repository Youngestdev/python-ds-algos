def solution(N):
    # write your code in Python 3.6
    binary_equiv = bin(N)[2:].split('1')[:-1]
    print(binary_equiv)

    if not binary_equiv or binary_equiv == ['']:
        return 0
    else:
        return len(max(binary_equiv))