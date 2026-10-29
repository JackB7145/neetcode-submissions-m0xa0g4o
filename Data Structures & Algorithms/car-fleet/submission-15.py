class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []  # arrival times of fleet leaders
        for p, s in sorted(zip(position, speed)):
            t = (target - p) / s
            while stack and stack[-1] <= t:   # car behind would catch this one
                stack.pop()
            stack.append(t)
        return len(stack)