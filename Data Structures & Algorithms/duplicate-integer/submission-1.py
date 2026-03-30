class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers = defaultdict(int)
        for i in nums:
            numbers[i] += 1
            if numbers[i] == 2:
                return True
        return False