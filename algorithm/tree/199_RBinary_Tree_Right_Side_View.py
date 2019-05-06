def rightSideView(self, root):
    def collect(node, depth):
        if node:
            # add node when first reaching record depth
            # when depth < len(view), it is not record depth
            if depth == len(view):
                view.append(node.val)
            # try right node first, if not exist, will append left child
            # once len(view) is incremented, appended node will never be overwritten
            collect(node.right, depth+1)
            collect(node.left, depth+1)
    view = []
    collect(root, 0)
    return view


def rightSideView2(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    view = []
    if root:
        level = [root]
        while level:
            # add right most child of current level
            view.append(level[-1].val)
            level = [kid for node in level for kid in (node.left, node.right) if kid]
    return view