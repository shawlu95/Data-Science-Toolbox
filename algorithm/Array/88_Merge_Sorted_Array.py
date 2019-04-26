class Solution:
    # terrible pointer: index, not length
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        m -= 1
        n -= 1
        while n >= 0 and m >= 0:
            if nums1[m] > nums2[n]:
                nums1[m + n + 1] = nums1[m]
                m -= 1
            else:
                nums1[m + n + 1] = nums2[n]
                n -= 1
        if n + 1 > 0:
            nums1[:n + 1] = nums2[:n + 1]
        print(nums1)

    # better pointer definition: length, not index
    def merge2(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
        print(nums1)




solver = Solution()
# ans = solver.merge([1,2,3,0,0,0], 3,
#                                  [2, 5, 6], 3)

ans = solver.merge([2, 0], 1,
                                 [1], 1)