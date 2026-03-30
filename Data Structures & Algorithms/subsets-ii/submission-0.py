class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        res = []
        def dfs(idx, path):
            path = path.copy()
            if idx >= len(nums):
                path.sort()
                if ''.join(str(x) for x in path) not in seen:
                    seen.add(''.join(str(x) for x in path))
                    res.append(path)

            else:
                path.append(nums[idx])
                dfs(idx+1, path)
                path.pop()
                dfs(idx+1, path)
        dfs(0, [])
        return res