class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binarySearch(left, right, target):
            mid = left + (right - left ) // 2
            if left > right:
                return -1 
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binarySearch(left, mid - 1, target)
            else:
                return binarySearch(mid + 1, right, target)
        
        return binarySearch(0, len(nums) - 1, target)

    