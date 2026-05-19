class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        freq = [[] for _ in range(max(c.values()))]

        for num in c:
            freq[c[num]-1].append(num)

        res = []
        for i in range(len(freq)-1, -1, -1):
            for item in freq[i]:
                res.append(item)
                if len(res) >= k:
                    return res

    