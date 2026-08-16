class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word2), len(word1)
        dp = [[0] * (m + 1) for _ in range(n + 1)] 
        for i in range(n + 1):
            for j in range(m + 1):
                if i == n:
                    dp[i][j] = len(word2) - j
                if j == m:
                    dp[i][j] = len(word1) - i

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = (1 + min(dp[i + 1][j + 1], dp[i][j + 1], 
                    dp[i + 1][j]))
        return dp[0][0]
