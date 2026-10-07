class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        def binarySearch(nums, left, right, target):
            if left > right:
                return -1
            mid = (right + left) // 2

            if nums[mid] == target:
                return mid 
            
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    return binarySearch(nums, left, mid - 1, target)
                else: 
                    return binarySearch(nums, mid + 1, right, target)
            else:
                if nums[mid] < target <= nums[right]:
                    return binarySearch(nums, mid + 1, right, target)
                else:
                    return binarySearch(nums, left, mid - 1, target)
        return binarySearch(nums, 0, len(nums) - 1, target)