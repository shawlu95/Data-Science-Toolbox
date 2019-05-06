class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# cleaner code than solution
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        For any node in inorder, its left hand side are in left subtree, vice versa for right hand side.
        Traverse the tree in preorder. Every time a node is dequeued from preorder sequence, find from the inorder sequence what goes left and what goes right (end index exclusive)
        """

        def buildNode(i, j):
            # base case
            if i == j: return None

            parent = TreeNode(preorder.pop(0))
            splitIdx = inorder.index(parent.val)

            parent.left = buildNode(i, splitIdx)
            parent.right = buildNode(splitIdx + 1, j)

            return parent

        return buildNode(0, len(preorder))


class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # last index is exclusive!
        def helper(in_left=0, in_right=len(inorder)):
            nonlocal pre_idx
            # if there is no elements to construct subtrees
            if in_left == in_right:
                return None

            # pick up pre_idx element as a root
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)

            # root splits inorder list
            # into left and right subtrees
            index = idx_map[root_val]

            # recursion
            pre_idx += 1
            # build left subtree
            root.left = helper(in_left, index) # last index is exclusive!
            # build right subtree
            root.right = helper(index + 1, in_right) # last index is exclusive!
            return root

        # start from first preorder element
        pre_idx = 0
        # build a hashmap value -> its index
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper()

solver = Solution()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
solver.buildTree(preorder, inorder)