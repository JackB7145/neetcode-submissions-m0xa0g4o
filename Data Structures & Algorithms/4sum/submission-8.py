class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        for aa in range(len(nums) - 3):
            if aa > 0 and nums[aa] == nums[aa - 1]:
                continue

            for ab in range(aa + 1, len(nums) - 2):
                if ab > aa + 1 and nums[ab] == nums[ab - 1]:
                    continue

                l, r = ab + 1, len(nums) - 1

                while l < r:
                    total = nums[aa] + nums[ab] + nums[l] + nums[r]

                    if total == target:
                        res.append([nums[aa], nums[ab], nums[l], nums[r]])
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