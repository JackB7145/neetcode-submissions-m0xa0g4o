class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        '''
        Keep track of the astroids moving right in a stack. If its going right, load it up, if its going left, and there

        is something in the stack we make a comparion. if that astaroid going left is larger than the one going right we pop unitl thats done



        '''

        stack = []
        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:
                if not stack or stack[-1] < 0:
                    stack.append(a)
                    continue

                while stack and abs(a) > stack[-1]:
                    stack.pop()
                
                if stack and stack[-1] == abs(a):
                    stack.pop()
            
        return stack