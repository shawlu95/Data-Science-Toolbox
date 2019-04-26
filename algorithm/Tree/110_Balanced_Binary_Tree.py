import Tree
treeVals = [3, 9, 20, None, None, 15, 7]
tree = Tree.Tree(treeVals)
root = tree.root

class Solution():
    # use a global variable to track if any subtree is unbalanced
    ans = True

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def helper(node):
            if node is None:
                return 0

            l_depth = helper(node.left)
            r_depth = helper(node.right)

            if abs(l_depth - r_depth) > 1:
                self.ans = False

            return max(l_depth, r_depth) + 1

        helper(root)
        return self.ans

solver = Solution()
print(solver.isBalanced(root))
