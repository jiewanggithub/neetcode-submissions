class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_prefix, max_suffix = 0, 0

        ans = 0
        while left <= right:
            max_prefix = max(height[left], max_prefix)
            max_suffix = max(height[right], max_suffix)

            if max_prefix <= max_suffix:
                ans += max_prefix - height[left]
                left += 1
            else:
                ans += max_suffix - height[right]
                right -= 1
        return ans   