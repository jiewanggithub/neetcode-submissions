class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        n = len(heights)
        left, right = 0, n - 1

        while left < right:
            length = right - left
            ans = max(ans, length * min(heights[left], heights[right]))

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        
        return ans 