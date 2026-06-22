class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0

        left = 0
        curSum = 0
        minLen = float('inf')
        for right in range(len(nums)):
            curSum += nums[right]
            while curSum >= target:
                minLen = min(minLen, right - left + 1)
                curSum -= nums[left]
                left += 1
        return minLen        