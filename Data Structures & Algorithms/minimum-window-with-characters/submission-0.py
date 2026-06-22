class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counterS, window = Counter(), Counter(t)

        have, need = 0, len(window)
        left = 0
        lenRes, res = float("inf"), [-1, -1]

        for right in range(len(s)):
            val = s[right]
            counterS[val] += 1

            if val in window and counterS[val] == window[val]:
                have += 1

            while need == have:
                if right - left + 1 < lenRes:
                    lenRes = right - left + 1
                    res = [left, right]
                
                counterS[s[left]] -= 1
                if s[left] in window and counterS[s[left]] < window[s[left]]:
                    have -= 1
                left += 1

        l, r = res
        return s[l:r+1] if lenRes != float("inf") else ""
