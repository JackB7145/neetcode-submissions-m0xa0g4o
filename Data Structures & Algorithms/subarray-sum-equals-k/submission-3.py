class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0: 1}          # empty prefix
        cnt = 0
        res = 0
        for n in nums:
            cnt += n
            res += seen.get(cnt - k, 0)
            seen[cnt] = seen.get(cnt, 0) + 1
        return res