class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return True
            while l < mid and nums[l] == nums[mid]:  # tricky part
                l += 1
            # the first half is ordered
            if nums[l] <= nums[mid]:
                # target is in the first half
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # the second half is ordered
            else:
                # target is in the second half
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False

    def search2(self, nums, target):
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2

            if nums[m] == target:
                return True

            while i < m and nums[i] == nums[m]:  # tricky part
                i += 1
            if nums[i] <= nums[m]:
                # left side is sorted and has target
                if nums[i] <= target < nums[m]:
                    j = m - 1
                else:
                    i = m + 1
            elif nums[m] <= nums[j]:
                # right side is sorted and has target
                if nums[m] < target <= nums[j]:
                    i = m + 1
                else:
                    j = m - 1
        return False

solver = Solution()
solver.search2([1,3,1,1,1], 3)