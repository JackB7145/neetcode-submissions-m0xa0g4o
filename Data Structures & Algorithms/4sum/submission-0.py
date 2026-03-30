class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for a1 in range(n - 3):
            if a1 > 0 and nums[a1] == nums[a1 - 1]:
                continue

            for a2 in range(a1 + 1, n - 2):
                if a2 > a1 + 1 and nums[a2] == nums[a2 - 1]:
                    continue

                l, r = a2 + 1, n - 1

                while l < r:
                    total = nums[a1] + nums[a2] + nums[l] + nums[r]

                    if total == target:
                        res.append([nums[a1], nums[a2], nums[l], nums[r]])
                        l += 1
                        r -= 1

                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1

                    elif total < target:
                        l += 1
                    else:
                        r -= 1

        return res
