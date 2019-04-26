class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        # save each row as rolling sum
        rolling = [[0] * len(matrix[0]) for i in range(len(matrix))]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                rolling[r][c] = matrix[r][c] + rolling[r][c - 1]
        self.rolling = rolling

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        old_val = self.rolling[row][col]
        if col > 0:
            old_val -= self.rolling[row][col - 1]

        for c in range(col, len(self.rolling[0])):
            self.rolling[row][c] -= old_val
            self.rolling[row][c] += val

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        s = 0
        for r in range(row1, row2 + 1):
            s += self.rolling[r][col2]

            if col1 > 0:
                s -= self.rolling[r][col1 - 1]
        return s

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)