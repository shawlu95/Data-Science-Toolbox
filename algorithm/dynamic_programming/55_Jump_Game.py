class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        def canJumpFromPosition(position, nums, d):
            if position == len(nums) - 1:
                return True

            # can jump to next position if in bound, or end of list if out of bound
            furthestJump = min(position + nums[position], len(nums) - 1)
            nextPosition = position + 1
            while nextPosition <= furthestJump:
                print(position, nextPosition)
                if canJumpFromPosition(nextPosition, nums, d + 1):
                    return True

                nextPosition += 1
            return False

        return canJumpFromPosition(0, nums, 0)

    # def canJump2(self, nums):
    #     def canJumpFromPosition(position, nums, d):
    #         if position == len(nums) - 1:
    #             return True
    #
    #         # can jump to next position if in bound, or end of list if out of bound
    #         furthestJump = min(position + nums[position], len(nums) - 1)
    #         nextPosition = furthestJump
    #         while nextPosition > furthestJump:
    #             if canJumpFromPosition(nextPosition, nums, d + 1):
    #                 return True
    #
    #             nextPosition -= 1
    #         return False
    #
    #     return canJumpFromPosition(0, nums, 0)

    # dynamic programming top down
    def canJumpMemo(self, nums):
        def canJumpFromPosition(position, nums, memo, d):
            if memo[position] != 'U':
                return memo[position] == 'G'

            # can jump to next position if in bound, or end of list if out of bound
            furthestJump = min(position + nums[position], len(nums) - 1)
            nextPosition = position + 1
            while nextPosition <= furthestJump:
                if canJumpFromPosition(nextPosition, nums, memo, d + 1):
                    memo[position] = 'G'
                    return True

                nextPosition += 1
            memo[position] = 'B'
            return False

        memo = ['U'] * len(nums)
        memo[-1] = 'G'
        return canJumpFromPosition(0, nums, memo, 0)

    # starting with last index, moving forward
    # move forward to an earlier index only when earlier index can jump to later index
    def canJump(self, nums):
        last = len(nums) - 1
        for i in range(len(nums) - 2, - 1, - 1):
            if i + nums[i] >= last:
                last = i
        return last == 0

    # exat jump length
    def canJumpDP(self, nums):
        memo = [None] * len(nums)
        memo[-1] = True

        for i in range(len(nums) - 2, - 1, - 1):
            j = i + nums[i]
            if j < len(nums) and memo[j] is True:
                memo[i] = True
            else:
                memo[i] = False

        return memo[0]

    # maximum jump length
    def canJumpDP2(self, nums):
        memo = [False] * len(nums)
        memo[-1] = True

        for i in range(len(nums) - 2, - 1, - 1):
            end = min(i + nums[i], len(nums) - 1)

            for j in range(i + 1, end + 1):
                if memo[j] == True:
                    memo[i] = True
                    break
        return memo[0]



arr1 = [2,3,1,1,4]
arr2 = [3,2,1,0,4]
arr3 = [2, 0]
solver = Solution()
print(solver.canJumpDP2(arr2))