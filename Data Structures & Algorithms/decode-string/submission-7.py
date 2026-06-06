class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            
            else:
                temp = ""
                while stack and stack[-1] != "[":
                    temp = stack.pop() + temp
                    
                stack.pop() #assuming this one is the opening bracket
                
                val = ""
                while stack and len(stack[-1]) == 1 and ord("0") <= ord(stack[-1]) <= ord("9"):
                    val = stack.pop() + val

                stack.append(int(val) * temp)
        
        return "".join(stack)

                
                