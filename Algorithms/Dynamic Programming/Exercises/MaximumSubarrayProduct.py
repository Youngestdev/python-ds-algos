def maximumSubarrayProduct(nums):
    res, cur_min, cur_max = nums[0], nums[0], nums[0]
    for i in range(1, len(nums)):
        cur_max, cur_min = max(cur_max * nums[i], cur_min * nums[i], nums[i]), min(cur_max * nums[i], cur_min * nums[i],
                                                                                   nums[i])
        res = max(cur_max, res)
    return res

print(maximumSubarrayProduct([-6, 12, -7, 0, 14, -7, 5]))