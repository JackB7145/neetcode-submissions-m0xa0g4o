class MinStack:

    def __init__(self):
        self.stack = []
        self.smallest = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.smallest or self.smallest and val <= self.smallest[-1]:
            self.smallest.append(val)
        

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.smallest[-1]:
            self.smallest.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.smallest[-1]
