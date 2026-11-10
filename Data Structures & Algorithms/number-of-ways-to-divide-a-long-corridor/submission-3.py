from functools import cache

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        
        seats = [i for i in range(len(corridor)) if corridor[i] == "S"]

        if len(seats) == 0 or len(seats) % 2:
            return 0
        res = 1 
        for i in range(2, len(seats), 2):
            res *= seats[i] - seats[i - 1]
            res %= MOD
        return res