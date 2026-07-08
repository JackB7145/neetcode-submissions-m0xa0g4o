class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)

        def build(x, y, size):
            # Check if all values in this square are the same
            first = grid[x][y]
            is_uniform = True

            for i in range(x, x + size):
                for j in range(y, y + size):
                    if grid[i][j] != first:
                        is_uniform = False
                        break
                if not is_uniform:
                    break

            # If uniform → leaf node
            if is_uniform:
                return Node(first == 1, True, None, None, None, None)

            # Otherwise split into 4 quadrants
            half = size // 2

            topLeft = build(x, y, half)
            topRight = build(x, y + half, half)
            bottomLeft = build(x + half, y, half)
            bottomRight = build(x + half, y + half, half)

            return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)

        return build(0, 0, n)