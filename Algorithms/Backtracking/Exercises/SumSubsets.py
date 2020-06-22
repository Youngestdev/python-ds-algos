def sumsubsets(arr, target):
    result = []

    def backtrack(valarr, current):
        if sum(current) == target:
            # No idea if the condition was required but ko kan aiye
            result.append(current[:])
            return
        else:
            for i in range(len(valarr)):
                backtrack(valarr[:i], current + [valarr[i]])

    backtrack(arr, [])
    return result

print(sumsubsets([1, 2, 3, 4, 5], 4))
