import Tree
treeVals = [1, 2, 5, 3, 4, None, 6]
# treeVals = []
tree = Tree.Tree(treeVals)
root = tree.root

#
#     1
#    / \
#   2   5
#  / \   \
# 3   4   6

# ouput:
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6

class Solution(object):
    r_child = None
    def flatten(self, root):
        """
        :type root: TreeNode
    D    :rtype: void Do not return anything, modify root in-place instead.
        """

        if root is None:
            return

        # post-order traversal
        self.flatten(root.right)
        self.flatten(root.left)

        # all left children must be None, right child is set to the flattened subtree
        # which grows overtime
        root.left = None
        root.right = self.r_child
        self.r_child = root

solver = Solution()
solver.flatten(root)