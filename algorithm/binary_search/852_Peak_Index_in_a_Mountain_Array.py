class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        def helper(A, l, h):
            m = (l + h) // 2

            if A[m] > max(A[m + 1], A[m - 1]):
                return m
            elif A[m] < A[m + 1]:
                return helper(A, m + 1, h)
            elif A[m] < A[m - 1]:
                return helper(A, l, m - 1)

        return helper(A, 0, len(A) - 1)

    def peakIndexInMountainArrayIterate(self, A):
        l, h = 0, len(A) - 1

        # the problem was set up such that a peak must exist
        while True:
            m = (l + h) // 2
            if A[m] > max(A[m + 1], A[m - 1]):
                return m
            elif A[m] < A[m + 1]:
                l = m + 1
            elif A[m] < A[m - 1]:
                h = m - 1

    def peakIndexInMountainArrayIterateBad(self, A):
        lo, hi = 0, len(A) - 1
        while lo < hi:
            mi = (lo + hi) / 2
            if A[mi] < A[mi + 1]:
                # peak is on the right
                lo = mi + 1
            else:
                # peak is on the left (mid may be the peak)
                hi = mi
        return lo

solver = Solution()
ans = solver.peakIndexInMountainArrayIterate([0,1,2,3,0])
print(ans)