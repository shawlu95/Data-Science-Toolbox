class Solution:
    def height(self, root):
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        nrows = self.height(root)
        ncols = 2 ** nrows - 1
        ret = [[""] * ncols for x in range(nrows)]

        bfs = [(root, 0, 0, ncols)]
        while bfs:
            # i: depth
            # l:r : range allocated for current node
            node, i, l, r = bfs.pop(0)

            j = (r + l) // 2

            ret[i][j] = str(node.val)

            if node.left:
                bfs.append((node.left, i + 1, l, j))
            if node.right:
                bfs.append((node.right, i + 1, j, r))

        return ret