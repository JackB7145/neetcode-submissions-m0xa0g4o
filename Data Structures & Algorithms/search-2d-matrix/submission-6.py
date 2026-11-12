class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        while l <= r:
            m = (l+r)//2
            if matrix[m][0] <= target <= matrix[m][-1]:
                #Binary Search
                idx = m
                l, r = 0, len(matrix[idx])-1
                while l <= r:
                    m = (l+r)//2
                    if matrix[idx][m] == target:
                        return True
                    
                    elif matrix[idx][m] < target:
                        l = m + 1
                    
                    else:
                        r = m - 1

                return False
            elif target < matrix[m][0]:
                r = m - 1
            
            else:
                l = m + 1
        
        return False
