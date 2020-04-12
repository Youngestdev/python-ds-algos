def solution(A):
    # write your code in Python 3.6
    counter = dict()
    for i in A:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
    return min(counter, key=counter.get)
