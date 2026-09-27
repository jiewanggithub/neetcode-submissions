from collections import defaultdict
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(list) 
        for word in words:
            for char in word:
                adj[char]
            
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            min_len = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].append(w2[j])
                    break 

        res = []
        state = {}

        def dfs(char):
            if char in state:
                if state[char] == 1:
                    return False
                if state[char] == 2:
                    return True

            state[char] = 1
            for nei in adj[char]:
                if not dfs(nei):
                    return False
            
            state[char] = 2
            res.append(char)
            return True
        
        for char in adj:
            if not dfs(char):
                return ""
        return "".join(res[::-1])

