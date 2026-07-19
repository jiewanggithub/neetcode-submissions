from functools import cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        target = sum(nums) // 2
        dp = set()
        dp.add(0)
        for i in range(len(nums) - 1, -1, -1):
            next_dp = set()
            for t in dp:
                next_dp.add(t + nums[i])
                next_dp.add(t)
            dp = next_dp
        return True if target in dp else False

        """
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
        """
                            