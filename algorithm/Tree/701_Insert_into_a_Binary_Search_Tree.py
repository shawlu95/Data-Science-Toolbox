# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        # ONE TIME SUCCESS!
        def insert(node, val):
            if node.val < val:
                if node.right:
                    insert(node.right, val)
                else:
                    node.right = TreeNode(val)
            elif node.val > val:
                if node.left:
                    insert(node.left, val)
                else:
                    node.left = TreeNode(val)

        insert(root, val)
        return root

    def insertIntoBST2(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            # create a leaf node
            return TreeNode(val)

        # traverse to the correct leaf node
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)

        # do not disturb non-leaf node
        return root