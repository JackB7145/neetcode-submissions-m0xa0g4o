class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        largest = max(nums)
        total = nums[0]
        lastIdx = 0
        for i in range(1, len(nums)):
            if nums[i] >= total and total < 0:
                total = nums[i]
                lastIdx = i
            else:
                total += nums[i]
            
            largest = max(largest, total)

        cnt = 0

        print(lastIdx, total)

        while cnt < lastIdx:
            print(total)
            if nums[cnt] > total and total < 0:
                return largest
            else:
                print(f'Adding {nums[cnt]} to {total}')
                total += nums[cnt]

            
            cnt += 1
            largest = max(largest, total)

        return largest        

        