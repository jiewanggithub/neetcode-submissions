class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # temperature, index

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                temp, tempIndex = stack.pop()
                res[tempIndex] = (i - tempIndex)
            stack.append([t, i])
        return res