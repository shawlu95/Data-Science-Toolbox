class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] == 1:
            return 0

        nrows = len(obstacleGrid)
        ncols = len(obstacleGrid[0])

        for r in range(nrows):
            for c in range(ncols):
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = False

        obstacleGrid[0][0] = 1
        for r in range(nrows):
            for c in range(ncols):
                if obstacleGrid[r][c] is False:
                    obstacleGrid[r][c] = 0
                    continue
                if r == 0 and c > 0:
                    obstacleGrid[r][c] = obstacleGrid[r][c - 1]
                elif r > 0 and c == 0:
                    obstacleGrid[r][c] = obstacleGrid[r - 1][c]
                elif r > 0 and c > 0:
                    obstacleGrid[r][c] = obstacleGrid[r - 1][c] + obstacleGrid[r][c - 1]
        return obstacleGrid[-1][-1]

input = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

input = [[1, 0]]

solver = Solution()
ans = solver.uniquePathsWithObstacles(input)
print(ans)