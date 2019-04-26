# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def successor(self, node):
        """
        One step right and then always left
        """
        cur = node.right
        while cur.left:
            cur = cur.left
        return cur.val

    def predecessor(self, node):
        """
        One step left and then always right
        """
        cur = node.left
        while cur.right:
            cur = cur.right
        return cur.val

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        if root.val < key:
            # node to delete is in the right subtree
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            # delete from the left subtree
            root.left = self.deleteNode(root.left, key)
        else:
            # the node is a leaf
            # if not (root.left and root.right): # wrong
            # if not (root.lefet or root.right) # right
            if not root.left and not root.right:
                root = None
            elif root.right:
                # the node is not a leaf and has a right child
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                # the node is not a leaf, has no right child, and has a left child
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
        return root
