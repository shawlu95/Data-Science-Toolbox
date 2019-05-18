class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Divide and conquer.
        """
        if not root or root == p or root == q: return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        # this is LCA: one node is in left, one node is in right
        if l and r: return root

        # return LCA to parent stack
        if l: return l # one node is found in left subtree
        if r: return r # one node is found in right subtree

        # none of p or q is root's children
        return None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        """
        First build a map linking child to parent.
        When construct entire path from p to root.
        Traverse starting with q, end when first node is found in common.
        """
        parent = {root : None}
        queue = [root]
        while p not in parent or q not in parent:
            node = queue.pop()
            if node.right:
                parent[node.right] = node
                queue.append(node.right)
            if node.left:
                parent[node.left] = node
                queue.append(node.left)
        path = set()
        while p:
            path.add(p)
            p = parent[p]
        while q not in path:
            q = parent[q]
        return q
