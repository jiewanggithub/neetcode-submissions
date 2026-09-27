class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        total = 0
        for i in range(len(nums) + 1):
            res += i
        for num in nums:
            total += num
        return res - total 