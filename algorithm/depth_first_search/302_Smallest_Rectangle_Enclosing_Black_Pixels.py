class Solution(object):

    def __init__(self):
        self.top = None
        self.bottom = None
        self.left = None
        self.right = None

    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        if not image:
            return 0

        self.top = x
        self.bottom = x
        self.left = y
        self.right = y

        def dfs(image, x, y):
            if x < 0 or y < 0 or x >= len(image) or y >= len(image[0]) or image[x][y] == '0':
                return

            image[x][y] = '0'
            self.top = min(self.top, x)
            self.bottom = max(self.bottom, x + 1)
            self.left = min(self.left, y)
            self.right = max(self.right, y + 1)

            dfs(image, x + 1, y)
            dfs(image, x - 1, y)
            dfs(image, x, y - 1)
            dfs(image, x, y + 1)

        dfs(image, x, y)

        return (self.right - self.left) * (self.bottom - self.top)