# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ans = 0

    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def traverse(node):
            if not node:
                return [0, 0]

            inc = 1
            dec = 1
            if node.left:
                l = traverse(node.left)
                if node.val == node.left.val + 1:
                    dec = l[1] + 1
                elif node.val == node.left.val - 1:
                    inc = l[0] + 1

            if node.right:
                r = traverse(node.right)
                if node.val == node.right.val + 1:
                    dec = max(dec, r[1] + 1)
                elif node.val == node.right.val - 1:
                    inc = max(inc, r[0] + 1)

            self.ans = max(self.ans, dec + inc - 1)

            return [inc, dec]
        traverse(root)
        return self.ans

import Tree

 #     3
 #    / \
 #   2   4
 #  / \   \
 # 3   1   5
 #     \    \
 #      4    6
treeVals = [3, 2, 4, 3, 1, None, 5, None, None, None, 4, None, None, None, 6]
# treeVals = []
tree = Tree.Tree(treeVals)
root = tree.root

solver = Solution()
print(solver.longestConsecutive(root))
