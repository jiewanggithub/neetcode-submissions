class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(0, len(nums)-1, nums, target)

    def binarySearch(self, l, r, nums, target) -> int:
        if l > r:
            return -1
        m = (l + r) // 2
        
        if nums[m] == target:
            return m
        elif nums[m] > target:
            return self.binarySearch(l, m - 1, nums, target)
        else:
            return self.binarySearch(m + 1, r, nums, target)