class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers) - 1
        while numbers[l] + numbers[r] != target:
            if numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
        return [l + 1, r + 1]

    def twoSum2(self, nums, target):
        i, j = 0, len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            elif numbers[i] + numbers[j] < target:
                i += 1
                while i < j and numbers[i] == numbers[i - 1]:
                    i += 1
            else:
                j -= 1
                while i < j and numbers[j] == numbers[j + 1]:
                    j -= 1

    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    # two sum unique pair
    def twoSum6(self, nums, target):
        if not nums or len(nums) < 2:
            return 0

        nums.sort()

        count = 0
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] + nums[right] == target:
                count, left, right = count + 1, left + 1, right - 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1

        return count
solver = Solution()
print(solver.twoSum([2,7,11,15], 9))