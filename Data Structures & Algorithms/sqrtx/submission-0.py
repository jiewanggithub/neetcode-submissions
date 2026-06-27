class Solution:
    def mySqrt(self, x: int) -> int:
        return self.sqrt(0, x, x) 

    def sqrt(self, l, r, x):
        m = (l + r) // 2
        if m * m <= x and x < (m + 1) * (m + 1):
            return m
        elif m * m < x:
            return self.sqrt(m + 1, r, x)
        elif m * m > x:
            return self.sqrt(l, m - 1, x)

