class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        maxPre, maxSuf = height[0], height[n - 1]
        l, r = 1, n - 2
        res = 0

        while l <= r:
            if maxPre <= maxSuf:
                res += max(0, maxPre - height[l])
                maxPre = max(maxPre, height[l])
                l += 1
            else:
                res += max(0, maxSuf - height[r])
                maxSuf = max(maxSuf, height[r])
                r -= 1
        return res