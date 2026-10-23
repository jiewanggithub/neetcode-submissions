from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        @cache
        def dfs(i):
            if i > len(s):
                return False

            if i == len(s):
                return True 

            res = False
            for word in wordDict:
                if s[i:i + len(word)] == word:
                    res = res or dfs(i + len(word))
            
            return res 
        return dfs(0)