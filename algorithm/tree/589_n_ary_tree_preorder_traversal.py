"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        
        def traverse(node, ans):
            if not node:
                return
            
            ans.append(node.val)
            for child in node.children:
                traverse(child, ans)
                
        traverse(root, ans)
        return ans
        
        