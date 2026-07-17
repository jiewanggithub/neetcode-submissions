class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        #dp = [0] * (n + 2)
        dp0 = dp1 = 0
        for i, num in enumerate(nums):
            new_dp = max(dp1, dp0 + num)
            dp0 = dp1
            dp1 = new_dp
        return dp1

        """
        Brute Force by Backtracking
        Time Complexity: O(2**n)
        Space Complexity: O(1) 
        
        Add-on: @cache
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        @cache
        def dfs(i):
            if i < 0:
                return 0

            res = max(dfs(i - 1), dfs(i - 2) + nums[i])

            return res
        return dfs(len(nums) - 1)
        """