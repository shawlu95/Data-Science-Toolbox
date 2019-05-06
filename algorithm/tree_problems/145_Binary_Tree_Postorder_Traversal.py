import Tree
treeVals = [10,5,-3,3,2,None,11,3,-2,None,1]
# treeVals = []
tree = Tree.Tree(treeVals)
root = tree.root

class Solution(object):
    # modify from pre-order traversal
    def postorderTraversalRecLogic(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        node = root
        stack = []
        res = []
        while stack or node:
            if node:
                stack.append(node)
                res.insert(0, node.val)
                node = node.right
            else:
                node = stack.pop().left
        return res

    # same as above, use build forward
    def postorderTraversalRecLogic2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        node = root
        stack = []
        res = []
        while stack or node:
            if node:
                stack.append(node)
                res.append(node.val)
                node = node.right
            else:
                node = stack.pop().left
        return res[::-1]

    # modify from pre-order traversal
    def postorderTraversal1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        ans = []
        while stack:
            node = stack.pop()

            # insert instead of append
            ans.insert(0, u.val)

            # add left child first
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return ans

    # modify from pre-order traversal. simplified using append instead of insert
    def postorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        ans = []
        while stack:
            node = stack.pop()

            ans.append(node.val)

            # add left child first
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return ans[::-1]

    def postorderNary(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        ans = []
        while stack:
            u = stack.pop()

            # insert instead of append
            ans.insert(0, u.val)

            # add left child first
            for child in u.children:
                stack.append(child)
        return ans

#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1

solver = Solution()
print(solver.postorderTraversalStack(root))