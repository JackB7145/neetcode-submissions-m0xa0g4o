class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        '''

        Keep track of a global max, and while we iterate over the data set we

        keep track of the longest increasing path, making it top down dp since the solution for each is memoized?

        you traverse in a direction that is larger, and you keep track of the answer everywhere, then do a separate run through findng the max

        '''

        cache = {}
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]

            res = 0
            for dx, dy in dirs:
                newI = i + dy
                newJ = j + dx
                if 0 <= newI < len(matrix) and 0 <= newJ < len(matrix[0]) and matrix[newI][newJ] > matrix[i][j]:
                    res = max(res, 1 + dfs(newI, newJ))

            cache[(i, j)] = res
            return res
        
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, 1 + dfs(i, j))
        
        return res



