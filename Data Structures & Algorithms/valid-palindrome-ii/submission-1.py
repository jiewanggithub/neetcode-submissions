class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isSameChar(l, r, c):
            if c > 1:
                return False
            if l >= r:
                return True

            if s[l] == s[r]:
                return isSameChar(l + 1, r - 1, c)
            
            return (
                isSameChar(l + 1, r, c + 1) or
                isSameChar(l, r - 1, c + 1)
            )
        
        return isSameChar(0, len(s) - 1, 0)
