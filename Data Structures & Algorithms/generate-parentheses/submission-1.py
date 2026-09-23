class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def dfs(total, left):
            if total == n * 2:
                res.append("".join(path.copy()))
                return
            right = total - left
            if left < n:
                path.append("(")
                dfs(total + 1, left + 1)
                path.pop()
            
            if right < left:
                path.append(")")
                dfs(total + 1, left)
                path.pop()


        dfs(0, 0)
        return res             