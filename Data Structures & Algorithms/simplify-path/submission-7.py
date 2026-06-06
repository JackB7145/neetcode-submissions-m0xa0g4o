class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")

        for directory in path:
            if directory == "..":
                if stack:
                    stack.pop() 
                continue
            
            if directory == "" or directory == ".":
                continue

            stack.append(directory)
        
        return "/" + "/".join(stack)

