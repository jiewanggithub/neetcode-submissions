class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char.lower() for char in s if char.isalnum())
        n = len(s)
        left, right = 0, n - 1
        while left <= right:

            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True 