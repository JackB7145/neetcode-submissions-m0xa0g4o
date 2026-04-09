class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        dotDirectory = 0

        def pop_directory():
            if stack and stack[-1] == "/":
                stack.pop()
            while stack and stack[-1] != "/":
                stack.pop()
            if stack:
                stack.pop()

        for i, c in enumerate(path):
            if c == ".":
                dotDirectory += 1
                continue

            # resolve dots ONLY if segment ends
            if dotDirectory:
                if c == "/" or not c.isalnum():
                    if dotDirectory == 1:
                        pass
                    elif dotDirectory == 2:
                        pop_directory()
                    else:
                        stack.append("." * dotDirectory)
                else:
                    # dots are part of a name
                    stack.append("." * dotDirectory)

                dotDirectory = 0

            if c == "/" and stack and stack[-1] == "/":
                continue

            stack.append(c)

        # handle trailing dots
        if dotDirectory:
            if dotDirectory == 2:
                pop_directory()
            else:
                stack.append("." * dotDirectory)

        if len(stack) > 1 and stack[-1] == "/":
            stack.pop()

        return "".join(stack) if stack else "/"
