class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)

        def isDivisor(s):
            if n % len(s) or m % len(s):
                return False 
            factor1, factor2 = n // len(s), m // len(s)
            if factor1 * s == str1 and factor2 * s == str2:
                return True 
            return False 

        for l in range(min(n, m), 0, -1):
            if isDivisor(str1[:l]):
                return str1[:l]
        return ""