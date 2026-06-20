class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int):
        l, r = 0, len(arr) - 1
        idx = 0

        # binary search pivot
        while l <= r:
            m = (l + r) // 2
            if arr[m] <= x:
                idx = m
                l = m + 1
            else:
                r = m - 1

        l = idx
        r = idx + 1

        less = []
        greater = []

        while len(less) + len(greater) < k:
            if l >= 0 and (r >= len(arr) or x - arr[l] <= arr[r] - x):
                less.append(arr[l])
                l -= 1
            else:
                greater.append(arr[r])
                r += 1

        return list(reversed(less)) + greater