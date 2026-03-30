class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        if not s:
            return False
        for i in s:
            if i in [']', '}', ')']:
                
                temp = stack.pop() if stack else False
                if i == ']' and temp == "[":
                    pass
                elif i == '}' and temp == "{":
                    pass
                elif i == ')' and temp == "(":
                    pass
                else:
                    return False
            else:
                stack.append(i)
        if stack:
            return False
        return True