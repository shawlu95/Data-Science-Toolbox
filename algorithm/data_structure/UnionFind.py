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
