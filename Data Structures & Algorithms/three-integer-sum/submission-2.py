class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums) 
        for i in range(n - 1):
            if i > 0 and nums[i - 1] == nums[i]:
                continue 
            if nums[i] > 0:
                break 

            left, right = i + 1, n - 1
            while left < right:
                sum_ = nums[i] + nums[left] + nums[right]
                if sum_ == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif sum_ > 0:
                    right -= 1
                else:
                    left += 1
        return res 
              