class Solution:
    def reverseBits(self, n: int) -> int:
        arr = []
        for i in range(32):
            char = 1 if (1 << i & n) else 0
            arr.append(str(char))

        return int("".join(arr), 2)