from functools import cache 
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # p: posive sum 
        # s - p: negative sum
        # p - (s - p) = target 正的和 - 负的和 = target
        # 2p - s = target 
        # p = (s + t) // 2 
        target += sum(nums)
        if target < 0 or target % 2:
            return 0
        target //= 2       
        
        @cache 
        def dfs(i, c):
            if i < 0:
                return 1 if c == 0 else 0
            
            if nums[i] > c:
                return dfs(i - 1, c)
            
            return dfs(i - 1, c) + dfs(i - 1, c - nums[i])
        return dfs(len(nums) - 1, target)