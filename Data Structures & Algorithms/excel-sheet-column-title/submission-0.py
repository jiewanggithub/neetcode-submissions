class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber:
            mod = (columnNumber - 1) % 26
            columnNumber = (columnNumber - 1) // 26
            
            res += chr(ord('A') + mod)
        return res[::-1]

        