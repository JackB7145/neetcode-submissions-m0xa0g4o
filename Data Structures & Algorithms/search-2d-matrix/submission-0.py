class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(row, target):
            print(row, target)
            left = 0
            right = len(row) - 1
            while left <= right:
                mid = (left+right) // 2
                if row[mid] == target:
                    return True
                if row[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return False



        lP = 0 
        rP = len(matrix) - 1

        while lP <= rP:
            mid = (lP + rP) // 2
            leftNum, rightNum = matrix[mid][0], matrix[mid][-1]
            if leftNum < target and rightNum > target:
                return search(matrix[mid], target)
            elif leftNum < target and rightNum < target:
                lP = mid + 1
            else:
                rP = mid - 1
        return False