class Solution(object):
    def rotate(self, matrix):
        # matrix is always square
        n = len(matrix)

        # handles both odd and even n
        for l in range(n // 2):

            # n - 1 is last column/row
            r = n - 1 - l

            # l, r defines layer
            # p, q traverse layer, excludes destination
            # p moves from low to high
            # q moves from high to low
            for p in range(l, r):
                q = n - 1 - p

                # save fixed lth row row, 0th, 1th.. element
                cache = matrix[l][p]

                # assign l th col to l th row
                matrix[l][p] = matrix[q][l]

                # assign r th row to l th col
                matrix[q][l] = matrix[r][q]

                # assign r th column to r th row
                matrix[r][q] = matrix[p][r]

                # assign lth row to r th col
                matrix[p][r] = cache