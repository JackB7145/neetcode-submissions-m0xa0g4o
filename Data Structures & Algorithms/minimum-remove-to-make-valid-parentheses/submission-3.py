class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s = list(s)  # convert to list so we can modify
        
        for i in range(len(s)):
            if s[i] == "(":
                stack.append((s[i], i))
            
            elif s[i] == ")":
                if stack and stack[-1][0] == "(":
                    stack.pop()
                else:
                    stack.append((s[i], i))

        # remove from end → avoids shifting issues
        for _, idx in reversed(stack):
            s.pop(idx)

        return "".join(s)