class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        offset = 10**4  # shift to avoid negative index (problem constraint)
        size = 2 * 10**4 + 1

        buckets = [[] for _ in range(size)]

        for n in arr:
            d = abs(n - x)
            buckets[d].append(n)

        res = []

        for d in range(size):
            if buckets[d]:
                for n in sorted(buckets[d]):  # tie-break inside same distance
                    res.append(n)
                    if len(res) == k:
                        return sorted(res)