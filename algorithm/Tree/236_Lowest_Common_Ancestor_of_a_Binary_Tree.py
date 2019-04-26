# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        parent = {root: None}
        queue = [root]
        while p not in parent or q not in parent:
            node = queue[0]
            queue = queue[1:]
            if node.left:
                parent[node.left] = node
                queue.append(node.left)
            if node.right:
                parent[node.right] = node
                queue.append(node.right)
        path = set()
        while p:
            path.add(p)
            p = parent[p]
        while q not in path:
            q = parent[q]
        return q
