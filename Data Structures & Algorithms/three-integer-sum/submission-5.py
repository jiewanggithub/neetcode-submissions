class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums) - 2):
            x = nums[i]
            if i > 0 and x == nums[i - 1]:
                continue 
        
            j = i + 1
            k = len(nums) - 1

            while j < k:
                if x + nums[j] + nums[k] > 0:
                    k -= 1
                elif x + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    res.append([x, nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return res  

              