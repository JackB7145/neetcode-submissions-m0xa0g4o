class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        candidates = [0, 0, 0]

        for i, j, k in triplets:
            if i == target[0]:
                if j > target[1] or k > target[2]:
                    continue
                else:
                    candidates[0] += 1
            if j == target[1]:
                if i > target[0] or k > target[2]:
                    continue
                else:
                    candidates[1] += 1

            if k == target[2]:
                if i > target[0] or j > target[1]:
                    continue
                else:
                    candidates[2] += 1

        return not 0 in candidates