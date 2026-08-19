class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSquares(n):
            output = 0

            while n:
                digit = n % 10
                digit = digit ** 2
                output += digit
                n = n // 10
            return output 

        slow, fast = n, sumOfSquares(n)
        while slow != fast:
            fast = sumOfSquares(fast)
            fast = sumOfSquares(fast)
            slow = sumOfSquares(slow)
        return True if fast == 1 else False 
