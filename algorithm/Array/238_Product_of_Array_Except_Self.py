class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l_prod = 1
        ans = []
        for num in nums:
            ans.append(l_prod)
            l_prod *= num

        r_prod = 1
        for j in range(len(nums) - 1, - 1, -1):
            ans[j] *= r_prod
            r_prod *= nums[j]
        return ans
solver = Solution()
ans = solver.productExceptSelf([1, 2, 3, 4])
print(ans)