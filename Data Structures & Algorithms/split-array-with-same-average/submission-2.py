from functools import cache
class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        nums.sort()
        total = sum(nums)
        
        @cache
        def dfs(i, k, target):
            if k == 0:
                return target == 0
            
            if i == n or n - i < k:
                return False 
            
            if nums[i] * k > target:
                return False 
            
            if dfs(i + 1, k - 1, target - nums[i]):
                return True 
            
            return dfs(i + 1, k, target)
        
        for k in range(1, n // 2 + 1):
            if total * k % n != 0:
                continue
            target = total * k // n
            if dfs(0, k, target):
                return True

        return False


