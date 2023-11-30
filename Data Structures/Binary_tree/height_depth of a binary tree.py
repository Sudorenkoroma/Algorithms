class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def tree_height(node):
    if node is None:
        return 0
    else:
        # Recursively calculate the height of the left and right subtrees
        left_height = tree_height(node.left)
        right_height = tree_height(node.right)

        # Return the maximum height plus 1 (to account for the current level)
        return max(left_height, right_height) + 1
# def tree_height(node):
#     if node is None:
#         return 0
#     return 1 + max(tree_height(node.left), tree_height(node.right))


# Example usage:
# Construct a binary tree:    1
#                           /   \
#                          2     3
#                         / \
#                        4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Calculate the height of the binary tree
height = tree_height(root)

# Print the result
print("Height of the binary tree:", height)