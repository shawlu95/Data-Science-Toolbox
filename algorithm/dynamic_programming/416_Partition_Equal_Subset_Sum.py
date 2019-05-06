# subset
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        self.target = int(sum(nums) / 2)
        
        self.subsets = []
        
        def combo(nums, subset, i):
            """Check all possible combination of numbers recursively"""
            self.subsets.append(subset)
            for i in range (i, len(nums)):
                combo(nums, subset + [nums[i]], i + 1)
        
        combo(nums, [], 0)
        
        print(self.subsets)
        return len(self.subsets) == 0

# brute force
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1: return False
        self.target = int(sum(nums) / 2)
        
        def combo(nums, subset, i):
            """Check all possible combination of numbers recursively"""
            if subset == self.target:
                return True
            return any(combo(nums, subset + nums[i], i + 1) 
                       for i in range (i, len(nums)) if nums[i] <= self.target)
        
        return combo(nums, 0, 0)
        
# 2D DP
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) & 1: return False
        
        target = sum(nums) // 2
        
        dp = [[False] * (target + 1) for _ in range(len(nums) + 1)]
        for i in range(len(dp)):
            dp[i][0] = True
        
        for r in range(1, len(dp)):
            print(r, len(dp), len(dp[0]))
            for c in range(1, len(dp[0])):
                if c >= nums[r - 1]: # or c - nums[r - 1] will be negative
                    dp[r][c] = dp[r - 1][c] or dp[r - 1][c - nums[r - 1]]

        return dp[-1][target]

# 1D DP backward (to avoid overwriting inner loop)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) & 1: return False
        
        target = sum(nums) // 2
        
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in nums:
            for c in range(len(dp) - 1, -1, -1): # careful with starting index
                if c >= num: # or c - nums[r - 1] will be negative
                    dp[c] = dp[c] or dp[c - num]
            # print([int(i) for i in dp], num)
            # [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 1
            # [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0] 5
            # [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1] 11
            if dp[-1]: return True # early stopping
        return False
        