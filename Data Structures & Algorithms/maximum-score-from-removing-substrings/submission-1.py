class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        

        def remove(s, pattern, val):
            stack = []
            points = 0

            for ch in s:
                if stack and stack[-1] == pattern[0] and ch == pattern[1]:
                    points += val
                    stack.pop()
                else:
                    stack.append(ch)
            
            return "".join(stack), points
        
        if y > x:
            first = "ba"
            second = "ab"
            x, y = y, x
        else:
            first = "ab"
            second = "ba"

        after_remove, point = remove(s, first, x)
        removed, points = remove(after_remove, second, y)
        return point + points