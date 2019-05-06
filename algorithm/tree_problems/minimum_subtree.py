import Tree
root = Tree.Tree([2,1,3,None,4,None,7]).root

def countNotes(root):
    def helper(node):
        if node is None:
            return 0
        return 1 + helper(node.left) + helper(node.right)
    return helper(root)

print(countNotes(root))


treeVals = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, None, 1]
root = Tree.Tree(treeVals).root

class Solution():
    def __init__(self):
        self.ans = float('inf')
        self.subtree = None

    def minimumSubtree(self, root):
        def helper(node):
            if node is None:
                return 0

            sum = 1 + helper(node.left) + helper(node.right)

            if sum < self.ans:
                self.ans = sum
                self.subtree = node

            return sum
        helper(root)
        return self.subtree, self.ans
solver = Solution()
subtree, count = solver.minimumSubtree(root)
print(subtree.val)
print(count)

#
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1