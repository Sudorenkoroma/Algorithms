class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder_traversal(node):
    if node is not None:
        # Обробка поточного вузла перед рекурсивним обходом лівого і правого піддерев
        print(node.value, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)

# Приклад використання:
# Створення бінарного дерева
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Виклик функції для обходу бінарного дерева в порядку передзамовлення
preorder_traversal(root)
print(root)