import Tree

treeVals = [1, 2, 3, 4, 5, None, 6, None, None, 7]
tree = Tree.Tree(treeVals)
root = tree.root


class Solution:
    def preorderTraversal(self, root):
        ans = []
        if root:
            ans.append(root.val)
            if root.left:
                ans = ans+self.preorderTraversal(root.left)
            if root.right:
                ans = ans+self.preorderTraversal(root.right)
        return ans

    def inorderTraversal(self, root):
        ans = []
        if root:
            if root.left:
                ans = ans + self.inorderTraversal(root.left)

            ans.append(root.val)

            if root.right:
                ans = ans + self.inorderTraversal(root.right)
        return ans

    def postorderTraversal(self, root):
        ans = []
        if root:
            if root.left:
                ans = ans + self.postorderTraversal(root.left)
            if root.right:
                ans = ans + self.postorderTraversal(root.right)
            ans.append(root.val)
        return ans

solver = Solution()
print(solver.postorderTraversal(root))

tree.postOrder()