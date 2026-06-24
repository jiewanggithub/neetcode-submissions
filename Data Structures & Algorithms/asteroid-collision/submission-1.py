class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            while stack and stack[-1] > 0 and ast < 0:
                diff = stack[-1] + ast
                if diff == 0:
                    ast = 0
                    stack.pop()
                elif diff < 0:
                    stack.pop()
                elif diff > 0:
                    ast = 0
            if ast:
                stack.append(ast)
        return stack
        