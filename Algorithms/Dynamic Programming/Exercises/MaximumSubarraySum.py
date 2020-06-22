def maximumSubarraySum(array):
    max_sum = current_sum = 0
    for i in range(len(array)):
        current_sum = max(array[i], current_sum + array[i])
        max_sum = max(max_sum, current_sum)
    return max_sum


print(maximumSubarraySum([-6, 12, -7, 0, 14, -7, 5]))