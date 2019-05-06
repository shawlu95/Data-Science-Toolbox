class Solution:
    def findDuplicateSort(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]

    def findDuplicateCycle(self, nums):
        # Find the intersection point of the two runners.
        tortoise = nums[0]
        hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # Find the "entrance" to the cycle.
        ptr1 = nums[0]
        ptr2 = tortoise
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]

        return ptr1

solver = Solution()
ans = solver.findDuplicateCycle([3,1,3,4,2])
print(ans)