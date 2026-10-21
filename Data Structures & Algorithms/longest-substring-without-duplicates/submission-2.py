class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        res = 0
        counter = Counter()
        for right, x in enumerate(s):
            counter[x] += 1
            while counter[x] > 1:
                counter[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res 