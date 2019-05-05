class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # not needed, handled automatically in while logic
        # if not nums or len(nums) < 2:
        #     return False

        for i, num in enumerate(nums):
            # not needed, handled automatically in while logic
            # if type(nums[i]) != int: # visited element
            #     continue
            # if nums[i] % n == 0: # self-loop
            #     continue

            # use a distinct marker for each starting point
            mark = str(i)

            # explore while node is new, direction maintains, and no self loop
            # if node has been marked by a different marker, no need to proceed
            j = i
            while (type(nums[j]) == int) and (num * nums[j] > 0) and (nums[j] % len(nums) != 0):
                jump = nums[j] # cannot switch with the line below
                nums[j] = mark
                j = (j + jump) % len(nums)

            # if self loop, nums[i] is never marked
            if nums[j] == mark:
                return True

        return False
