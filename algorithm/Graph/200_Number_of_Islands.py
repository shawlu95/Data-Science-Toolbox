class DSU(object):
    def __init__(self, grid):
        nrows = len(grid)
        ncols = len(grid[0])

        self.par = [-1] * (nrows * ncols)
        self.rnk = [0] * (nrows * ncols)
        self.count = 0

        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == "1":
                    self.par[r * ncols + c] = r * ncols + c
                    self.count += 1

    # path compression, continously reassign parent to root
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    # union by rank, attach small tree as substree to larger tree
    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return
        elif self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr
        else:
            self.par[yr] = xr
            self.rnk[xr] += 1
        self.count -= 1

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        nrows = len(grid)
        ncols = len(grid[0])

        dsu = DSU(grid)
        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == '1':
                    grid[r][c] = '0'
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        candr = r + dr
                        candc = c + dc

                        if 0 <= candr < nrows and 0 <= candc < ncols and grid[candr][candc] == '1':
                            dsu.union(r * ncols + c, candr * ncols + candc)
        print(dsu.count)
        return dsu.count


class BFS_Solution:
    def numIslands(self, grid: 'List[List[str]]') -> 'int':
        # empty array
        if not grid or not grid[0]:
            return 0

        # use BFS
        nr, nc = len(grid), len(grid[0])

        island = 0

        def clear_island(r, c, gird):
            grid[r][c] = "0"
            queue = [(r, c)]
            while queue:
                r, c = queue.pop()  # reassign r, c here!
                for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                    cr, cc = r + dr, c + dc
                    if 0 <= cr < nr and 0 <= cc < nc and grid[cr][cc] == "1":
                        queue.append((cr, cc))
                        grid[cr][cc] = "0"

        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    # add island, start BFS
                    island += 1
                    clear_island(r, c, grid)

        return island


class DFS_Solution:
    def numIslands(self, grid: 'List[List[str]]') -> 'int':
        # empty array
        if not grid or not grid[0]:
            return 0

        # use DFS
        nr, nc = len(grid), len(grid[0])

        island = 0

        def clear_island(r, c):
            grid[r][c] = "0"
            for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                cr, cc = r + dr, c + dc
                if 0 <= cr < nr and 0 <= cc < nc and grid[cr][cc] == "1":
                    clear_island(cr, cc)

        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    # add island, start DFS
                    island += 1
                    clear_island(r, c)

        return island


solver = Solution()
solver.numIslands([["1","1","1","1","0"],
                   ["1","1","0","1","0"],
                   ["1","1","0","0","0"],
                   ["0","0","0","0","0"]])


