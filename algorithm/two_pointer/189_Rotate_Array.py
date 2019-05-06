class Solution:
    def rotate1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            tmp = nums[-1]
            for j in range(len(nums)-1, -1, 0):
                nums[j] = nums[j - 1]
            nums[0] = tmp

    def rotate2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            tmp = nums[-1]
            del nums[-1]
            nums.insert(0, tmp)

    # reverse
    def rotate3(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # in case k is greater than len, moving element by len position returns to original position
        k = k % len(nums)
        def reverse(nums, i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, len(nums) - 1)

    # CYCLIC SWAP
    def rotate4(self, nums, k):
        k = k % len(nums)
        count = 0
        start = 0
        while count != len(nums):
            current = start
            prev = nums[start]
            while True:
                next = (current + k) % len(nums)
                tmp = nums[next]
                nums[next] = prev
                prev = tmp
                current = next
                count += 1
                if start == current:
                    break
            start += 1

