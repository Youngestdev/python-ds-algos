#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'groupSort' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
import itertools

def groupSort(arr):
    # Write your code here
    store = {}
    result = []
    for i in range(len(arr)):
        if arr[i] not in store:
            store[arr[i]] = 0
        store[arr[i]] += 1
    
    for k, v in sorted(list(store.items()), key=lambda x: (-1*x[1], x[0])):
        # print("{} {}".format(k, v))
        result.append((k, v))
    
    # print(result)
    return result

if __name__ == '__main__':
    groupSort(arr)
