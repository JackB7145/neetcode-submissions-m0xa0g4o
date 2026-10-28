class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)

        for i, v in enumerate(temperatures):
            while stack and stack[-1][0] < v:
                _, idx = stack.pop()
                res[idx] = i-idx 
            if not stack or stack[-1][0] >= v:
                stack.append((v, i))
        
        return res