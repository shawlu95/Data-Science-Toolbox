class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        e, t, d = 0, 0, len(nums) - 1

        # DO NOT MISS the equality sign
        # [1, 0, 2], e, t, d = 0, 1, 1
        while t <= d:
            if nums[t] == 0:
                nums[e], nums[t] = nums[t], nums[e]
                # both e and t are now in correct position
                e += 1
                t += 1
            elif nums[t] == 1:
                # t is in correct position
                t += 1
            elif nums[t] == 2:
                nums[t], nums[d] = nums[d], nums[t]
                d -= 1
                # this may cause d == t,
                # but nums[d] (now at t) may not be at correct place
                # so equality sign must be used


arr = [2,0,2,1,1,0]
solver = Solution()
solver.sortColors(arr)
print(arr)