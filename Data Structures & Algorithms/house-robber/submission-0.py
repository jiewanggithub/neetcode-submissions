class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 2)
        for i, num in enumerate(nums):
            dp[i+2] = max(dp[i+1], dp[i] + num)
        return dp[n + 1]

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