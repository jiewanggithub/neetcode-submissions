from functools import cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        @cache 
        def dfs(l, r):
            if l > r:
                return 0
            
            max_ = 0
            for i in range(l, r + 1):
                left = 1 if l - 1 < 0 else nums[l - 1]
                right = 1 if r + 1 > len(nums) - 1 else nums[r + 1]
                coins = left * nums[i] * right
                max_ = max(
                    max_,
                    dfs(l, i - 1) + coins +
                    dfs(i + 1, r)
                )
            return max_
        return dfs(0, len(nums) - 1)
