# Solution one: Time complexity of O(n^2) and Space complexity of O(1)


def two_sum_brute_fore(arr, target):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                print(arr[i], arr[j])
                return True
    return False


# Solution two: Time complexity of O(n) and Space complexity of 0(n)

def two_sum_hash_table(arr, target):
    store = dict()

    for i in range(len(arr)):
        if arr[i] in store:
            print(store[arr[i]], arr[i])
            print("Store >> ", store)
            return True
        else:
            store[target - arr[i]] = arr[i]
    return False

# Solution three: Time complexity of 0(n) and Space complexity of 0(1)


def two_sum(arr, target):
    i = 0
    j = len(arr) - 1

    while i < j:
        if arr[i] + arr[j] == target:
            print(arr[i], arr[j])
            return True
        elif arr[i] + arr[j] < target:
            i += 1
        else:
            j -= 1
    return False
