class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            print(token)
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token)) 
            else:
                if token == "+":
                    total = 0
                    while stack:
                        total += stack.pop()
                    stack.append(total)
                elif token == "-":
                    total = 0
                    while stack:
                        total -= stack.pop()
                    stack.append(-total)
                elif token == "*":
                    total = 1
                    while stack:
                        total *= stack.pop()
                    stack.append(total)
                else:
                    total = 1
                    print(f'Here {token}')
                    while stack:
                        numerator = stack.pop()
                        denominator = stack.pop()
                        total *= numerator // denominator
                    stack.append(total)
        return stack[0]

            
