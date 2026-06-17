class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 

        counterS, counterT = {}, {}
        for c in s:
            counterS[c] = 1 + counterS.get(c, 0)
        
        for c in t:
            counterT[c] = 1 + counterT.get(c, 0)
        
        for c in s:
            if counterS.get(c, 0) != counterT.get(c, 0):
                return False
        
        return True