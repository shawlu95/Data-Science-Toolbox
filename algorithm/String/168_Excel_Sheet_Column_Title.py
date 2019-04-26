class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """

        ans = ""

        while n != 0:
            # corner case 26: insert 25(Z), then n <- (25 // 26) == 0
            ans = chr(ord('A') + (n - 1) % 26) + ans
            n = (n - 1) // 26
        return ans




