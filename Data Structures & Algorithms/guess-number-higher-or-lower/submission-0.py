# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        numMin, numMax = 1, n
        m = (numMin + numMax) // 2
        while guess(m) != 0:
            m = (numMin + numMax) // 2
            if guess(m) == -1:
                numMax = m - 1
            elif guess(m) == 1:
                numMin = m + 1 
            m = (numMin + numMax) // 2
        return m 
        