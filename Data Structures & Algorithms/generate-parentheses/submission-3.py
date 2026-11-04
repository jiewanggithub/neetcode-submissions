class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []
        m = 2 * n
        def dfs(i, open):
            if i == m:
                res.append("".join(path))
                return 
            
            if open < n:
                path.append('(')
                dfs(i + 1, open + 1)
                path.pop()
            if i - open < open:
                path.append(')')
                dfs(i + 1, open)
                path.pop()
        dfs(0, 0)
        return res 