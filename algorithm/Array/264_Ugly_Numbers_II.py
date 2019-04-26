class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [1]
        i2 = i3 = i5 = 0

        while len(nums) != n:
            while nums[i2] * 2 <= nums[-1]:
                i2 += 1
            while nums[i3] * 3 <= nums[-1]:
                i3 += 1
            while nums[i5] * 5 <= nums[-1]:
                i5 += 1
            nums.append(min(nums[i2] * 2, nums[i3] * 3, nums[i5] * 5))
        return nums[-1]
