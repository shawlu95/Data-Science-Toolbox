# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return None

        if root.val == val:
            return root
        elif root.val > val:
            # don't forget to return
            return self.searchBST(root.left, val)
        else:
            # don't forget to return
            return self.searchBST(root.right, val)