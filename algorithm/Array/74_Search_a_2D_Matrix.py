class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or matrix == [[]]:
            return False

        nrows = len(matrix)
        ncols = len(matrix[0])

        r = 0
        c = ncols - 1
        while c >= 0 and r <= nrows - 1:
            if matrix[r][c] > target:
                c -= 1
            elif matrix[r][c] < target:
                r += 1
            elif matrix[r][c] == target:
                return True
        return False

solver = Solution()
print(solver.searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 3))