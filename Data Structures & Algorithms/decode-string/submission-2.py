class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c == ']':
                parts = []
                num = ""
                while stack and stack[-1] != '[':
                    parts.append(stack.pop())
                stack.pop()
                while stack and stack[-1].isdigit():
                    num += stack.pop()
                cur = "".join(reversed(parts))
                stack.append(cur * int(num[::-1]))
            else:
                stack.append(c)
        return "".join(stack)
        