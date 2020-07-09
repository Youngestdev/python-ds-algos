"""
Counting sort.
Takes an array and a number, number here should be the highest number in the list I think
"""


def counting_sort(array, number):
    c = [0] * (number+1)
    for i in range(len(array)):
        c[array[i]] = c[array[i]] + 1
    for i in range(1, number):
        c[i] = c[i] + c[i-1]

    b = [0] * (len(array))
    for i in range(len(array)-1, -1, -1):
        c[array[i]] = c[array[i]] - 1
        b[c[array[i]]] = array[i]
    
    return b
