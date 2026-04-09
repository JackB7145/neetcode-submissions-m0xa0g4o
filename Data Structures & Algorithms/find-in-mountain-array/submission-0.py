class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        # 1) find peak index
        peak = 0
        for i in range(1, n - 1):
            if mountainArr.get(i - 1) < mountainArr.get(i) > mountainArr.get(i + 1):
                peak = i
                break

        # 2) binary search on left (increasing)
        l, r = 0, peak
        while l <= r:
            m = (l + r) // 2
            val = mountainArr.get(m)

            if val == target:
                return m
            elif val < target:
                l = m + 1
            else:
                r = m - 1

        # 3) binary search on right (decreasing)
        l, r = peak + 1, n - 1
        while l <= r:
            m = (l + r) // 2
            val = mountainArr.get(m)

            if val == target:
                return m
            elif val < target:
                r = m - 1
            else:
                l = m + 1

        return -1
