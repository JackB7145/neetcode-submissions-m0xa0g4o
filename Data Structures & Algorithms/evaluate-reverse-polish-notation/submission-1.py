class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in ["+", "-", "/", "*"]:
                stack.append(int(t))
            else:
                one = stack.pop()
                two = stack.pop()
                if t == "+":
                    stack.append(one + two)
                elif t == "-":
                    stack.append(two - one)
                elif t == "/":
                    stack.append(two // one)
                else:
                    stack.append(one * two)


        return stack[0]
            
