from functools import cache 

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:        
        @cache
        def dfs(i):
            longest = 1
            if i == len(nums):
                return 1 

            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    longest = max(longest, 1 + dfs(j))
            return longest 
        return max(dfs(i) for i in range(len(nums)))