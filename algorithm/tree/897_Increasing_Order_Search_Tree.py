# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        # trivial solution, rebuild list and reconstruct
        l = []
        def inOrder(node):
            if not node:
                return 
            
            cur = inOrder(node.left)
            
            l.append(node.val)
            
            inOrder(node.right)
        
        inOrder(root)
        head = cur = TreeNode(None)
        for val in l:
            cur.right = TreeNode(val)
            cur = cur.right
        return head.right

    def increasingBST2(self, root: TreeNode) -> TreeNode:

        # use a class attribute to avoid losing variable in recursive stack
        dummy = self.cur = TreeNode(None)
        
        def inOrder(node):
            if not node:
                return
            
            inOrder(node.left)
            self.cur.right = node
            self.cur.right.left = None # trace the tree to understand this operation
            self.cur = self.cur.right
            
            inOrder(node.right)
        inOrder(root)
        return dummy.right
