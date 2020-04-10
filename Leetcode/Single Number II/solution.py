class Solution:
    def singleNumber(self, nums: List[int]) -> int:
      store = dict()

      for i in nums:
          if i in store:
            store[i] += 1
          else:
              store[i] = 1
      return min(store, key=store.get)  