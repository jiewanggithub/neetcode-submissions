class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [float('-inf')] * (n + 1)
        dp[n] = 0

        for i in range(len(stoneValue) - 1, -1, -1):
            for j in range(i, min(i + 3, len(stoneValue))):
                dp[i] = max(dp[i], sum(stoneValue[i:j+1]) - dp[j + 1])
        result = dp[0]
        if result == 0:
            return "Tie"
        
        return "Alice" if result > 0 else "Bob" 
        """
        n = len(stoneValue)
        dp = {}

        def dfs(i):
            if i >= n:
                return 0
            if i in dp:
                return dp[i]

            res, total = float("-inf"), 0
            for j in range(i, min(i + 3, n)):
                total += stoneValue[j]
                res = max(res, total - dfs(j + 1))

            dp[i] = res
            return res

        result = dfs(0)
        if result == 0:
            return "Tie"
        return "Alice" if result > 0 else "Bob"
        """