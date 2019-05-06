class Solution(object):

    def findPeakElementLinear(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            # check dangerous condition first
            if i == len(nums) - 1 or (nums[i + 1] < nums[i]):
                return i
            i += 1

    def findPeakElementBisec(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        if not nums:
            return

        if len(nums) == 1:
            return 0

        if len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1

        while l < r: # should not exclude equal case
            m = (l + r) // 2
            if nums[m] > nums[m - 1] and nums[m] > nums[m + 1]:
                return m
            elif nums[m] < nums[m - 1]:
                # climb left uphill
                r = m - 1
            elif nums[m] < nums[m + 1]:
                # climb right uphill
                l = m + 1
        # no peak exists
        return l if nums[0] > nums[-1] else r

