# recursive with memo
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # mapping integer to number of coin
        cache = {}
        
        def searchTree(coins, target):
            nonlocal cache
            if target < 0:
                return -1
            
            if target == 0:
                return 0
            
            if target in cache:
                return cache[target]
            
            minTmp = 2 ** 32
            for coin in coins:
                min_ = searchTree(coins, target - coin)
                if min_ >= 0 and min_ < minTmp:
                    minTmp = min_ + 1 # do not add if min_ == -1
            
            if minTmp == 2 ** 32:
                cache[target] = -1
            else:
                cache[target] = minTmp
            
            # return -1 if cannot reach
            return cache[target]
                    
        return searchTree(coins, amount)

# DP
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 0 1 1 2 2 1 2 2 3 3 2 3
        # 0 1 2 3 4 5 6 7 8 9 A B
        
        dp = [None] * (amount + 1) # don't forget to pad zero!
        dp[0] = 0
        for num in range(1, len(dp)):
            minTmp = 2 ** 32
            for coin in coins:
                if num - coin >= 0 and dp[num - coin] != -1: # careful not to add to -1
                    minTmp = min(minTmp, dp[num - coin])
                    
            if minTmp == 2 ** 32:
                dp[num] = -1
            else:
                dp[num] = minTmp + 1
        print(dp)
        return dp[-1]