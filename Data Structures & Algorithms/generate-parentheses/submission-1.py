class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        def generateBrackets(string, n):
            
            if n == 0:
                print(string, validateBrackets(string))
                if validateBrackets(string):
                    stack.append(string)
                    return 
                return 
            else:
                generateBrackets(string + '(', n-1)
                generateBrackets(string + ')', n-1)                

        def validateBrackets(brackets):
            stack1 = []
            if not brackets:
                return False
            for i in brackets:
                if i == ")":
                    if stack1 and stack1.pop() == "(":
                        pass
                    else:
                        return False
                else:
                    stack1.append(i)
            print(stack1)
            return True if not stack1 else False
        
        generateBrackets('', n*2)
        return stack
        
