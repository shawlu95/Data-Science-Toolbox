class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        neg = ((dividend < 0) != (divisor < 0))
        dividend = left = abs(dividend)
        divisor = div = abs(divisor)
        Q = 1  # quotient
        ans = 0
        while left >= divisor:
            left -= div
            ans += Q
            # speed up
            Q += Q
            div += div

            # restart when indivisible
            if left < div:
                div = divisor
                Q = 1
        # cap extreme positve & negative
        if neg:
            return max(-ans, -2 ** 31)
        else:
            return min(ans, 2 ** 31 - 1)