class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left, right = 0, 0 

        while right < len(nums):
            val = nums[left]
            for i in range(left + 1, min(len(nums),right + k + 1)):
                if nums[i] == val:
                    return True
            left += 1
            right += 1
                
        return False

        1, 2, 3, 1