class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > heights[i]:
                pos, h = stack.pop()
                res = max(res, h * (i - pos))
                start = pos
            stack.append([start, height])
            
        n = len(heights)
        for pos, h in stack:
            res = max(res, h * (n - pos))
        return res 