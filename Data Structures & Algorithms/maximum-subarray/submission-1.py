class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        max_ = float('-inf')
        for num in nums:
            if num + curr >= num:
                curr += num 
            else:
                curr = num
            max_ = max(max_, curr)
        return max_