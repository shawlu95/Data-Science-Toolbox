# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        ans = 1
        q = [(root, 1)]
        while q:
            left = 0
            for i in range(len(q)):
                node, pos = q.pop(0)

                if i == 0:
                    left = pos
                else:
                    ans = max(ans, pos - left + 1)

                if node.left:
                    q.append((node.left, 2 * pos))

                if node.right:
                    q.append((node.right, 2 * pos + 1))
        return ans

import Tree

treeVals = [1,3,2,5,3,None,9]
tree = Tree.Tree(treeVals)
root = tree.root

solver = Solution()
solver.widthOfBinaryTree(root)