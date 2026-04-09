class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        dotDirectory = 0

        def pop_directory():
            # remove trailing slash
            if stack and stack[-1] == "/":
                stack.pop()
            # remove directory name
            while stack and stack[-1] != "/":
                stack.pop()
            # remove leading slash of that directory
            if stack:
                stack.pop()

        for i, c in enumerate(path):
            if c == ".":
                dotDirectory += 1
                continue

            # resolve dot sequence when it ends
            if dotDirectory:
                if dotDirectory == 1:
                    pass  # current directory → no-op
                elif dotDirectory == 2:
                    pop_directory()
                else:
                    stack.append("." * dotDirectory)
                dotDirectory = 0

            if c == "/" and stack and stack[-1] == "/":
                continue

            stack.append(c)

        # resolve trailing dots
        if dotDirectory:
            if dotDirectory == 2:
                pop_directory()
            elif dotDirectory > 2:
                stack.append("." * dotDirectory)

        # cleanup trailing slash
        if len(stack) > 1 and stack[-1] == "/":
            stack.pop()

        return "".join(stack) if stack else "/"
