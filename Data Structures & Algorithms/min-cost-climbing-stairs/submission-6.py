from functools import cache 
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        one = two = 0
        for i in range(n - 1, -1 , -1):
            one, two = min(one, two) + cost[i], one 

        return min(one, two)
        """
        @cache 
        def dfs(i):
            if i >= n:
                return 0
            
            res = min(dfs(i + 1), dfs(i + 2)) + cost[i]
            return res
        return min(dfs(0), dfs(1))
        """