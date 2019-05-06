class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        """
        If the roots both do not exist, there is nothing to check.
        When recursion reaches leave node's children, there is also nothing to check
        """
        if p is None and q is None:
            return True

        """
        If only one of the two nodes is None, then the trees are different.
        """
        if p is None or q is None:
            return False

        """
        Three conditions must all be true:
            1. values are equal
            2. left children recursion returns true
            3. righr children recursion returns true
        """
        return (p.val == q.val
                and self.isSameTree(p.left, q.left)
                and self.isSameTree(p.right, q.right))

    def isSameTreeStack(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False

        s1 = [p]
        s2 = [q]
        while len(s1) > 0 and len(s2) > 0:
            curr1 = s1.pop()
            curr2 = s2.pop()

            if curr1.val != curr2.val:
                return False

            if curr1.right and curr2.right:
                s1.append(curr1.right)
                s2.append(curr2.right)
            elif curr1.right or curr2.right:
                return False

            if curr1.left and curr2.left:
                s1.append(curr1.left)
                s2.append(curr2.left)
            elif curr1.left or curr2.left:
                return False

        return True


