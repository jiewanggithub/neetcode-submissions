class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = n
        for i in range(n):
            j, k = i, i + 1
            while j > -1 and k < n:
                if s[j] == s[k]:
                    count += 1
                else:
                    break
                j -= 1
                k += 1

            j, k = i - 1, i + 1
            while j > -1 and k < n:
                if s[j] == s[k]:
                    count += 1
                else:
                    break
                j -= 1
                k += 1
        return count 