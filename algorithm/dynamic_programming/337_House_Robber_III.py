# https://leetcode.com/problems/house-robber-iii/discuss/79330/step-by-step-tackling-of-the-problem

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# plain
class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        val = 0
        if root.left:
            val += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            val += self.rob(root.right.left) + self.rob(root.right.right)
            
        return max(val + root.val, self.rob(root.left) + self.rob(root.right))

# reuse result
class Solution:
    def rob(self, root: TreeNode) -> int:
        return self.robHelper(root, {})
    
    def robHelper(self, root, hashmap):
        if not root:
            return 0
        
        # memoization
        if root in hashmap:
            return hashmap[root]
        
        # if rob root, must not rob either child
        val = 0
        # rob left child's children
        if root.left:
            val += self.robHelper(root.left.left, hashmap) + self.robHelper(root.left.right, hashmap)
            
        # rob right child's children
        if root.right:
            val += self.robHelper(root.right.left, hashmap) + self.robHelper(root.right.right, hashmap)
            
        
        # either rob root, or does not rob root
        val = max(val + root.val, self.robHelper(root.left, hashmap) + self.robHelper(root.right, hashmap))
        
        # memoization
        hashmap[root] = val
        
        return val

# decounled recursion
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def superrob(node):
            # returns tuple of size two (now, later)
            # now: max money earned if input node is robbed
            # later: max money earned if input node is not robbed
            
            # base case
            if not node: 
                return (0, 0)
            
            # get values
            left, right = superrob(node.left), superrob(node.right)
            
            # rob now: we cannot rob the nodes of root.left and root.right.
            now = node.val + left[1] + right[1]
            
            # rob later: root is not robbed and we are free to rob its left and right subtrees
            later = max(left) + max(right)
            
            return (now, later)
            
        return max(superrob(root))