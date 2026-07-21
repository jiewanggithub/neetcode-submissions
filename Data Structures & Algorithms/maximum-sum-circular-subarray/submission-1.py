class Solution:
    def findMaxSumSubarray(self, nums):
        curr, max_ = 0, float('-inf')
        for num in nums:
            if curr + num >= num:
                curr += num
            else:
                curr = num
            max_ = max(max_, curr)
        return max_
    def findMinSumSubarray(self, nums):
        curr, min_ = 0, float('inf')
        for num in nums:
            if num + curr <= num:
                curr += num
            else:
                curr = num
            min_ = min(min_, curr)
        return min_
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        min_, max_ = self.findMinSumSubarray(nums), self.findMaxSumSubarray(nums)
        total = sum(nums)
        if max_ < 0:
            return max_
        return max(total - min_ , max_)