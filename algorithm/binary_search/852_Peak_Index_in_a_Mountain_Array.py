class Solution(object):
    """
    A peak element is guaranteed to exist!
    Use binary search method. Cannot directly
    apply the XXOO template.

    A point can have three possible scenarios:
        (1) ascending (compare to element at right)
        (2) at peak
        (3) descending (compare to element at left)
    """
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

solver = Solution()
ans = solver.peakIndexInMountainArrayIterate([0,1,2,3,0])
print(ans)
