class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        last_index = {}
        for i, char in enumerate(s):
            last_index[char] = i
        
        start = 0
        end = 0
        for i in range(len(s)):
            end = max(end, last_index[s[i]])

            if i == end:
                res.append(i - start + 1)
                start = i + 1
        return res 