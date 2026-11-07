from functools import cache 
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)

        @cache 
        def dfs(i, a):
            if i >= n:
                return 0
            
            cost = float('inf')
            if a < n // 2:
                cost = costs[i][0] + dfs(i + 1, a + 1)

            if i - a < n // 2:
                cost = min(cost, costs[i][1] + dfs(i + 1, a))
            return cost 
        return dfs(0, 0)

