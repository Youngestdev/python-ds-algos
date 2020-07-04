def cyclicSort(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    return nums

if __name__ == '__main__':
    nums = [3, 1, 5, 4, 2]
    print(cyclicSort(nums))