class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def postorder_traversal(node):
    if node is not None:
        # Рекурсивний обхід лівого піддерева
        postorder_traversal(node.left)

        # Рекурсивний обхід правого піддерева
        postorder_traversal(node.right)

        # Обробка поточного вузла
        print(node.value, end=" ")


# Приклад використання:
# Створення бінарного дерева
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Виклик функції для обходу бінарного дерева в порядку післязамовлення
postorder_traversal(root)


