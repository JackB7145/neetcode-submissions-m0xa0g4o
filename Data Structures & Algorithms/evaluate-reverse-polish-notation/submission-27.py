class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for n in tokens:
            if n == "+":
                one, two = stack.pop(), stack.pop()
                stack.append(one+two)
            elif n == "*":
                one, two = stack.pop(), stack.pop()
                stack.append(one*two)
            elif n == "-":
                one, two = stack.pop(), stack.pop()
                stack.append(two-one)

            elif n == "/":
                one, two = stack.pop(), stack.pop()
                val = two/one if not [one, two] in [[0, two], [one, 0]] else 0
                stack.append(int(val))

            else:
                stack.append(int(n))
        
        return int(stack[0])