class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        # using the sign as a boolean of seen or unseen
        # this method only works when all numbers are positive
        # and maximum element is equal to size of array
        for x in nums:
            # if element is negative, it has been seen before
            if nums[abs(x)-1] < 0:
                res.append(abs(x))
            else:
                # otherwise, mark it as seen by making it negative
                nums[abs(x)-1] *= -1
        return res

solver = Solution()
ans = solver.findDuplicates([4,3,2,7,8,2,3,1])
print(ans)