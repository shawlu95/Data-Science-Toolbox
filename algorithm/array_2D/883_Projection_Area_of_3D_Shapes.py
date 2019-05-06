class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        row_max = grid[0] # first row
        col_max = [grid[i][0] for i in range(len(grid))] # first col
        bottom = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0: bottom += 1
                row_max[c] = max(row_max[c], grid[r][c])
                col_max[r] = max(col_max[r], grid[r][c])
        return bottom + sum(row_max) + sum(col_max)
                