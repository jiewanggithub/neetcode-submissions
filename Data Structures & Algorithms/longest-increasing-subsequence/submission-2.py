from functools import cache 
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        @cache 
        def dfs(i):
            if i == len(nums):
                return 1
            
            res = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    res = max(res, 1 + dfs(j))
            return res 
        
        return max(dfs(i) for i in range(len(nums)))
        
            