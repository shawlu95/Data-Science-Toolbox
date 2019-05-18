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
    class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Stack solution
        node    stack       connect right
        1       5, 2        1 -> 2
        2       5, 4, 3     2 -> 3
        3       5, 4        3 -> 4
        4       5           4 -> 5
        5       6           5 -> 6
        6       break
        """
        if not root: return

        # warning: if root is None,
        # [None] will trigger while loop
        stack = [root]
        print(stack)
        while stack:
            node = stack.pop()
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)

            node.left = None
            if stack:
                node.right = stack[-1]
            else:
                node.right = None
            # <- breakpoint

    r_child = None
    def flatten(self, root):
        """
        Post-order
        """
        if root is None: return

        # post-order traversal
        self.flatten(root.right)
        self.flatten(root.left)

        # all left children must be None, right child is set to the flattened subtree
        # which grows overtime
        root.left = None
        root.right = self.r_child
        self.r_child = root


    last = None
    def flatten(self, root: TreeNode) -> None:
        """
        Pre-order
        """
        if not root: return

        if self.last:
            self.last.left = None
            self.last.right = root

        self.last = root
        right = root.right
        self.flatten(root.left)
        self.flatten(right)

solver = Solution()
solver.flatten(root)
