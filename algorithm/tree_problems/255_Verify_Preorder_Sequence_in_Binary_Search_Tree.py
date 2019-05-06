
class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        st = []
        low = float('-inf')
        for x in preorder:
            if x < low:
                return False
            while st and st[-1] < x:
                low = st.pop()
            st.append(x)
        return True

    def is_preorder(self, preorder, s, e, lb, ub):
        # nothing to iterate
        if s >= e:
            return True

        # j marks the first node which is greater than root, j is a right child of the root
        j = e + 1 # init to an impossible index
        r = preorder[s]
        for i in range(s, e + 1):
            if lb <= preorder[i] <= ub:
                if preorder[i] > r:
                    j = i
                    break
            else:
                return False

        # all nodes to the left of j must be smaller than root r
        return self.is_preorder(preorder, s + 1, j - 1, lb, r - 1) and self.is_preorder(preorder, j, e, r + 1, ub)

    def verifyPreorder2(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        return self.is_preorder(preorder, 0, len(preorder) - 1, float('-inf'), float('inf'))
solver = Solution()
# solver.verifyPreorder([5,2,6,1,3])
solver.verifyPreorder2([5,2,1,3,6])