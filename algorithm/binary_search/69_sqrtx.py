class Solution(object):
    def mySqrt(self, x):
        """
        Take floor of largest number s.t. num ** 2 <= x

        九章算法模版
        """
        if x == 0: return 0

        l, r = 0, x

        while l + 1 < r:
            m = (r - l) // 2 + l
            if m ** 2 == x:
                return m
            elif m ** 2 < x:
                l = m
            else:
                r = m - 1

        # need to have `<=` here to handle edge case x = 1
        # l = 0, r = 1, loop never enters
        if r ** 2 <= x:
            return r
        return l

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
