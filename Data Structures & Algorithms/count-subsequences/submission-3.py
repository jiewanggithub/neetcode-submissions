class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        dp = [0] * (len(t) + 1)    
        dp[len(t)] = 1

        for i in range(len(s) - 1, -1, -1):
            newDp = [0] * (len(t) + 1)
            newDp[len(t)] = 1
            for j in range(len(t) - 1, -1, -1):
                newDp[j] = dp[j]
                if s[i] == t[j]:
                    newDp[j] += dp[j + 1]
            dp = newDp
        return dp[0]