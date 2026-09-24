class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first, last = strs[0], strs[-1]
        i = 0

        while i < min(len(first), len(last)):
            if first[i] != last[i]:
                break
            i += 1
        
        return first[:i]