class Solution:
    # brute force, O(2 ^ (N - 1))
    def findTargetSumWaysBrute(self, nums: [int], S: int) -> int:
        self.ans = 0
        
        def dfs(arr, i, s):
             # careful, last num len(arr) - 1 is not base case
            if i == len(arr): 
                if s == 0:
                    self.ans += 1
                return
            
            dfs(arr, i + 1, s - arr[i])
            dfs(arr, i + 1, s + arr[i])

        if not nums:
            return 0

        dfs(nums, 0, S)

        return self.ans

    def findTargetSumWaysDP(self, nums: [int], S: int) -> int:
        n = len(nums)
        s = sum(nums)
        if s < S: return 0

        dp = [[0] * (2 * s + 1) for _ in range(n + 1)]
        dp[0][s] = 1

        for i in range(n):
            for j in range(nums[i], 2 * s + 1 - nums[i]):

                if dp[i][j]:
                    dp[i + 1][j + nums[i]] += dp[i][j]
                    dp[i + 1][j - nums[i]] += dp[i][j]

        return dp[-1][s + S]

solver = Solution()
nums = [5, 6, 8]
S = 3
print(solver.findTargetSumWaysDP(nums, S))