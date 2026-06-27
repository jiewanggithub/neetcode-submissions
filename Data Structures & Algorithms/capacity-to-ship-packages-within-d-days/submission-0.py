class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        minCap = r

        while l <= r:
            m = (l + r) // 2

            cap = m
            day = 1
            for w in weights:
                if cap - w < 0:
                    cap = m
                    day += 1
                cap -= w
            
            if day <= days:
                minCap = min(minCap, m)
                r = m - 1
            else:
                l = m + 1

        return minCap