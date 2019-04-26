class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        ans = float('inf')
        cum = 0
        i = 0
        for j in range(len(nums)):
            cum += nums[j]
            while cum >= s:
                ans = min(ans, j - i + 1)
                cum -= nums[i]
                i += 1
        if ans == float('inf'):
            return 0
        return ans