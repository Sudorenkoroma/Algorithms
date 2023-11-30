class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def count_nodes(node):
    if node is None:
        return 0
    else:
        # Recursively count the nodes in the left and right subtrees
        left_count = count_nodes(node.left)
        right_count = count_nodes(node.right)

        # Return the total count including the current node
        return left_count + right_count + 1
# def tree_size(node):
#     if node is None:
#         return 0
#     return 1 + tree_size(node.left) + tree_size(node.right)




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

# Count the number of nodes in the binary tree
node_count = count_nodes(root)

# Print the result
print("Number of nodes in the binary tree:", node_count)