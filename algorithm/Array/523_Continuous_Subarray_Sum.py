class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        # map sum to idx
        s = {0 : -1}
        rolling = 0
        for i in range(len(nums)):
            num = nums[i]
            rolling += num
            if k != 0:
                rolling = rolling % k
            if rolling in s:
                if i - s[rolling] > 1:
                    return True
            else:
                s[rolling] = i
        return False