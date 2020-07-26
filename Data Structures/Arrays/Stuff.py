def solution(array, index):
    less, equal, greater = 0, 0, len(array)
    pivot = array[index]

    while equal < greater:
        if array[equal] < pivot:
            array[less], array[equal] = array[equal], array[less]
            equal, less = equal + 1, less + 1
        elif array[equal] == pivot:
            equal += 1
        else:
            greater -= 1
            array[equal], array[greater] = array[greater], array[equal]
    return array


def solution2(array):
    steps = 1
    l, r = 0, array[0]

    while r < len(array) - 1:
        steps += 1
        maxRange = max(i + array[i] for i in range(l, r + 1))
        l, r = r, maxRange
    return steps


def perfect_squares(num):
    num = abs(num)

    i = 2
    while True:
        if pow(num, 0.5) == i:
            print(num, "is a perfect square")
            break
        i += 1
    # /    else:
    print(num, "isnt")
    # return print(num, "isn't")

if __name__ == '__main__':
    perfect_squares(5)
    perfect_squares(4)