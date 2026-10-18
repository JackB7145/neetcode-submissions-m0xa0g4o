class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[]for _ in range(len(nums)+1)]

        mp = Counter(nums)
        for n in mp:
            buckets[mp[n]].append(n)

        res = []
        for i in range(len(buckets)-1, -1, -1):
            for j in range(len(buckets[i])):
                if len(res) == k:
                    return res
                res.append(buckets[i][j])
        
        return res