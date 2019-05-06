# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        val = root.val
        def check(node, val):
            if not node:
                return True
            return node.val == val and check(node.left, val) and check(node.right, val)
        
        return check(root, val)
        