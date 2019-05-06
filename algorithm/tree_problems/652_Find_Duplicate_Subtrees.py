# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        count = {}
        ans = []

        # serialize every subtree, and count its appearance
        def collect(node):
            if not node:
                return "#"

            l = collect(node.left)
            r = collect(node.right)
            serial = "{},{},{}".format(node.val, l, r)

            count[serial] = count.get(serial, 0) + 1
            if count[serial] == 2:
                ans.append(node)

            return serial

        collect(root)
        return ans