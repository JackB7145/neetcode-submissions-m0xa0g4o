class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        while l <= r:
            mid = (l+r)//2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                l, r = 0, len(matrix[0])-1
                while l <= r:
                    m = (l+r)//2
                    if matrix[mid][m] == target:
                        return True
                    elif matrix[mid][m] < target:
                        l = m + 1
                    else:
                        r = m - 1

                break
            elif matrix[mid][0] <= matrix[mid][-1] <= target:
                l = mid + 1
            else:
                r = mid - 1
            
        return False