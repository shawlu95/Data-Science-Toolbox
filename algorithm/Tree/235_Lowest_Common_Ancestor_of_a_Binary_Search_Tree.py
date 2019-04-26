# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.lca = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        def helper(node, p, q):
            if not node:
                return

            if p.val <= node.val <= q.val:
                self.lca = node
                return

            self.lowestCommonAncestor(node.left, p, q)
            self.lowestCommonAncestor(node.right, p, q)

        if p.val > q.val:
            p, q = q, p
        helper(root, p, q)
        return self.lca

    # clean code for study
    def lowestCommonAncestor2(self, root, p, q):
        if (max(p.val, q.val) < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (min(p.val, q.val) > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

    def lowestCommonAncestorIter(self, root, p, q):
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root