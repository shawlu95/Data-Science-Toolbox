class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1, 1]]
        else:
            ans = [[1],
                   [1, 1]]

            for i in range(2, numRows):
                l = [1]
                prevRow = ans[i - 1]
                for j in range(len(prevRow) - 1):
                    l.append(prevRow[j] + prevRow[j + 1])
                l.append(1)
                ans.append(l)
        return ans

    # cleaner solution, gracefully handle corner case
    def generate2(self, num_rows):
        triangle = []

        for row_num in range(num_rows):
            # The first and last row elements are always 1.
            row = [None for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row) - 1):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

            triangle.append(row)

        return triangle

solver = Solution()
ans = solver.generate2(5)
for row in ans:
    print(row)