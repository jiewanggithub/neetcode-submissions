class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            x = nums[i]
            if i > 0 and x == nums[i - 1]:
                continue 
            if x + nums[-1] + nums[-2] < 0:
                continue 
            
            if x + nums[i + 1] + nums[i + 2] > 0:
                break

            j = i + 1
            k = len(nums) - 1

            while j < k:
                s = x + nums[j] + nums[k]
                if s < 0:
                    j += 1
                elif s > 0:
                    k -= 1
                else:
                    res.append([x, nums[j], nums[k]])

                    j += 1 
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return res  
            
