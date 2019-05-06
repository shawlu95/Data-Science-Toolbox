# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ans = 0

    # top-down, my solution, one-pass success
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def traverse(node, parent, seq):
            if not node:
                return

            if parent and parent.val + 1 == node.val:
                seq += 1
            else:
                seq = 1

            self.ans = max(self.ans, seq)

            traverse(node.left, node, seq)
            traverse(node.right, node, seq)

        traverse(root, None, 0)

        return self.ans

    # bottom-up
    def traverse2(node):
        if not node:
            return 0

        l = traverse(node.left) + 1
        r = traverse(node.right) + 1

        # always check existance first
        if node.left and node.left.val != node.val + 1:
            l = 1

        # always check existance first
        if node.right and node.right.val != node.val + 1:
            r = 1

        self.ans = max(l, r, self.ans)
        return max(l, r)

    traverse(root)

    return self.ans



