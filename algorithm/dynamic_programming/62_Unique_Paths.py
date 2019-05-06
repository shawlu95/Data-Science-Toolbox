class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int nrows
        :type n: int ncols
        :rtype: int
        """
        grid = [[0 for i in range(n)] for j in range(m)]
        grid[0][0] = 1
        queue = [(0, 0)]
        while queue:
            loc = queue[0]
            del queue[0]

            srcU = 0
            if loc[0] - 1 >= 0:
                srcU = grid[loc[0] - 1][loc[1]]
            srcL = 0
            if loc[1] - 1 >= 0:
                srcL = grid[loc[0]][loc[1] - 1]
            grid[loc[0]][loc[1]] += (srcU + srcL)

            # append right
            if loc[1] + 1 < n:
                if (loc[0], loc[1] + 1) not in queue:
                    queue.append((loc[0], loc[1] + 1))

            # append down
            if loc[0] + 1 < m:
                if (loc[0] + 1, loc[1]) not in queue:
                    queue.append((loc[0] + 1, loc[1]))
        return grid[-1][-1]



solver = Solution()
print(solver.uniquePaths(7, 3))