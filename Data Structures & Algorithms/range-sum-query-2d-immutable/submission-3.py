class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        for i in range(len(self.matrix)):
            rowCount = 0
            for j in range(len(self.matrix[0])):
                temp = self.matrix[i][j]
                self.matrix[i][j] += rowCount
                self.matrix[i][j] += self.matrix[i-1][j] if 0 < i else 0
                rowCount += temp

        for row in self.matrix:
            print(row)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.matrix[row2][col2]

        topSegment = self.matrix[row1-1][col2] if 0 <= row1-1 and 0 <= col2 else 0
        leftSegment = self.matrix[row2][col1-1] if 0 <= row2 and 0 <= col1-1 else 0
        adjustedLeftSegment = leftSegment - self.matrix[row1-1][col1-1] if 0 <= row1-1 and 0 <= col1-1 else leftSegment

        return total - topSegment - adjustedLeftSegment


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)