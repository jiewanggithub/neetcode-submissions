class Solution:
    def tribonacci(self, n: int) -> int:
        zero, one, two = 0, 1, 1

        if n == 0:
            return zero
        if n == 1:
            return one

        if n == 2:
            return two

        for i in range(3, n + 1):
            zero, one, two = one, two, zero + one + two
        
        return two