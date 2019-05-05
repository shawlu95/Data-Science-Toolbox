class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1 # mind the "-1"

        while l <= r: # cannot use !=, because of edge case [1] (length 1)
            m = (l + r) // 2
            if nums[m] == target:
                return m

            elif nums[m] > target:
                r = m - 1 # must subtract 1, or 1, r never meet if target does not exist
            else:
                l = m + 1 # must add 1, or 1, r never meet if target does not exist
        return -1
