import Tree
treeVals = [1, 2, 3, 4, 5, 6]
tree = Tree.Tree(treeVals)
root = tree.root

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        def traverse(node, l):
            if node is None:
                return
            traverse(node.left, l)
            ans.append(node.val)
            traverse(node.right, l)
        traverse(root, ans)

        return ans

    def inorderTraversalStack1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # if root is None:
        #     return []
        # output = []
        # return printInorder(root, output)

        result = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()

            # do something --------
            result.append(curr.val)
            # ---------------------

            curr = curr.right
        return result

    # compare to def preorderTraversal3(self, root): in 144 Preorder Traversak
    def inorderTraversalStack2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # if root is None:
        #     return []
        # output = []
        # return printInorder(root, output)

        result = []
        stack = []
        curr = root
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()

                # do something --------
                result.append(curr.val)
                # ---------------------

                curr = curr.right
        return result

    def inorderTraversalFlat(self, root):

        # if not root:
        #     return []
        #
        # result, stack = [], [(root, False)]
        #
        # while stack:
        #     cur, visited = stack.pop()
        #     if visited:
        #         result.append(cur.val)
        #     else:
        #         if cur.right:
        #             stack.append((cur.right, False))
        #         stack.append((cur, True))
        #         if cur.left:
        #             stack.append((cur.left, False))
        # return result

        result, stack = [], [(root, False)]

        while stack:
            cur, visited = stack.pop()
            # either check existence here, or check existence before appending left & right child
            # also, if input is null, the exception is handled gracefully
            if cur:
                if visited:
                    # do something --------
                    result.append(cur.val)
                    # ---------------------
                else:
                    stack.append((cur.right, False))
                    stack.append((cur, True))
                    stack.append((cur.left, False))
        return result



solver = Solution()
ans = solver.inorderTraversalFlat(root)
print(ans)