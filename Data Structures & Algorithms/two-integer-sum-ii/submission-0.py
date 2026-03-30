class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lP = 0
        rP = len(numbers)-1
        while lP < rP:
            leftNum = numbers[lP]
            rightNum = numbers[rP]

            total = leftNum + rightNum

            if total == target:
                return [lP + 1, rP + 1]

            elif total > target:
                rP -= 1
            
            else:
                lP +=1
            