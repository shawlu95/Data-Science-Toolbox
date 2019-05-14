class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        Plain implementation: difficult to adapt!

        Initialize `r` to `len(arr) - 1`, not `len(arr)`, which causes index out of bound error.
        `l = m + 1`: need to increment by 1 because integer division rounds down. Think of the case where `r` points to `a` and `l` is repeated moving right.
        `r = m - 1`: `r = m` may get stuck if `a` is not found and `l` can not move right. Then need to move `r` repeatedly left until l - r == 1.
        If `a` is not found, `l` is where `a` should have been inserted in the sorted array. (l - r = 1)
        """
        l, r = 0, len(nums) - 1 # mind the "-1"

        while l <= r:
            # cannot use !=, because of edge case [1] (length 1)
            m = (l + r) // 2
            if nums[m] == target:
                return m

            elif nums[m] > target:
                # must subtract 1
                # or 1, r never meet if target does not exist
                r = m - 1
            else:
                # must add 1
                # or 1, r never meet if target does not exist
                l = m + 1
        return -1
