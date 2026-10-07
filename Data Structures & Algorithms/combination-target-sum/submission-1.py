class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(start, n):
            if n == target:
                res.append(path.copy())
                return
            total = 0
            for j in range(start, len(nums)):
                if n + nums[j] <= target:
                    path.append(nums[j])
                    dfs(j, n + nums[j])
                    path.pop()
        
        dfs(0, 0)
        return res