class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []

        for n in arr:
            res.append((x - n, n))

        res.sort(key=lambda x: (abs(x[0]), x[1]))

        res = [res[i][1] for i in range(k)]

        return sorted(res)