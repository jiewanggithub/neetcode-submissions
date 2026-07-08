class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def dfs(i):
            if i == len(s):
                res.append(path.copy())
                return
            
            for j in range (i, len(s)):
                t = s[i:j+1]
                if t == t[::-1]:
                    path.append(t)
                    dfs(j+1)
                    path.pop()
        dfs(0)
        return res 