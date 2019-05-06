class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if not stones or (len(stones) > 1 and stones[1] != 1):
            return False

        # each stone maps to a set of jump lengths that can lead to current stone
        dp = {x : set() for x in stones}

        # start with first stone, there is only one way to jump to firs stone
        dp[1].add(1)

        for stone in stones[1:]:
            if dp[stone]:
                # use previous jump lengths to determine all possible destinations
                for pre_k in dp[stone]:
                    for nxt_k in range(pre_k - 1, pre_k + 2):
                        # warning: check set for existence, not list. The following condition will exceeds time limit
                        # if nxt_k > 0 and stone + nxt_k in dp:
                        if nxt_k > 0 and stone + nxt_k in dp:
                            dp[stone + nxt_k].add(nxt_k)
        return dp[stones[-1]] != set()

solver = Solution()
solver.canCross([0,1,3,5,6,8,12,17])