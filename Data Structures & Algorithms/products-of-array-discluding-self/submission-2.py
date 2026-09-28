class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        # prefix 
        for i in range(1, len(nums)):
            output[i] = output[i - 1] * nums[i - 1]
        
        suffix = 1
        # suffix
        for i in range(len(nums) - 2, -1, -1):
            suffix *= nums[i + 1]
            output[i] *= suffix
        
        return output