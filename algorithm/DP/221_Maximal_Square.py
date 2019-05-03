class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        build dp matrix with same dimension as matrix
        dp[i][j] is side length of largest square whose lower right corner ends at matrix[i][j]
        
        note:
        (1) if list is empty, cannot access ncol
        (2) pad an extra row and column to handle edge case
        (3) keep track of side length, not area
        (4) when return, square the side length
        """
        ans = 0
        nrow = len(matrix)
        if nrow == 0: return ans
        
        ncol = len(matrix[0])
        
        dp = [[0] * (ncol + 1) for _ in range(nrow + 1)]
        
        # not needed
        # for r in range(nrow):
        #     for c in range(ncol):
        #         dp[r + 1][c + 1] = int(matrix[r][c])
        
        for r in range(1, len(dp)):
            for c in range(1, len(dp[0])):
                if matrix[r - 1][c - 1] == "1": # offset to correct for padding
                    dp[r][c] = min(min(dp[r][c-1], dp[r-1][c]), dp[r - 1][c - 1]) + 1
                    ans = max(ans, dp[r][c])
        return ans ** 2