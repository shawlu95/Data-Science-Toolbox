import Tree
treeVals = [-10,9,20,None,None,15,7]
# treeVals = []
tree = Tree.Tree(treeVals)
root = tree.root

class Solution:
    res = -float('inf')

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.helper(root)
        return self.res

    def helper(self, root):
        if root is None:
            return 0

        leftMax = self.helper(root.left)
        rightMax = self.helper(root.right)

        # the best path may be left - node - right
        dual_sum = root.val + leftMax + rightMax

        # the best path may be left/right - node
        side_sum = root.val + max(leftMax, rightMax, 0)

        # or the node itself may be the best "path" containing a single node (e.g. when it is the only positive integers)
        self.res = max(side_sum, dual_sum, self.res)

        return side_sum

solver = Solution()
solver.helper(root)