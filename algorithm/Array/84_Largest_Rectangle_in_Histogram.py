class Solution(object):
    def largestRectangleArea1(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        self.ans = float('-inf')

        def recurse(heights, l, r):
            if l > r:
                return 0
            min_idx = l

            # index r is included when searching min
            for i in range(l, r + 1):
                if heights[min_idx] > heights[i]:
                    min_idx = i

            print(l, r)

            return max(
                heights[min_idx] * (r - l + 1),
                recurse(heights, l, min_idx - 1),
                recurse(heights, min_idx + 1, r))

        return recurse(heights, 0, len(heights) - 1)


    def largestRectangleArea2(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        self.ans = float('-inf')

        def recurse(heights, l, r):
            if l > r:
                return 0
            min_idx = l

            # index r is included when searching min
            for i in range(l, r + 1):
                if heights[min_idx] > heights[i]:
                    min_idx = i

            print(l, r)

            # time limit exceeded
            cur = heights[min_idx] * (r - l + 1)
            left = recurse(heights, min_idx + 1, r)
            right = recurse(heights, l, min_idx - 1)
            return max(cur, left, right)

        return recurse(heights, 0, len(heights) - 1)

    def largestRectangleArea(self, height):
        height.append(0)
        stack, size = [], 0
        for i in range(len(height)):
            while stack and height[stack[-1]] > height[i]:
                l = stack.pop()
                h = height[l]
                w = i if not stack else i-l
                cand = h * w
                print(cand)
                size = max(size, cand)
            stack.append(i)
        return size

solver = Solution()

arr1 = [2,1,5,6,2,3]
arr2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67]

print("largestRectangleArea")
print(solver.largestRectangleArea(arr2))

# print("largestRectangleArea")
# print(solver.largestRectangleArea1(arr2))
#
# print("largestRectangleArea2")
# print(solver.largestRectangleArea2(arr2))