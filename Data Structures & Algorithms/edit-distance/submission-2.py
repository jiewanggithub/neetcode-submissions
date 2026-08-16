class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word2), len(word1)
        dp = [m - j for j in range(m + 1)]

        for i in range(n - 1, -1, -1):
            diagonal = dp[m]
            dp[m] = n - i
            for j in range(m - 1, -1, -1):
                down = dp[j]
                if word1[i] == word2[j]:
                    dp[j] = diagonal
                else:
                    dp[j] = (1 + min(down, diagonal, dp[j + 1]))
                diagonal = down
        return dp[0]
