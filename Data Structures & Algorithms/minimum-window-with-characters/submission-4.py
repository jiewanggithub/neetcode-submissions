class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt_s, cnt_t = Counter(), Counter(t)

        have, need = 0, len(cnt_t)
        left = 0
        shortest = None

        for right in range(len(s)):
            val = s[right]
            cnt_s[val] += 1

            if val in cnt_t and cnt_s[val] == cnt_t[val]:
                have += 1
            
            while need == have:
                if shortest is None or right - left < shortest[1] - shortest[0]:
                    shortest = (left, right)

                cnt_s[s[left]] -= 1
                if s[left] in cnt_t and cnt_s[s[left]] < cnt_t[s[left]]:
                    have -= 1
                
                left += 1   
            
        if shortest is None:
            return ""
        l, r = shortest
        return s[l:r + 1]
        
