class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree():
    root = None
    def __init__(self, treeVals):
        if not treeVals:
            return

        nodes = [TreeNode(i) for i in treeVals]
        root = nodes[0]
        for i in range(1, len(treeVals)):
            if treeVals[i] is not None:
                parent = nodes[(i - 1) // 2]
                if i % 2 == 1:
                    parent.left = nodes[i]
                else:
                    parent.right = nodes[i]
        self.root = root

    def inOrder(self):
        def traverse(node):
            if node is None:
                return
            traverse(node.left)
            print(node.val)
            traverse(node.right)
        traverse(self.root)

    def preOrder(self):
        def traverse(node):
            if node is None:
                return
            print(node.val)
            traverse(node.left)
            traverse(node.right)
        traverse(self.root)

    def postOrder(self):
        def traverse(node):
            if node is None:
                return
            traverse(node.left)
            traverse(node.right)
            print(node.val)
        traverse(self.root)

    def flatten(self):
        stack = [self.root]
        res = []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.insert(0, node.left)
                stack.insert(0, node.right)
            else:
                res.append(None)
        while res[-1] is None:
            del res[-1]
        return res
