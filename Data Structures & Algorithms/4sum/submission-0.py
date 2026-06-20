class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                left, right = j + 1, len(nums) - 1
                while left < right:
                    val = nums[left] + nums[right] + nums[i] + nums[j]
                    if target == val:
                        res.add((nums[left], nums[right], nums[i], nums[j]))
                        left += 1
                        right -= 1
                    elif target > val:
                        left += 1
                    else:
                        right -= 1
        return list(map(list, res))
                    
        