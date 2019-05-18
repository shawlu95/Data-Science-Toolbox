https://www.youtube.com/watch?v=gcULXE7ViZw

def findMin(root):
    while cur.left:
        cur = root.left
    return cur

def delete(root, val):
    if not root:
        return None
    elif val < root.val:
        root.left = delete(root.left, val)
    elif val > root.val:
        root.right = delete(root.right, val)
    else:
        if not root.left and not root.right:
            root = None
        elif root.left is None:
            root = root.right
        elif root.right is None:
            root = root.left
        else:
            rMin = findMin(root.right)
            root.val = rMin.val
            root.right = delete(root.right, rMin.val)
        return root