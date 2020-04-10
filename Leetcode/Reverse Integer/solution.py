class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        if x > 0:
            ans = int(str(x)[::-1])
        if x < 0:
            ans = -1 * int(str(x*-1)[::-1])
        
        min_value = -2**31
        max_value = 2**31 - 1
        
        if ans not in range(min_value, max_value):
            return 0
        else:
            return ans