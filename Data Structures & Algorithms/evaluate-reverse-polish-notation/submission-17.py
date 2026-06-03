class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = set(["+", "-", "*", "/"])
        for c in tokens:
            print(stack, c)
            if c not in operations:
                stack.append(int(c))

            else:
                if c == "+":
                    stack.append(stack.pop() + stack.pop())
                elif c == "-":
                    stack.append(-1 * (stack.pop()-stack.pop()))
                elif c == "*":
                    stack.append(stack.pop() * stack.pop())
                else:
                    val = (1/stack.pop()*stack.pop())
                    print(val)
                    stack.append(int(val))
        
        return stack[-1]

        #[22]