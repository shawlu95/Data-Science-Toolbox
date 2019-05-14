### 二叉树

#### 时间
用O(N)的时间把规模拆成2个T(N/2):

T(N) = O(N) + 2 T(N/2) = O(N) + 2 O(N/2) + 4 T(N/4) = ... = logN * O(N) + N * T(1) = O(NlogN)


用O(1)的时间把规模拆成2个T(N/2):
T(N) = O(1) + 2T(N/2) = 2 O(1) + 4T(N/4) = ... = logN O(1) + N * T(1) = O(N)

#### Iterative Traversal
* Pre-order: [[Link](https://leetcode.com/problems/binary-tree-preorder-traversal)][[Code](144_binary_tree_preorder_traversal.py)].
* In-order: [[Link](https://leetcode.com/problems/binary-tree-inorder-traversal)][[Code](94_binary_tree_inorder_traversal.py)].
* Post-order: [[Link](https://leetcode.com/problems/binary-tree-postorder-traversal)][[Code](145_binary_tree_postorder_traversal.py)].

```Python
def preorderTraversal(self, root):
    if not root:
        return []
    stack = [root]
    ans = []
    while stack:
        node = stack.pop()

        # do something --------
        ans.append(node.val)
        # ---------------------

        # add right child first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return ans

def inorderTraversal(self, root):
    # if root is None:
    #     return []

    result = []
    stack = []
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()

        # do something --------
        result.append(cur.val)
        # ---------------------

        cur = cur.right
    return result
```



#### Recursion Traversal

```Python
def preorderTraversal(root):
    ans = []
    def traverse(node, l):
        if node is None: return
        ans.append(node.val)
        traverse(node.left, l)
        traverse(node.right, l)
    traverse(root, ans)
    return ans

def inorderTraversal(root):
    ans = []
    def traverse(node, l):
        if node is None: return
        traverse(node.left, l)
        ans.append(node.val)
        traverse(node.right, l)
    traverse(root, ans)
    return ans

def postorderTraversal(root):
    ans = []
    def traverse(node, l):
        if node is None: return
        traverse(node.left, l)
        traverse(node.right, l)
        ans.append(node.val)
    traverse(root, ans)
    return ans
```

#### Recursion Divide & Conquer

```Python
def divideConquerTraversal(self, root):
	def traverse(node):
		if node is None: return []
		l = traverse(node.left)
		r = traverse(node.right)

        # preorder
		# return [node.val] + l + r

        # inorder
        # return l + [node.val] + r

        # post-order
        return l + r + [node.val]
	return traverse(root)
```

#### Primer
* Binary tree path (DC, DFS) [[Link](https://leetcode.com/problems/binary-tree-paths)][[Code](257_binary_tree_paths.py)].
* Minimum subtree (DC) [[Link](https://starllap.space/2017/05/30/LintCode-596-Minimum-Subtree/)][[Code](minimum_subtree.py)].

#### Application
* Balanced binary tree [[Link][1]][[Code](110_balanced_binary_tree)].
* Tuple return: binary tree maximum node [[Link](https://www.lintcode.com/problem/binary-tree-maximum-node/description)][[Code](binary_tree_maximum_node.py)].

[1] https://leetcode.com/problems/balanced-binary-tree/
