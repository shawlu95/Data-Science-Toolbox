class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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