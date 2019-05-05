# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# stack
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        running = 0
        node = root
        stack = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.right
            node = stack.pop()

            running += node.val
            node.val = running

            node = node.left
        return root

# recursion
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.running = 0
        def traverse(node):
            if not node:
                return 0

            traverse(node.right)

            self.running += node.val
            node.val = self.running

            traverse(node.left)

        traverse(root)
        return root
