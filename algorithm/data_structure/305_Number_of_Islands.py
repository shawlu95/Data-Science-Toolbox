class DSU(object):
    def __init__(self, nrows, ncols):
        self.count = 0
        self.par = [-1] * (nrows * ncols)
        self.rnk = [0] * (nrows * ncols)

    def isLand(self, idx):
        return self.par[idx] >= 0

    def setLand(self, idx):
        self.par[idx] = idx
        self.count += 1

    # path compression, continously reassign parent to root
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    # union by rank, attach small tree as substree to larger tree
    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)

        # if already union, do nothing
        if xr == yr:
            return
        elif self.rnk[xr] < self.rnk[yr]:
            # if x tree is smaller, attach x tree to y root
            self.par[xr] = yr
        elif self.rnk[xr] > self.rnk[yr]:
            # if y tree is smaller, attach y tree to x root
            self.par[yr] = xr
        else:
            # if tie, attach y tree to x root
            # increment x root's rank
            self.par[yr] = xr
            self.rnk[xr] += 1
        self.count -= 1

class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]] position of lands to be added
        :rtype: List[int] return a list of number of islands as lands get added
        """
        if m == 0 or n == 0:
            return 0

        ans = []

        nrows = m
        ncols = n

        # initialize
        dsu = DSU(nrows, ncols)

        # everytime a new land is added, check if its neighbor is land
        # union with each neighboring land, if successful, decrease island count
        for r, c in positions:
            dsu.setLand(r * ncols + c)

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                candr = r + dr
                candc = c + dc

                if 0 <= candr < nrows and 0 <= candc < ncols and dsu.isLand(candr * ncols + candc):
                    dsu.union(r * ncols + c, candr * ncols + candc)

            ans.append(dsu.count)
        return ans