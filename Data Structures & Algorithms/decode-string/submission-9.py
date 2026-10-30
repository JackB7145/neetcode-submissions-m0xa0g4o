class Solution:
    def decodeString(self, s: str) -> str:
        stack = []          # (string built before '[', repeat count)
        current = ""
        num = 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "[":
                stack.append((current, num))
                current, num = "", 0
            elif c == "]":
                prev, k = stack.pop()
                current = prev + current * k
            else:
                current += c
        return current