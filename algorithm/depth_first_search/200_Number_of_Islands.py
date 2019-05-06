class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(r, c, grid):
            # mark as visited
            grid[r][c] = 0
            inBound = lambda r, c: 0 <= r < len(grid) and 0 <= c < len(grid[0])
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                rr = r + dr
                cc = c + dc
                if inBound(rr, cc) and grid[rr][cc] == "1":
                    dfs(rr, cc, grid)

        n = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    n += 1
                    dfs(r, c, grid)

        return n
