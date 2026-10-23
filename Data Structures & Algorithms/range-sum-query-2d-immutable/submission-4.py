class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.b = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            cnt = 0
            for j in range(len(matrix[0])):
                top = self.b[i-1][j] if i - 1 >= 0 else 0
                self.b[i][j] = cnt + top + matrix[i][j]
                cnt += matrix[i][j]

        for row in self.b:
            print(row)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.b[row2][col2]
        top = self.b[row1-1][col2] if row1-1 >= 0 else 0
        left = self.b[row2][col1-1] if row2 >= 0 and col1-1 >= 0 else 0
        diff = self.b[row1-1][col1-1] if row1-1>=0 and col1-1 >= 0 else 0

        total -= (top + left - diff)

        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)