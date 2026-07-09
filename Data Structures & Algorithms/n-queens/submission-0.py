class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols = []

        def valid(r, c):
            for R in range(r):
                C = cols[R]
                if C + R == c + r or C - R == c - r:
                    return False
            return True

        def dfs(r, s):
            if r == n:
                res.append(['.'*c + 'Q' + '.'*(n - 1 - c) for c in cols])
                return 

            for c in s:
                if valid(r, c):
                    cols.append(c)
                    dfs(r + 1, s - {c})
                    cols.pop()
        dfs(0, set(range(n)))
        return res             

