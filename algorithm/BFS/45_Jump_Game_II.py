class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        start = 0 # start of range of indices to jump from at current step
        end = 0 # end of range of indices to jump from at current step (inclusive, so add 1 in iteration range)
        step = 0 # count how many steps have been taken
        while end < n - 1:
            step += 1
            maxend = end + 1
            for i in range(start, end + 1):
                if i + nums[i] >= n - 1:
                    return step
                maxend = max(maxend, i + nums[i])
            start = end + 1
            end = maxend
        return step

solver = Solution()
ans = solver.jump([2, 3, 1, 1, 4])
print(ans)