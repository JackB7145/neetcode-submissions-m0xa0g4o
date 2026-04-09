class Solution:
    def simplifyPath(self, path: str) -> str:
        dotDirectory = 0
        stack = []
        for c in path:
            print(dotDirectory, c)
            if c == ".":
                dotDirectory += 1
                continue

            if c.isalnum() or c == "/":
                if dotDirectory > 2:
                    stack.append("."*dotDirectory)
                elif dotDirectory == 2:
                    stack.pop()
                    stack.pop()
                    stack.pop()
                elif dotDirectory == 1:
                    stack.pop()
                dotDirectory = 0
            
            if c == "/" and stack and stack[-1] == "/":
                continue
            
            stack.append(c)
        
        if stack[-1] == "/":
            stack.pop()
        
        print(stack)

        "".join(stack)