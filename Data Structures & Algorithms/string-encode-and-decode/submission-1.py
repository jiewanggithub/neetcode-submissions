class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        left = 0
        while left < len(s):
            j = left 

            while s[j] != "#":
                j += 1
            
            length = int(s[left:j])
            res.append(str(s[j + 1:j + 1 + length]))
            left = j + 1 + length
        return res

