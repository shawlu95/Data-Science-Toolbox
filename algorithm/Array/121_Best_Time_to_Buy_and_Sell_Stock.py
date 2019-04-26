class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # handle corner case of empty array
        # note that when array size is 1, it's handled well by the rest of the code
        if not prices:
            return 0

        # initial case: buy and sell on day 0, making 0 profit
        buy = sell = prices[0]
        profit = 0
        for i in range(1, len(prices)):

            # every time price drops to a new low, it's an opportunity to buy,
            # and make potentially high profit. Reset sell price.
            if prices[i] <= buy:
                buy = sell = prices[i]

            # when price rises above last sell price, better profit can be made.
            # update max profit if necessary
            if prices[i] >= sell:
                sell = prices[i]
                profit = max(profit, sell - buy)
        return profit

solver = Solution()
ans = solver.maxProfit([2, 4, 1])
print(ans)