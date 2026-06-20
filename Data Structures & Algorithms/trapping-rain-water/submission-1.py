class Solution:
    def trap(self, height: List[int]) -> int:
        prefix, suffix = [0] * len(height) , [0] * len(height)
        maxPrefix = height[0]
        maxSuffix = height[-1]
        res = 0
        
        for i in range(1, len(height)):
            prefix[i] = maxPrefix
            maxPrefix = max(height[i], maxPrefix)

        for j in range(len(height) - 2, -1, -1):
            suffix[j] = maxSuffix
            maxSuffix = max(height[j], maxSuffix)
        
        for k in range(len(height)):
            val = min(suffix[k], prefix[k]) - height[k]
            res += max(val, 0)
        return res