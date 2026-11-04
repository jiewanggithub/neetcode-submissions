class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        col = []
        
        def valid(r, c):
            for R in range(r):
                C = col[R]
                if C + R == r + c or R - C == r - c:
                    return False
            return True 

        def dfs(r, s):
            if r == n:
                res.append([c*"." + "Q" +(n - c - 1)*"." for c in col])
                return 
            
            for c in s:
                if valid(r, c):
                    col.append(c)
                    dfs(r + 1, s - {c})
                    col.pop()
        dfs(0, set(range(n)))
        return res