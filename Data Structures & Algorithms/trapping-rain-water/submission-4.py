class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height)
        prefix[0] = height[0] 
        suffix = [0] * len(height)
        suffix[-1] = height[-1]
        ans = 0
        for i in range(1, len(height)):
            prefix[i] = max(height[i], prefix[i - 1])
        
        for i in range(len(height) - 2, -1, -1):
            suffix[i] = max(height[i], suffix[i + 1])

        for i in range(len(height)):
            ans += max(0, min(suffix[i], prefix[i]) - height[i])
        
        return ans 
                

        