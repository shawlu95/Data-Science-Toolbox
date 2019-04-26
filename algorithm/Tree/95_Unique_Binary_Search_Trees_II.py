from Tree import TreeNode
import Tree

# https://leetcode.com/problems/unique-binary-search-trees-ii/discuss/31609/Simple-python-solution
class Solution(object):
    def generateTrees1(self, n):
        return self.cal([i for i in range(1, n + 1)])

    def cal(self, lst):
        if not lst: return [None]
        res = []
        for i in range(len(lst)):
            for left in self.cal(lst[:i]):
                for right in self.cal(lst[i + 1:]):
                    node = TreeNode(lst[i])
                    node.left = left
                    node.right = right
                    res += [node]
        return res

    def generateTrees2(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        def generate(i, j):
            if j < i:
                return [None]
            elif j == i:
                return [TreeNode(i)]
            else:
                res = []
                # k is the root of BST
                for k in range(i, j + 1):
                    # what goes to the left must all be smaller than k
                    left = generate(i, k - 1)

                    # what foes to the right must all be larger than k
                    right = generate(k + 1, j)
                    for l in left:
                        for r in right:
                            root = TreeNode(k)
                            root.left = l
                            root.right = r
                            res.append(root)
                return res
        if n == 0: # corner case
            return []
        else:
            # the problem requires starting with 1, not 0
            return generate(1, n)

solver = Solution()
ans = solver.generateTrees2(2)
for root in ans:
    tree = Tree.Tree(None)
    tree.root = root
    print(tree.flatten())