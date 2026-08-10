class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        numSum = sum(stones)
        target = numSum // 2
        
        dp = [[0] * (target + 1) for _ in range(len(stones) + 1)]

        for i in range(len(stones) - 1, -1, -1):
            for t in range(target + 1):
                dp[i][t] = dp[i+1][t]

                if t >= stones[i]:
                    dp[i][t] = max(dp[i][t], dp[i + 1][t - stones[i]] + stones[i])
        
        return numSum - (2 * dp[0][target])