class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def dfs(i, s):
            if i == len(nums):
                res.append(path.copy())
                return 
            
            path.append(nums[i])
            dfs(i + 1, s - {nums[i]})
            path.pop()
            dfs(i + 1, s)
        
        dfs(0, set())
        return res 
