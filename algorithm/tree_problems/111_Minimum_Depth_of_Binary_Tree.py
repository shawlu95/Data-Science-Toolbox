import Tree
treeVals = [3, 9, 20, None, None, 15, 7]
tree = Tree.Tree(treeVals)
root = tree.root

class Solution():
    def minDepthBFS(self, root):
        """
        :type root: TreeNode
        :rtype: int
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

                if not left and not right:
                    return depth

                if left:
                    next_level.append(left)
                if right:
                    next_level.append(right)

            current_level = next_level
        return depth

    def minDepthDFS(self, root):
        if root is None:
            return 0
        elif root.left is None:
            return self.minDepth(root.right) + 1
        elif root.right is None:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.right), self.minDepth(root.left)) + 1