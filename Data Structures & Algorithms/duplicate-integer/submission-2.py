class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        pre = None
        for n in nums:
            if pre != None and pre == n:
                return True 
            pre = n
        return False 