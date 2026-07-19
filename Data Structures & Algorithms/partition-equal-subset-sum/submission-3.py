from functools import cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False 
        
        @cache
        def dfs(i, sum_):
            if sum_ == total // 2:
                return True 
            
            if sum_ > total // 2:
                return False 
                
            if i == len(nums):
                return False 
            return dfs(i + 1, sum_ + nums[i]) or dfs(i + 1, sum_)
        
        return dfs(0,0)
 
                            