class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height) - 1
        a = 0
        while i < j:
            h = min(height[i], height[j])
            a = max((j - i) * h, a)
            if height[i] < height[j]:
                i += 1
            elif height[i] >= height[j]:
                j -= 1
        return a

    def maxArea2(self, height):
        i, j = 0, len(height) - 1
        a = 0
        while i < j:
            h = min(height[i], height[j])
            a = max((j - i) * h, a)

            if height[i] < height[j]:
                while height[i] <= h and i < j:
                    i += 1
            elif height[i] >= height[j]:
                while height[j] <= h and i < j:
                    j -= 1
        return a

    # this is identical to maxArea2
    def maxArea3(self, height):
        i, j = 0, len(height) - 1
        a = 0
        while i < j:
            h = min(height[i], height[j])
            a = max((j - i) * h, a)
            while height[j] <= h and i < j:
                j -= 1
            while height[i] <= h and i < j:
                i += 1
        return a

solver = Solution()
ans = solver.maxArea3([1,8,6,2,5,4,8,3,7])
print(ans)