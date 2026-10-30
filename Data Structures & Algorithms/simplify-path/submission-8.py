class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        newPath = []
        for string in path:
            string = string.replace('/', '')
            if not string:
                continue

            if string == ".":
                continue
            elif string == "..":
                if newPath:
                    newPath.pop() 
            else:
                newPath.append(string)


        return '/'+'/'.join(newPath)