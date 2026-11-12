class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        res = 0
        used = set()

        def dfs(i):
            nonlocal res

            if i == n:
                res = max(res, len(used))
                return 
            
            for j in range(i + 1, n + 1):
                sub = s[i:j]
                if sub in used:
                    continue
                used.add(sub)
                dfs(j)
                used.remove(sub)
        dfs(0)
        return res 