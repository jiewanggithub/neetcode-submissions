class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = 0, n - 1
        
        res = 0
        while left < right:
            volume = (right - left) * min(heights[left], heights[right])
            res = max(res, volume)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return res 