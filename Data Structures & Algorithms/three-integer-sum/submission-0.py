class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:\
        # nlogn
        nums.sort()
        # [-1, 0, 1, 2, -1, -4]
        # [-4, -1, -1, 0, 1, 2] 
        # using the algo of 2 sum in order
        tuples = []
        for i in range(len(nums)):
            target = 0 - nums[i]
            k, j = i + 1, len(nums) - 1
            while k < j:
                val = nums[k] + nums[j]
                if val == target:
                    tuples.append((nums[i], nums[k], nums[j]))
                    k += 1
                    j -= 1
                elif val > target:
                    j -= 1
                else:
                    k += 1
        hashset = set(tuples)
        return list(map(list, hashset))    