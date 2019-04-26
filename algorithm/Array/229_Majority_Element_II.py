class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cand1 = None
        cand2 = None
        count1 = 0
        count2 = 0

        # first pass, Boyer-Moore
        for num in nums:
            # note that the two candidates may be duplicate, consider input [2, 2]
            # cand2 will remain 0, and will be discarded in second pass
            if count1 == 0 and cand2 != num:
                cand1 = num
            elif count2 == 0 and cand1 != num:
                cand2 = num

            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        # second pass, check frequency
        # warning, use 'is not None' to check existence
        # use 'if n' will return false if n is zero (numeric)
        return [n for n in (cand1, cand2)
                if n is not None and nums.count(n) > len(nums) // 3]

solver = Solution()
ans = solver.majorityElement([1,1,1,3,3,2,2,2])
# ans = solver.majorityElement([0,0])
print(ans)