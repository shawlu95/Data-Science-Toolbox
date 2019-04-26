class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy1 = float('-inf')
        buy2 = float('-inf')
        sell1 = 0
        sell2 = 0

        for price in prices:
            # The maximum if we've just sold 2nd stock so far.
            sell2 = max(sell1, buy2 + price)

            # The maximum if we've just buy  2nd stock so far.
            buy2 = max(buy2, sell1 - price)

            # The maximum if we've just sold 1nd stock so far.
            sell1 = max(sell1, buy1 + price)

            # The maximum if we've just buy  1st stock so far.
            buy1 = max(buy1, - price)

        # Since release1 is initiated as 0, so release2 will always higher than release1.
        return sell2

solver = Solution()
print(solver.maxProfit([3,3,5,0,0,3,1,4]))