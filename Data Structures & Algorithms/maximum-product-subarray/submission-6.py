class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)

        curMax, curMin = 1, 1
        for num in nums:
            tmp = curMax * num
            curMax = max(tmp, num, curMin * num)
            curMin = min(tmp, curMin * num, num )
            res = max(curMax, res)
        return res 