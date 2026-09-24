class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def dfs(total, left):
            if total == 2 * n:
                res.append("".join(path.copy()))
                return

            right = total - left

            if left < n:
                path.append("(")
                dfs(total + 1, left + 1)
                path.pop()

            if left > right:
                path.append(")")
                dfs(total + 1, left)
                path.pop()
        dfs(0, 0)
        return res        