class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            print(stack)
            if op == "+":
                res = stack[-1] + stack[-2]
                stack.append(res)
            elif op == "D":
                stack.append(stack[-1]*2)
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)