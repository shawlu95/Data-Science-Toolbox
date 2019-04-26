class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        if not grid:
            return ans

        ans = 0

        def dfs(grid, r, c):
            if grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            ds = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            s = 1
            for delr, delc in ds:
                if 0 <= r + delr < len(grid) and 0 <= c + delc < len(grid[0]):
                    s += dfs(grid, r + delr, c + delc)
            return s

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    tmp = dfs(grid, r, c)
                    # print(tmp)
                    ans = max(tmp, ans)
        # print(ans)
        return ans

    def maxAreaOfIslandRec(self, grid):
        seen = set()

        def area(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                    and (r, c) not in seen and grid[r][c]):
                return 0
            seen.add((r, c))
            return (1 + area(r + 1, c) + area(r - 1, c) +
                    area(r, c - 1) + area(r, c + 1))

        return max(area(r, c)
                   for r in range(len(grid))
                   for c in range(len(grid[0])))

    def maxAreaOfIslandIter(self, grid):
        seen = set()
        ans = 0
        for r0, row in enumerate(grid):
            for c0, val in enumerate(row):
                if val and (r0, c0) not in seen:
                    shape = 0
                    stack = [(r0, c0)]
                    seen.add((r0, c0))
                    while stack:
                        r, c = stack.pop()
                        shape += 1
                        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                            if (0 <= nr < len(grid) and 0 <= nc < len(grid[0])
                                    and grid[nr][nc] and (nr, nc) not in seen):
                                stack.append((nr, nc))
                                seen.add((nr, nc))
                    ans = max(ans, shape)
        return ans





solver = Solution()
solver.maxAreaOfIsland(
    [[0,0,1,0,0,0,0,1,0,0,0,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,1,1,0,1,0,0,0,0,0,0,0,0],
     [0,1,0,0,1,1,0,0,1,0,1,0,0],
     [0,1,0,0,1,1,0,0,1,1,1,0,0],
     [0,0,0,0,0,0,0,0,0,0,1,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,0,0,0,0,0,0,1,1,0,0,0,0]]
)