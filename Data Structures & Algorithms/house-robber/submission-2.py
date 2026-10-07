class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.helper(nums)

    def helper(self, nums):
        rob1 = rob2 = 0
        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2 
            rob2 = newRob 
        return rob2
        
        