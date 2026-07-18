from functools import cache 
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1:
            return nums[0]

        """
        @cache
        def dfs(i, end):
            if i > end:
                return 0
            return max(dfs(i + 1, end), nums[i] + dfs(i + 2,end)

        return max(dfs(0, n-2), dfs(1, n-1))
        """

        def helper(s, e):
            dp = [0] * (n + 2)
            for i in range(e, s - 1, -1):
                dp[i] = max(dp[i + 1], dp[i + 2] + nums[i])
            return dp[s]

        n = len(nums)
        return max(helper(0, n-2), helper(1, n-1))           