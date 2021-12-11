 # Binary Search Tree is a node-based binary tree data structure which has the following properties:
 # The left subtree of a node contains only nodes with keys lesser than the node’s key.
 # The right subtree of a node contains only nodes with keys greater than the node’s key.
 # The left and right subtree each must also be a binary search tree.

 # [7, 5, 1, 8, 3, 6, 0, 9, 4, 2] for giving array :

def search(root, key):
    # Base Cases: root is null or key is present at root
    if root is None or root.val == key:
        return root

    # Key is greater than root's key
    if root.val < key:
        return search(root.right, key)

    # Key is smaller than root's key
    return search(root.left, key)

