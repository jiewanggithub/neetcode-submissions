class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        MAPPING = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        if not digits:
            return []
            
        res = []
        path = []

        def dfs(i):
            if i == len(digits):
                res.append("".join(path.copy()))
                return
            
            for x in MAPPING[int(digits[i])]:
                path.append(x)
                dfs(i + 1)
                path.pop()
        dfs(0)
        return res
