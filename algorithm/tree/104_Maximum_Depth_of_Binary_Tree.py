class Solution():
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if not root:
            return 0

        depth = 0
        current_level = [root]

        while current_level:
            depth += 1
            next_level = []
            for node in current_level:
                left = node.left
                right = node.right

                if left:
                    next_level.append(left)
                if right:
                    next_level.append(right)

            current_level = next_level
        return depth

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def helper(node):
            if node is None:
                return 0

            l_depth = helper(node.left)
            r_depth = helper(node.right)

            return max(l_depth, r_depth) + 1

        return helper(root)