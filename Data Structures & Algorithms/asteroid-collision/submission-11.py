class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for n in asteroids:
            if n > 0 or not stack and n < 0:
                stack.append(n)
            else:
                if stack[-1] <= 0:
                    stack.append(n)
                    continue
                while stack and not stack[-1] <= 0 and stack[-1] < -n:
                    stack.pop()
                if not stack or stack and stack[-1] < 0:
                    stack.append(n)
                elif -stack[-1] == n:
                    stack.pop()

        return stack
                
