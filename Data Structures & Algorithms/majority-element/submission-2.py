class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter, res = 0, 0 
        for n in nums:
            if counter == 0:
                res = n

            if n == res:
                counter += 1
            else:
                counter -= 1
        return res