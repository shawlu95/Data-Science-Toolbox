class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        rows = ["" for _ in range(min(numRows, len(s)))]

        r = 0
        dr = -1

        for c in s:
            rows[r] += c

            # change direction when reaching top or bottom
            if r == 0 or r == numRows - 1:
                dr = -dr
            r += dr

        return "".join(rows)