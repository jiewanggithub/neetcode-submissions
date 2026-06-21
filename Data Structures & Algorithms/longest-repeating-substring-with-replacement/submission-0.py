class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = Counter()
        maxFre = 0
        left = 0
        res = 0

        for right, x in enumerate(s):
            cnt[x] += 1
            maxFre = max(maxFre, cnt[x])

            while right - left + 1 - maxFre > k:
                cnt[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1) 
        return res