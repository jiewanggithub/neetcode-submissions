class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return 

        nums[:] = nums[::-1]
        k %= len(nums)
        nums[:] = nums[0:k][::-1] + nums[k:][::-1]
        


        