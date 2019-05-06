class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for _ in range(rowIndex):
            # pad 0, perform element-wise addition
            row = [x + y for x, y in zip([0] + row, row + [0])]
        return row

    # row = [1]
    # for i in range(rowIndex):
    #     row = [1] + [row[j] + row[j + 1] for j in range(len(row) - 1)] + [1]
    # return row