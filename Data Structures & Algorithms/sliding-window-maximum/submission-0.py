class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        left, right = 0, k - 1

        while right < len(nums):
            levelMax = sorted(nums[left:right + 1])[-1]
            res.append(levelMax)
            left += 1
            right += 1
        return res

        