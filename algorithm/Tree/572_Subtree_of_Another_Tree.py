class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def isSameTree(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            return (isSameTree(t1.left, t2.left) and isSameTree(t1.right, t2.right))
        if isSameTree(s, t):
            return True
        if s.left and self.isSubtree(s.left, t):
            return True
        if s.right and self.isSubtree(s.right, t):
            return True
        return False