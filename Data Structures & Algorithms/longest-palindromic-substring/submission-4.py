class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        "Center Expansion"
        indices = (0, 0)
        longest = 1
        for i in range(len(s)):
            j, k = i, i + 1
            while j >= 0 and k < len(s):
                if s[j] == s[k]:
                    if k - j + 1 > longest:
                        longest = k - j + 1
                        indices = (j, k)
                    j -= 1
                    k += 1 
                else:
                    break

            j, k = i - 1, i + 1
            while j >= 0 and k < len(s):
                if s[j] == s[k]:
                    if k - j + 1 > longest:
                        longest = k - j + 1
                        indices = (j, k)
                    j -= 1
                    k += 1 
                else:
                    break
        return s[indices[0]:indices[1]+1] 
                    
            
        