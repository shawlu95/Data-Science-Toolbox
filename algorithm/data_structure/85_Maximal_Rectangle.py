class Solution:
# @param matrix, a list of lists of 1 length string
# @return an integer
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        h, w = len(matrix), len(matrix[0])
        m = [[0]*w for _ in range(h)]
        for j in range(h):
            for i in range(w):
                if matrix[j][i] == '1':
                    m[j][i] = m[j-1][i] + 1
        return max(self.largestRectangleArea(row) for row in m)

    def largestRectangleArea(self, height):
        height.append(0)
        stack, size = [], 0
        for i in range(len(height)):
            while stack and height[stack[-1]] > height[i]:
                h = height[stack.pop()]
                w = i if not stack else i-stack[-1]-1
                cand = h*w
                # print(cand)
                size = max(size, cand)
            stack.append(i)
        return size

arr = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
solver = Solution()
solver.maximalRectangle(arr)