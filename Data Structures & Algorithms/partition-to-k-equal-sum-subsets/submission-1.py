class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort(reverse=True)
        size = sum(nums) // k
        if size != sum(nums) / k:
            return False 
        subsets = [0] * k

        def dfs(i):
            if i == len(nums):
                return True
            
            for j in range(k):
                if subsets[j] + nums[i] <= size:
                    subsets[j] += nums[i]
                    if dfs(i+1):
                        return True
                    subsets[j] -= nums[i]
                if subsets[j] == 0:
                    break
            return False 
        return dfs(0)