class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for n in asteroids:
            if n > 0 or not stack:
                stack.append(n)
                continue
        
            while stack and abs(n) > abs(stack[-1]) and stack[-1] > 0:
                stack.pop()

            if stack and stack[-1] == -n:
                stack.pop()
                continue

            if not stack or stack[-1] < 0:
                stack.append(n)

        return stack