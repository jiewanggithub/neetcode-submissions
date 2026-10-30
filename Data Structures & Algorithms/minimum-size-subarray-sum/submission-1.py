class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        left = right = 0
        s = 0 
        while right < len(nums):
            s += nums[right]
            while s >= target:
                res = min(res, right - left + 1)
                s -= nums[left]
                left += 1
            right += 1
        
        return res if res < float("inf") else 0