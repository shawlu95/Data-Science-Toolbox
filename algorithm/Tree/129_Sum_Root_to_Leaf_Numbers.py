import Tree
treeVals = [4, 9, 0, 5, 1]
# treeVals = []
tree = Tree.Tree(treeVals)
root = tree.root

class Solution(object):
    nums = []
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        self.nums = []

        def helper(node, num):
            if not node:
                return

            # nice touch: only add once
            num = num * 10 + node.val

            # if current node is a leaf, append num to results
            if not node.left and not node.right:
                self.nums.append(num)

            # go one step further, None node is handled in base case
            helper(node.left, num)
            helper(node.right, num)

        helper(root, 0)

        return sum(self.nums)

solver = Solution()
print(solver.sumNumbers(root))

tree.postOrder()