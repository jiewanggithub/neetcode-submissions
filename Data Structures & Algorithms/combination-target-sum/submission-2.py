class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(start, total):
            if total == target:
                res.append(path.copy())
                return
            
            for j in range(start, len(nums)):
                if total + nums[j] <= target:
                    path.append(nums[j])
                    dfs(j, nums[j] + total)
                    path.pop()
        dfs(0, 0)
        return res