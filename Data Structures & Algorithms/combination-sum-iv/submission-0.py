from functools import cache
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        @cache 
        def dfs(s):
            if s == target:
                return 1

            if s > target:
                return 0
            
            res = 0
            for i in range(len(nums)):
                res += dfs(s + nums[i])
            return res 
        return dfs(0)