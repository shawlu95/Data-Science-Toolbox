class Solution(object):
    # brute force (submitted in August)
    from math import floor

    class Solution(object):
        baseline = 0

        def numSquaresBrute(self, n):
            """
            :type n: int
            :rtype: int
            """
            if n < 0:
                return 0

            set_ = []
            i = 1
            while i ** 2 < n:
                set_.append(i ** 2)
                i += 1

            sqrs = []
            n_ = n
            while n_ != 0:
                sqr = floor(n_ ** 0.5) ** 2
                sqrs.append(sqr)
                n_ = n_ - sqr
            self.baseline = len(sqrs)

            def numSquaresHelper(n, n_, used, cnt_):
                # base case:
                # if completing sum
                if n_ == 0:
                    self.baseline = min(self.baseline, cnt_)
                    return

                    # if exceeding baseline, no need to continue
                if cnt_ >= self.baseline:
                    return

                for sqr in set_:
                    if sqr <= n_:
                        used.append(sqr)
                        numSquaresHelper(n, n_ - sqr, used, cnt_ + 1)
                        used.pop()

            used = []
            # check if can do better
            numSquaresHelper(n, n, used, 0)

            return self.baseline

    # DP
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float('inf')] * (n + 1)
        print("Upperbound of square number: %i"%int(n ** 0.5 + 1))
        for i in range(1, int(n ** 0.5) + 1):
            dp[i ** 2] = 1

        for i in range(1, n + 1):
            for k in range(1, int(i ** 0.5) + 1):
                dp[i] = min(dp[i], dp[i - k ** 2] + 1)

        return dp[n]

solver = Solution()
print(solver.numSquares(12))