class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        diff = 1
        while self.stack and self.stack[-1][0] <= price:
            diff += self.stack.pop()[1]
        self.stack.append((price, diff))
        return diff


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)