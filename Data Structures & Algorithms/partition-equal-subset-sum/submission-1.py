class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2

        cache = {}

        def dfs(idx, total):
            if total == target:
                return True

            if idx == len(nums) or total > target:
                return False

            if (idx, total) in cache:
                return cache[(idx, total)]

            # Take nums[idx]
            if dfs(idx + 1, total + nums[idx]):
                return True

            # Skip nums[idx]
            if dfs(idx + 1, total):
                return True

            cache[(idx, total)] = False
            return False

        return dfs(0, 0)
