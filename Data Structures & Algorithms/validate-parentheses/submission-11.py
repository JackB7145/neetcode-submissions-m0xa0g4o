class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        for c in s:
            if c in mp:
                if not stack or mp[c] != stack.pop():
                    return False
            else:
                stack.append(c)
        return not stack
            