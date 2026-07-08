class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        path = []
        
        def dfs(i, s):
            if i == n:
                res.append(path.copy())
                return 
            
            for x in s:
                path.append(x)
                dfs(i + 1, s - {x})
                path.pop()
        dfs(0, set(nums))
        return res 