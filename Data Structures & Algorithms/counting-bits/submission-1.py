class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for num in range(n + 1):
            for j in range(32):
                if (1 << j) & num:
                    res[num] += 1
        return res 