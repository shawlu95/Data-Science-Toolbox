
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """

        # 1: (i = 0, j = 5, m=5)
        # 2: (i=2, j=5, m=4)
        # 3: (i=3, j=4, m=4) (i=4, j=5)
        # 4: (i=4, j=4, end) (i=4, j=4, end)
        def build(i, j): # j is exclusive
            if i == j:
                return

            node = TreeNode(preorder[i])

            # can use bsearch here
            m = i + 1
            while m < j and preorder[m] < node.val:
                m += 1

            node.left = build(i + 1, m)
            node.right = build(m, j)

            return node

        return build(0, len(preorder))
