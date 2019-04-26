class Solution(object):
    def twoSumHasg(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int] return index
        """
        # for i in range(len(nums)):
        #     n1 = nums[i]
        #     n2 = target - n1
        #     for j in range(len(nums)):
        #         if n2 == nums[j] and i != j:
        #             return [i, j]
        maps = {}
        for i in range (len(nums)):
            n2 = target-nums[i]
            if n2 in maps:
                return [maps[n2], i]
            maps[nums[i]] = i

