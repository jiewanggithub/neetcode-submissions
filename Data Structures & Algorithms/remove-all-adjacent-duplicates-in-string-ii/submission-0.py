class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for i in range(len(s)):
            if stack and stack[-1][0] == k - 1 and stack[-1][1] == s[i]:
                stack.pop()
            elif stack and stack[-1][1] == s[i]:
                stack[-1][0] += 1
            else:
                stack.append([1, s[i]])
        return "".join(ch * amount for amount, ch in stack)
