class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def search(r, c, grid):
            # mark as visited
            grid[r][c] = 0

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                candr = r + dr
                candc = c + dc
                if 0 <= candr < len(grid) and 0 <= candc < len(grid[0]) and grid[candr][candc] == "1":
                    search(candr, candc, grid)
            # # left
            # if r - 1 >= 0 and grid[r - 1][c] == "1":
            #     search(r - 1, c, grid)
            # # up
            # if c - 1 >= 0 and grid[r][c - 1] == "1":
            #     search(r, c - 1, grid)
            # # down
            # if r + 1 < len(grid) and grid[r + 1][c] == "1":
            #     search(r + 1, c, grid)
            # # right
            # if c + 1 < len(grid[0]) and grid[r][c + 1] == "1":
            #     search(r, c + 1, grid)

        n = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    n += 1
                    search(r, c, grid)

        return n