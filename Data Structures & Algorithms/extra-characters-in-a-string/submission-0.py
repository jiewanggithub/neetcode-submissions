from functools import cache
class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        root = Node()
        for word in dictionary:
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = Node()
                cur = cur.children[c]
            cur.endOfWord = True 
        
        n = len(s)

        @cache
        def dfs(i):
            if i == n:
                return 0
            
            res = 1 + dfs(i + 1)
             
            cur = root
            for j in range(i, n):
                if s[j] not in cur.children:
                    break
            
                cur = cur.children[s[j]]
                if cur.endOfWord:
                    res = min(res, dfs(j+1))
            return res
        return dfs(0)








