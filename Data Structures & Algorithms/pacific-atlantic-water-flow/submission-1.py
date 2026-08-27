class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        pacific = set()
        atlantic = set()

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def traverse(i, j, visited):
            if (i, j) in visited:
                return

            visited.add((i, j))

            for dx, dy in dirs:
                nX, nY = i + dx, j + dy

                if (
                    0 <= nX < ROWS
                    and 0 <= nY < COLS
                    and heights[nX][nY] >= heights[i][j]
                ):
                    traverse(nX, nY, visited)

        # Pacific: top row + left column
        for j in range(COLS):
            traverse(0, j, pacific)

        for i in range(ROWS):
            traverse(i, 0, pacific)

        # Atlantic: bottom row + right column
        for j in range(COLS):
            traverse(ROWS - 1, j, atlantic)

        for i in range(ROWS):
            traverse(i, COLS - 1, atlantic)

        # Cells reachable from both oceans
        return [list(cell) for cell in pacific & atlantic]