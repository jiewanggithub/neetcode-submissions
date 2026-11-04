class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def isPalindrome(s):
            return s[::-1] == s 
            
        def dfs(i):
            if i == len(s):
                res.append(path.copy())
                return 
            for j in range(i, len(s)):
                t = s[i:j + 1]
                if isPalindrome(t):
                    path.append(t)
                    dfs(j + 1)
                    path.pop()
        dfs(0)
        return res 
