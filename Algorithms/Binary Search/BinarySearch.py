class BinarySearch:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def iterative(self, target):
        low = 0
        high = len(self.data) - 1

        while low <= high:
            mid = (low + high) // 2

            if target == self.data[mid]:
                return True
            if target < self.data[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return False

    def recursive(self, target, low, high):
        if low > high:
            return False
        else:
            mid = (low + high) // 2
            if target == self.data[mid]:
                return True
            elif target < self.data[mid]:
                return self.recursive(self.data, target, low, mid-1)
            else:
                return self.recursive(self.data, target, mid+1, high)

arr = [1,2,3,4,5]
test = BinarySearch(arr)
print(test.iterative(2))
print(test.recursive(3, 0, len(arr)-1))