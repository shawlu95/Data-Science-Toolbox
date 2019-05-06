import Tree
treeVals = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, None, 1]
tree = Tree.Tree(treeVals)
root = tree.root

class Solution(object):
    # 112_Path_Sum_I
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def rec(node, partial, sum):
            """\
            DFS
            In the case where a node has been over extended, do not check if partial sum is equal to sum,
            because the node in previous call may not be a leaf node, it may have another child
            """
            if node is None:
                return False
            partial = partial + node.val

            # compare only when current node is a leaf
            if node.left is None and node.right is None:
                return partial == sum

            return (rec(node.left, partial, sum)
                    or rec(node.right, partial, sum))
        return rec(root, 0, sum)

#
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1
solver = Solution()
print(solver.hasPathSum(root, 22))
