class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 0, x

        while l <= r:
            m = (l + r) // 2
            if m ** 2 <= x:
                l = m + 1
                ans = m
            else:
                r = m - 1
        return ans

    def newton(self, x):
        r = x
        while r * r > x:
            r = (r + x / r) / 2
        return r

solver = Solution()
print(solver.mySqrt(6))