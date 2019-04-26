class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s = set(nums1)
        ans = set()
        for num in nums2:
            if num in s:
                ans.add(num)
        return list(ans)