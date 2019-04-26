class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        self.ans = float('inf')
        numLevel = len(triangle)
        def dfs(triangle, r, c, pathSum):
            if r == numLevel:
                self.ans = min(self.ans, pathSum)
                return

            pathSum += triangle[r][c]

            # go left
            dfs(triangle, r + 1, c, pathSum)
            # go right
            dfs(triangle, r + 1, c + 1, pathSum)

        dfs(triangle, 0, 0, 0)
        return self.ans

    def minimumTotalList(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        cands = []
        numLevel = len(triangle)
        def dfs(triangle, r, c, pathSum, cands):
            if r == numLevel:
                cands.append(pathSum)
                return

            pathSum += triangle[r][c]

            # go left
            dfs(triangle, r + 1, c, pathSum, cands)
            # go right
            dfs(triangle, r + 1, c + 1, pathSum, cands)

        dfs(triangle, 0, 0, 0, cands)
        return min(cands)

    # O(n*n/2) space, top-down
    def minimumTotal1(self, triangle):
        if not triangle:
            return
        res = [[0 for i in range(len(row))] for row in triangle]
        res[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                # left most, arrived from left most in level above
                if j == 0:
                    res[i][j] = res[i - 1][j] + triangle[i][j]
                # right most, arrived from right most in level above
                elif j == len(triangle[i]) - 1:
                    res[i][j] = res[i - 1][j - 1] + triangle[i][j]
                # middle, two possible paths to arrive at
                else:
                    res[i][j] = min(res[i - 1][j - 1], res[i - 1][j]) + triangle[i][j]
        return min(res[-1]) # [15, 11, 18, 16]

    # Modify the original triangle, top-down
    def minimumTotal2(self, triangle):
        if not triangle:
            return
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] += triangle[i - 1][j]
                elif j == len(triangle[i]) - 1:
                    triangle[i][j] += triangle[i - 1][j - 1]
                else:
                    triangle[i][j] += min(triangle[i - 1][j - 1], triangle[i - 1][j])
        return min(triangle[-1])

    # Modify the original triangle, bottom-up
    def minimumTotal3(self, triangle):
        if not triangle:
            return
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]

    # bottom-up, O(n) space
    def minimumTotal4(self, triangle):
        if not triangle:
            return
        res = list(triangle[-1]) # make a copy
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                res[j] = min(res[j], res[j + 1]) + triangle[i][j]
        # [11, 10, 10, 3]
        return res[0]


solver = Solution()
ans = solver.minimumTotal1([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
])

print(ans)