class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def isPossible(largestAllowed):
            cnt = 0
            sub = 1
            for n in nums:
                if cnt + n > largestAllowed:
                    cnt = n
                    sub += 1
                else:
                    cnt += n
            return sub <= k

        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            m = (l + r) // 2
            if isPossible(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res