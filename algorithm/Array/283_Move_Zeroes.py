class Solution(object):
    def moveZeroes2PointersOpt(self, nums):
        fast = slow = 0
        # fast pointer moves fast, to find all non zero numbers
        # slow pointer is responsible for putting down every non-zero number recently found
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow] = nums[fast]

                # if the current element is non-0, its'
                # correct position can at best be it's current
                # position (slow == fast) or a position earlier (slow < fast)
                if slow != fast:
                    nums[fast] = 0

                slow += 1
            fast += 1

    def moveZeroes2Pointers(self, nums):
        fast = slow = 0
        # fast pointer moves fast, to find all non zero numbers
        # slow pointer is responsible for putting down every non-zero number recently found
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        # after non-zero numbers have been moved to the front, fill the rest of the array with 0
        while slow < len(nums):
            nums[slow] = 0
            slow += 1

    def moveZeroesBubble(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # bubble sort (very slow)
        good = False
        while good is False:
            good = True
            for i in range(len(nums) - 1):
                if nums[i] == 0 and nums[i + 1] != 0:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    good = False



solver = Solution()
solver.moveZeroes2PointersOpt([0,1,0,3,12])