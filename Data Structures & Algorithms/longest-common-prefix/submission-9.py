class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first, last = strs[0], strs[-1]

        i = 0
        while i < len(first) and i < len(last) and last[i] == first[i]:
            i += 1
        return first[:i]