def solution(xs):
    # Your code here
    # Original author - https://github.com/rudisimo/google-foobar/blob/master/solutions/power_hungry/solution.py
    if len(xs) == 0:
        return str(0)

    if len(xs) == 1:
        # return the only value
        return str(xs[0])

    if len(xs) > 50:
        return str(0)

    max_value = [i for i in xs if i > 0]
    min_value = [j for j in xs if j < 0]

    if len(min_value) == 1 and len(max_value) == 0:
        return str(0)

    if len(min_value) == 0 and len(max_value) == 0:
        return str(0)

    output = 1L
    for i in max_value:
        output *= i
        print(output)

    if len(min_value) % 2 == 1:
        min_value.remove(max(min_value))
        print(min_value)

    for j in min_value:
        print(output)
        output *= j
    return str(output)

print(solution([-2,-3,4,-5]))