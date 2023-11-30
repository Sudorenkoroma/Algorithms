class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inorder_traversal(node):
    if node is not None:
        # Інордерний обхід лівого піддерева
        inorder_traversal(node.left)

        # Обробка поточного вузла
        print(node.value, end=" ")

        # Інордерний обхід правого піддерева
        inorder_traversal(node.right)




# Приклад використання:
# Створення бінарного дерева
root = TreeNode(1)
# root.left = TreeNode(2)
root.right = TreeNode(2)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
root.right.left = TreeNode(3)
# root.right.right = TreeNode(7)


out = inorder_traversal(root)
print(out)