class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        '''
        Keep track of the astroids moving right in a stack. If its going right, load it up, if its going left, and there

        is something in the stack we make a comparion. if that astaroid going left is larger than the one going right we pop unitl thats done



        '''

        stack = []
        for a in asteroids:
            if not stack or stack and stack[-1] < 0 or a > 0:
                stack.append(a)
                continue

            while stack and a < 0 and stack[-1] > 0 and stack[-1] < abs(a):
                stack.pop()
            
            if stack and stack[-1] > 0 and stack[-1] == abs(a):
                stack.pop()
                continue
            
            if not stack or stack[-1] < 0:
                stack.append(a)
            
            
        return stack