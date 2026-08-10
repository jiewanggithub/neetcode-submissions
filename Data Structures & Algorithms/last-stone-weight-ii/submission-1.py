from functools import cache
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        numSum = sum(stones)
        target = math.ceil( numSum / 2)
        
        @cache
        def dfs(i, total):
            if total >= target or i == len(stones):
                return abs(total - (numSum - total))
            
            return min(dfs(i + 1, total), dfs(i+ 1, total + stones[i]))
        
        return dfs(0,0)        

            