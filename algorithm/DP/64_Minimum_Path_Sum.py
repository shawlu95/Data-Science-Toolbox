# top down, classic 2D O(mn) time, O(mn) space
# top down, 1-D O(mn) time, O(n) space
# top down, O(mn) time, O(1) space
# bottom up, classic 2D O(mn) time, O(mn) space
# bottom up, 1-D O(mn) time, O(n) space
# bottom up, O(mn) time, O(1) space
# left-right, classic 2D O(mn) time, O(mn) space
# left-right, 1-D O(mn) time, O(m) space
# left-right, O(mn) time, O(1) space
# right-left, classic 2D O(mn) time, O(mn) space
# right-left, 1-D O(mn) time, O(m) space
# right-left, O(mn) time, O(1) space
# BFS, starting with top left
# BFS, starting with bottom right

class Solution:
    # top down, classic 2D O(mn) time, O(mn) space
    def minPathSum1(self, grid):
        nrows = len(grid)
        ncols = len(grid[0])
        ans = [[0 for i in range(ncols)] for j in range(nrows)]

        for r in range(nrows):
            for c in range(ncols):
                if r == 0 and c > 0:
                    # top row
                    ans[r][c] = grid[r][c] + ans[r][c - 1]
                elif r > 0 and c == 0:
                    # left col
                    ans[r][c] = grid[r][c] + ans[r - 1][c]
                elif r > 0 and c > 0:
                    # everywhere else
                    ans[r][c] = grid[r][c] + min(ans[r - 1][c], ans[r][c - 1])
                else:
                    # top left corner
                    ans[r][c] = grid[r][c]
        return ans[-1][-1]

    # top down, 1-D O(mn) time, O(n) space
    def minPathSum2(self, grid):
        nrows = len(grid)
        ncols = len(grid[0])
        ans = [0 for i in range(ncols)]
        for r in range(nrows):
            for c in range(ncols):
                if r == 0 and c > 0:
                    # top row
                    ans[c] = grid[r][c] + ans[c - 1]
                elif r > 0 and c == 0:
                    # left col
                    ans[c] = grid[r][c] + ans[c]
                elif r > 0 and c > 0:
                    # everywhere else
                    ans[c] = grid[r][c] + min(ans[c], ans[c - 1])
                else:
                    # top left corner
                    ans[c] = grid[r][c]
        return ans[-1]

    # top down, O(mn) time, O(1) space
    def minPathSum3(self, grid):
        nrows = len(grid)
        ncols = len(grid[0])
        for r in range(nrows):
            for c in range(ncols):
                if r == 0 and c > 0:
                    # top row
                    grid[r][c] = grid[r][c] + grid[r][c - 1]
                elif r > 0 and c == 0:
                    # left col
                    grid[r][c] = grid[r][c] + grid[r - 1][c]
                elif r > 0 and c > 0:
                    # everywhere else
                    grid[r][c] = grid[r][c] + min(grid[r - 1][c], grid[r][c - 1])
        return grid[-1][-1]

    # bottom up, classic 2D O(mn) time, O(mn) space
    def minPathSum4(self, grid):
        nrows = len(grid)
        ncols = len(grid[0])
        ans = [[0 for i in range(ncols)] for j in range(nrows)]

        for r in range(nrows - 1, - 1, - 1):
            for c in range(ncols - 1, - 1, - 1):
                if r == nrows - 1 and c < ncols - 1:
                    # bottom row
                    ans[r][c] = grid[r][c] + ans[r][c + 1]
                elif r < nrows - 1 and c == ncols - 1:
                    # right col
                    ans[r][c] = grid[r][c] + ans[r + 1][c]
                elif r < nrows - 1 and c < ncols - 1:
                    # everywhere else
                    ans[r][c] = grid[r][c] + min(ans[r][c + 1], ans[r + 1][c])
                else:
                    # bottom right
                    ans[-1][-1] = grid[-1][-1]
        return ans[0][0]

    # bottom up, 1-D O(mn) time, O(n) space
    def minPathSum5(self, grid):
        nrows = len(grid)
        ncols = len(grid[0])
        ans = [0 for i in range(ncols)]

        for r in range(nrows - 1, - 1, - 1):
            for c in range(ncols - 1, - 1, - 1):
                if r == nrows - 1 and c < ncols - 1:
                    # bottom row
                    ans[c] = grid[r][c] + ans[c + 1]
                elif r < nrows - 1 and c == ncols - 1:
                    # right col
                    ans[c] = grid[r][c] + ans[c]
                elif r < nrows - 1 and c < ncols - 1:
                    # everywhere else
                    ans[c] = grid[r][c] + min(ans[c + 1], ans[c])
                else:
                    # bottom right
                    ans[-1] = grid[-1][-1]
        return ans[0]

    # bottom up, O(mn) time, O(1) space
    def minPathSum6(self, grid):
        nrows = len(grid)
        ncols = len(grid[0])

        for r in range(nrows - 1, - 1, - 1):
            for c in range(ncols - 1, - 1, - 1):
                if r == nrows - 1 and c < ncols - 1:
                    # bottom row
                    grid[r][c] = grid[r][c] + grid[r][c + 1]
                elif r < nrows - 1 and c == ncols - 1:
                    # right col
                    grid[r][c] = grid[r][c] + grid[r + 1][c]
                elif r < nrows - 1 and c < ncols - 1:
                    # everywhere else
                    grid[r][c] = grid[r][c] + min(grid[r][c + 1], grid[r + 1][c])
                else:
                    # bottom right corner
                    grid[-1][-1] = grid[-1][-1]
        return grid[0][0]

    # left-right, classic 2D O(mn) time, O(mn) space
    def minPathSum7(self, grid):
        nrows = len(grid)
        ncols = len(grid[0])

        ans = [[0 for i in range(ncols)] for j in range(nrows)]

        for c in range(ncols):
            for r in range(nrows):
                if r == 0 and c > 0:
                    # top row
                    ans[r][c] = grid[r][c] + ans[r][c - 1]
                elif r > 0 and c == 0:
                    # left col
                    ans[r][c] = grid[r][c] + ans[r - 1][c]
                elif r > 0 and c > 0:
                    # everywhere else
                    ans[r][c] = grid[r][c] + min(ans[r - 1][c], ans[r][c - 1])
                else:
                    # top left corner
                    ans[r][c] = grid[r][c]
        return ans[-1][-1]


    # left-right, 1-D O(mn) time, O(m) space
    def minPathSum8(self, grid):
        nrows = len(grid)
        ncols = len(grid[0])
        ans = [0 for i in range(nrows)]

        for c in range(ncols):
            for r in range(nrows):
                if r == 0 and c > 0:
                    # top row
                    ans[r] = grid[r][c] + ans[r]
                elif r > 0 and c == 0:
                    # left col
                    ans[r] = grid[r][c] + ans[r - 1]
                elif r > 0 and c > 0:
                    # everywhere else
                    ans[r] = grid[r][c] + min(ans[r - 1], ans[r])
                else:
                    # top left corner
                    ans[r] = grid[r][c]
        return ans[-1]

    # left-right, O(mn) time, O(1) space
    def minPathSum9(self, grid):
        nrows = len(grid)
        ncols = len(grid[0])

        for c in range(ncols):
            for r in range(nrows):
                if r == 0 and c > 0:
                    # top row
                    grid[r][c] = grid[r][c] + grid[r][c - 1]
                elif r > 0 and c == 0:
                    # left col
                    grid[r][c] = grid[r][c] + grid[r - 1][c]
                elif r > 0 and c > 0:
                    # everywhere else
                    grid[r][c] = grid[r][c] + min(grid[r - 1][c], grid[r][c - 1])
        return grid[-1][-1]

    # right-left, classic 2D O(mn) time, O(mn) space
    def minPathSum10(self, grid):
        nrows = len(grid)
        ncols = len(grid[0])
        ans = [[0 for i in range(ncols)] for j in range(nrows)]

        for c in range(ncols - 1, - 1, - 1):
            for r in range(nrows - 1, - 1, - 1):
                if r == nrows - 1 and c < ncols - 1:
                    # bottom row
                    ans[r][c] = grid[r][c] + ans[r][c + 1]
                elif r < nrows - 1 and c == ncols - 1:
                    # right col
                    ans[r][c] = grid[r][c] + ans[r + 1][c]
                elif r < nrows - 1 and c < ncols - 1:
                    # everywhere else
                    ans[r][c] = grid[r][c] + min(ans[r][c + 1], ans[r + 1][c])
                else:
                    # bottom right
                    ans[-1][-1] = grid[-1][-1]
        return ans[0][0]

    # right-left, 1-D O(mn) time, O(m) space
    def minPathSum11(self, grid):
        nrows = len(grid)
        ncols = len(grid[0])
        ans = [0 for i in range(nrows)]

        for c in range(ncols - 1, - 1, - 1):
            for r in range(nrows - 1, - 1, - 1):
                if r == nrows - 1 and c < ncols - 1:
                    # bottom row
                    ans[r] = grid[r][c] + ans[r]
                elif r < nrows - 1 and c == ncols - 1:
                    # right col
                    ans[r] = grid[r][c] + ans[r + 1]
                elif r < nrows - 1 and c < ncols - 1:
                    # everywhere else
                    ans[r] = grid[r][c] + min(ans[r], ans[r + 1])
                else:
                    # bottom right
                    ans[-1] = grid[-1][-1]
        return ans[0]

    # right-left, O(mn) time, O(1) space
    def minPathSum12(self, grid):
        nrows = len(grid)
        ncols = len(grid[0])

        for c in range(ncols - 1, - 1, - 1):
            for r in range(nrows - 1, - 1, - 1):
                if r == nrows - 1 and c < ncols - 1:
                    # bottom row
                    grid[r][c] = grid[r][c] + grid[r][c + 1]
                elif r < nrows - 1 and c == ncols - 1:
                    # right col
                    grid[r][c] = grid[r][c] + grid[r + 1][c]
                elif r < nrows - 1 and c < ncols - 1:
                    # everywhere else
                    grid[r][c] = grid[r][c] + min(grid[r][c + 1], grid[r + 1][c])
        return grid[0][0]

    # BFS, starting with top left
    def minPathSum13(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        queue = [(0, 0)]

        while queue:
            loc = queue[0]
            del queue[0]

            # if at top row
            if loc[0] == 0 and loc[1] > 0:
                grid[loc[0]][loc[1]] += grid[loc[0]][loc[1] - 1]
            # if at left col
            elif loc[0] > 0 and loc[1] == 0:
                grid[loc[0]][loc[1]] += grid[loc[0] - 1][loc[1]]
            elif loc[0] > 0 and loc[1] > 0:
                grid[loc[0]][loc[1]] += min(grid[loc[0] - 1][loc[1]], grid[loc[0]][loc[1] - 1])

            # append right
            if loc[1] + 1 < len(grid[0]):
                if (loc[0], loc[1] + 1) not in queue:
                    queue.append((loc[0], loc[1] + 1))

            # append down
            if loc[0] + 1 < len(grid):
                if (loc[0] + 1, loc[1]) not in queue:
                    queue.append((loc[0] + 1, loc[1]))

        return grid[-1][-1]

    # BFS, starting with bottom right
    def minPathSum14(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        nrows = len(grid)
        ncols = len(grid[0])
        queue = [(nrows - 1, ncols - 1)]

        while queue:
            loc = queue[0]
            del queue[0]

            # if at bottom row
            if loc[0] == nrows - 1 and loc[1] < ncols - 1:
                grid[loc[0]][loc[1]] += grid[loc[0]][loc[1] + 1]
            # if at right col
            elif loc[0] < nrows - 1 and loc[1] == ncols - 1:
                grid[loc[0]][loc[1]] += grid[loc[0] + 1][loc[1]]
            elif loc[0] < nrows - 1 and loc[1] < ncols - 1:
                grid[loc[0]][loc[1]] += min(grid[loc[0] + 1][loc[1]], grid[loc[0]][loc[1] + 1])

            # append above
            if loc[1] - 1 >= 0:
                if (loc[0], loc[1] - 1) not in queue:
                    queue.append((loc[0], loc[1] - 1))

            # append left
            if loc[0] - 1 >= 0:
                if (loc[0] - 1, loc[1]) not in queue:
                    queue.append((loc[0] - 1, loc[1]))

        return grid[0][0]



solver = Solution()
print(solver.minPathSum14([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))