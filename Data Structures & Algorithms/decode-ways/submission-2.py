from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        @cache 
        def dfs(i):
            if i >= n:
                return 1

            cnt = 0
            if int(s[i]) == 0:
                return 0
                
            if i + 1 < n and (
                s[i] == '1' or
                (s[i] == '2' and s[i + 1] <= '6')
            ):
                cnt = dfs(i + 2)
            return cnt + dfs(i + 1)

        return dfs(0)