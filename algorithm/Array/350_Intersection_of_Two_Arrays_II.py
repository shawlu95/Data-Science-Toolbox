class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count1 = {}
        for num in nums1:
            count1[num] = count1.get(num, 0) + 1

        count2 = {}
        for num in nums2:
            count2[num] = count2.get(num, 0) + 1

        ans = []
        for num in nums1:
            if num in count2:
                ans += [num] * min(count1[num], count2[num])

                # tricky!
                del count2[num]
        return ans

    # for two sorted array
    # if nums1[pt1] > nums2[pt2]:
    #     pt2 += 1
    # elif nums1[pt1] < nums2[pt2]:
    #     pt1 += 1
    # else:
    #     res.append(nums1[pt1])
    #     pt1 += 1
    #     pt2 += 1
    def intersect2(self, nums1, nums2):

        nums1, nums2 = sorted(nums1), sorted(nums2)
        pt1 = pt2 = 0
        res = []

        while pt1 < len(nums1) and pt2 < len(nums2):
            if nums1[pt1] > nums2[pt2]:
                pt2 += 1
            elif nums1[pt1] < nums2[pt2]:
                pt1 += 1
            else:
                res.append(nums1[pt1])
                pt1 += 1
                pt2 += 1

        return res