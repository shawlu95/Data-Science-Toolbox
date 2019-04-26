class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        nrows = len(matrix)  # nrows
        ncols = len(matrix[0])  # ncols

        # starting at upper right corner
        r = 0
        c = ncols - 1

        # search rows downward
        # search cols left-ward
        # the special arrangement of matrix allow linear time algo
        while r <= nrows - 1 and c >= 0:
            if matrix[r][c] > target:
                c -= 1
            elif matrix[r][c] < target:
                r += 1
            else:
                return True
        return False

solver = Solution()
print(solver.searchMatrix([
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
], 5))