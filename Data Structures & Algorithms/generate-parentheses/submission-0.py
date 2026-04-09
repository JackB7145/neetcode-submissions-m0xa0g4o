class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        def generateBrackets(string, n):
            if n == 0:
                if validateBrackets(string):
                    stack.append(string)
                    return 
                return 
            else:
                generateBrackets(string + '(', n-1)
                generateBrackets(string + ')', n-1)                

        def validateBrackets(brackets):
            stack1 = []
            if not stack1:
                return False
            for i in brackets:
                if i in '(':
                    stack1.append('(')
                else:
                    if stack1.pop() != "(":
                        return False
            return True
        
        generateBrackets('', n)
        return stack
        
