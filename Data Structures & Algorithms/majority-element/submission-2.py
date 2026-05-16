class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        number = float('inf')
        cnt = 1
        for n in nums:
            if n == number:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    cnt = 1
                    number = n
        return number