def permutation(arr):
    output = []

    def backtrack(nums, current):
        if len(current) == len(arr) and len(output) < 3:
            output.append(current)
            return
        else:
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i + 1:], current + [nums[i]])

    backtrack(arr, [])
    return output


print(permutation([3, 2, 1]))
print(permutation([1, 2, 3]))


def permuteString(sentence):
    result = []

    def backtrack(word, current):
        if len(current) == len(sentence):
            result.append(current)
            return
        else:
            for i in range(len(word)):
                backtrack(word[:i] + word[i + 1:], current + word[i])

    backtrack(sentence, "")
    return result


print(permuteString("ade"))
