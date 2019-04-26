class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        twoSum = {}
        ans = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                twoSum[- (nums[i] + nums[j])] = (i, j)
        for k in range(len(nums)):
            if nums[k] in twoSum.keys() and k not in twoSum[k]:
                ans.append([nums[k], nums[twoSum[k][0]],  nums[twoSum[k][1]]])
        return ans

    def threeSumTwoPointers(self, nums):
        ans = []
        if len(nums) < 3:
            return ans

        nums.sort()
        for i in range(len(nums) - 2):
            # i has been incremented, check if it's equal to earlier i (i - 1)t
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    # warning: j has been incremented, check if it's equal to previous j (j - 1)
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    # warning: k has been decremented, check if it's equal to previous k (k + 1)
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif s < 0:
                    j += 1
                else:
                    k -= 1
        return ans

solver = Solution()
ans = solver.threeSumTwoPointers([-2,0,1,1,2])
print(ans)