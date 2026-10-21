class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close = {'[': ']', '{': '}', '(': ')'}
        stack = []

        for char in s:
            if stack and open_to_close.get(stack[-1]) == char:
                stack.pop()
            else:
                stack.append(char)
        
        return not stack
        