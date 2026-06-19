class Solution:
    def isPalindrome(self, s: str) -> bool:

        def isSameChar(l, r):
            if l >= r:
                return True

            if not s[l].isalnum():
                return isSameChar(l + 1, r)

            if not s[r].isalnum():
                return isSameChar(l, r - 1)

            if s[l].lower() != s[r].lower():
                return False 

            return isSameChar(l + 1, r - 1)

        return isSameChar(0, len(s) - 1)
   
        