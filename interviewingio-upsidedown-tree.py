

def turnTreeUpsideDown(root):
    curr = root
    while curr:
        left_child = curr.left
        if left_child:
            left_child.right = curr
            left_child.left = curr.right
            if curr == root:
                curr.right = None
                curr.left = None
        curr = left_child
    return curr
    """
    starting from root, for each node curr:
        hold on to the left child
        leftchild.right = curr
        leftchild.left = curr.right
        only for root:
            curr.right = None
            curr.left = None
        curr = left child

        1        2
       / \      / \
      2   3    3   1
     /  \
    4    5
    """


turnTreeUpsideDown()
