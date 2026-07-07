class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(start, total):
            if sum(path) == target:
                res.append(path.copy())
                return
            
            if sum(path) > target:
                return 

            for j in range(start, len(nums)):
                path.append(nums[j])
                dfs(j, total + nums[j])
                path.pop()
            
        dfs(0, 0)
        return res 
