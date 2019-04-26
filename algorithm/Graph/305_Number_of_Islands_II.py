class DSU(object):
    def __init__(self, nrows, ncols):
        self.count = 0
        self.par = [-1] * (nrows * ncols)
        self.rnk = [0] * (nrows * ncols)

    def isLand(self, idx):
        return self.par[idx] != -1

    def setLand(self, idx):
        self.par[idx] = idx # initialize parent to itself
        self.count += 1

    # path compression, continously reassign parent to root
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x] # or return x

    # union by rank, attach small tree as substree to larger tree
    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr == yr:
            return # already same cluster

        # if belong to distinct cluster
        if self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        elif self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr
        else: # same rank, different cluster
            self.par[yr] = xr
            self.rnk[xr] += 1
        self.count -= 1

class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        if m == 0 or n == 0:
            return 0

        ans = []

        nrows = m
        ncols = n

        dsu = DSU(nrows, ncols)
        for r, c in positions:
            dsu.setLand(r * ncols + c)

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                candr = r + dr
                candc = c + dc

                if 0 <= candr < nrows and 0 <= candc < ncols and dsu.isLand(candr * ncols + candc):
                    # convert 2D matrix to 1D array here
                    dsu.union(r * ncols + c, candr * ncols + candc)

            ans.append(dsu.count)
        return ans

solver = Solution()
solver.numIslands2(3, 3, [[0,0],
                          [0,1],
                          [1,2],
                          [2,1]])