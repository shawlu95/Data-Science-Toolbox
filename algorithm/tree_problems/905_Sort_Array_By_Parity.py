class Solution(object):
    def sortArrayByParity(self, l):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        """
        Mark beginning as i, end as j

        If number at i is even, it is in correct position, advance i by 1.
        If number at j is odd, it is in correct position, decrease j by 1.
        If both i and j are in wrong position, switch them, and update i, j.

        Time: O(n)
        Space: O(1)
        """

        i, j = 0, len(l) - 1
        while j > i:
            if l[i] % 2 == 0:
                i += 1
            elif l[j] % 2 == 1:
                j -= 1
            elif l[i] % 2 == 1 and l[j] % 2 == 0:
                l[i], l[j] = l[j], l[i]
                i += 1
                j -= 1
        return l


solver = Solution()
ans = solver.sortArrayByParity([1,2,7,3,4])