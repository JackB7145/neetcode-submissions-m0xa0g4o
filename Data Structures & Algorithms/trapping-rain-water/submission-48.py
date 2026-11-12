class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0 for _ in range(n)]
        right = [0 for _ in range(n)]

        largest = 0
        for i in range(n):
            largest = max(height[i], largest)
            left[i] = largest

        largest = 0
        for i in range(n-1, -1, -1):
            largest = max(height[i], largest)
            right[i] = largest

        res = 0
        for i in range(n):
            res += min(left[i], right[i]) - height[i]


        return res

