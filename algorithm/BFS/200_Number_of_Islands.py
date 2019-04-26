class DU(object):
    def __init__(self, n):
        self.count = 0
        self.parent = [-1] * n
        self.rank = [0] * n

    def isLand(self, idx):
        return self.parent[idx] != -1

    def setLand(self, idx):
        self.parent[idx] = idx  # initialize parent to itself
        self.count += 1

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]  # DO NOT RETURN x

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)

        if xr == yr:
            return

        if self.rank[xr] < self.rank[yr]:
            self.parent[xr] = yr  # setting parent of ROOT
        elif self.rank[xr] > self.rank[yr]:
            self.parent[yr] = xr  # setting parent of ROOT
        else:
            self.parent[xr] = yr  # setting parent of ROOT
            self.rank[yr] += 1
        self.count -= 1


class Solution2:
    def numIslands(self, grid: 'List[List[str]]') -> 'int':
        # empty array
        if not grid or not grid[0]:
            return 0

        nr, nc = len(grid), len(grid[0])
        du = DU(nr * nc)
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    du.setLand(r * nc + c)
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        candr = r + dr
                        candc = c + dc

                        if 0 <= candr < nr and 0 <= candc < nc and du.isLand(candr * nc + candc):
                            du.union(r * nc + c, candr * nc + candc)
        return du.count


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

        n = 0
        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == "1":
                    n += 1

                    queue = []
                    queue.append((r, c))
                    while queue:
                        print(queue)
                        node = queue.pop(0)
                        grid[node[0]][node[1]] = "0"
                        if node[0] - 1 >= 0 and grid[node[0] - 1][node[1]] == '1' and (node[0] - 1, node[1]) not in queue:
                            queue.append((node[0] - 1, node[1]))
                        if node[0] + 1 < nrows and grid[node[0] + 1][node[1]] == '1' and (node[0] + 1, node[1]) not in queue:
                            queue.append((node[0] + 1, node[1]))
                        if node[1] - 1 >= 0 and grid[node[0]][node[1] - 1] == '1' and (node[0], node[1] - 1) not in queue:
                            queue.append((node[0], node[1] - 1))
                        if node[1] + 1 < ncols and grid[node[0]][node[1] + 1] == '1' and (node[0], node[1] + 1) not in queue:
                            queue.append((node[0], node[1] + 1))

        print(n)
        return n

solver = Solution()
solver.numIslands([["1","1","1","1","0"],
                   ["1","1","0","1","0"],
                   ["1","1","0","0","0"],
                   ["0","0","0","0","0"]])