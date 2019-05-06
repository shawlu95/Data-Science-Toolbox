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
        ncols = 2 ** nrows - 1 # always odd
        ret = [[""] * ncols for x in range(nrows)]

        bfs = [(root, 0, 0, ncols)]
        while bfs:
            # d: depth
            # l:r : range allocated for current node
            node, d, l, r = bfs.pop(0)

            m = (r + l) // 2

            ret[i][m] = str(node.val)

            if node.left:
                bfs.append((node.left, d + 1, l, m))
            if node.right:
                bfs.append((node.right, d + 1, m, r))

        return ret
