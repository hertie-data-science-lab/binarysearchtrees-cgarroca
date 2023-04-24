from Tree_to_BST import Node, convert, inorder

root = Node(8)
root.left = Node(3)
root.right = Node(5)
root.left.left = Node(10)
root.left.right = Node(2)
root.right.left = Node(4)
root.right.right = Node(6)

convert(root)
inorder(root)