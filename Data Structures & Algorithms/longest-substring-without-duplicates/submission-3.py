class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        counter = Counter()
        left = 0
        ans = 0

        for right, x in enumerate(s):
            counter[x] += 1

            while counter[x] > 1:
                counter[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)

        return ans     
