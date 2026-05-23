class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = {0:1}

        cnt = 0

        res = 0
        for i in range(len(nums)):
            cnt += nums[i]
            if cnt - k in mp:
                res += mp[cnt-k]

            mp[cnt] = mp.get(cnt, 0) + 1
        
        return res

            