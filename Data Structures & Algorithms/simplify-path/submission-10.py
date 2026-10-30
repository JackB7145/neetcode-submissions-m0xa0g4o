class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        newPath = []
        for string in path:
            if not string or string == ".":
                continue

            elif string == ".." and newPath:
                    newPath.pop() 
            elif string != "..":
                newPath.append(string)


        return '/'+'/'.join(newPath)