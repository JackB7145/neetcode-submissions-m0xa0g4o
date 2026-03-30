class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = {}
        def findChain(number, count):
            if numbers[number] not in numbers:
                return count
            else:
                return findChain(numbers[number], count+1)
        
        for i in nums:
            numbers[i] = i + 1
        
        longest = 0
        for num in nums:
            temp = findChain(num, 1)
            if temp > longest:
                longest = temp
        
        return longest

        